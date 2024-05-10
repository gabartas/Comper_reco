#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json
import sys
import time

import jsonschema

from ..logger import loggering
from .errors import ComponentMissingError
from .strategyObjects import (ComponentObject, ManipulableObject,
                              PedagogicStrategy, Predicate, SelectionProcedure,
                              SelectionRule, StrategyDescription)


logging = loggering.getLogger()


def loadStrategy(rule_file, schema_rule_file):
    logging.info("Strategy : reading[" + rule_file + "] ...")
    # loading SP
    try:
        f = open(rule_file, 'r')
    except IOError:
        logging.error('cannot open %s', rule_file)
        raise IOError("Strategy " + rule_file + " doesn't exist")
    else:
        strategy = json.loads("".join(f.readlines()))
        f.close()

    # loading grammar
    try:
        f = open(schema_rule_file, 'r', encoding='utf-8')
    except IOError:
        logging.error('cannot open', schema_rule_file)
    else:
        strategy_grammar = json.loads("".join(f.readlines()))
        f.close()

    logging.info("Strategy loaded...")

    return strategy, strategy_grammar


def loadJson(file):
    f = open(file, "r", encoding='utf-8')
    jContent = json.load(f)
    f.close()

    return jContent


def createSPObjectFromFile(file):
    SP = loadJson(file)
    SP_object = SP["pedagogic_strategy"]

    return StrategyDescription(
        file,
        SP_object["Object_id"],
        SP_object["Object_name"],
        SP_object["Object_description"],
        SP_object["authors"],
        SP_object["version"],
        SP_object["Object_type"],
        SP_object["public_visibility"]
    ) \



def validationStrategySyntax(strategy, strategy_grammar):
    logging.info("Strategy : validation ...")

    nb_errors = 0
    try:
        jsonschema.validate(instance=strategy, schema=strategy_grammar)
    except jsonschema.ValidationError as e:
        logging.error(e)
        nb_errors += 1
        # sys.exit(1)
    if nb_errors > 0:
        logging.critical(" --> invalid")
        sys.exit(1)
    logging.info(" --> Conform")


def importStrategy(strategy):
    objects = {}
    logging.info("Strategy : object creation ...")
    # ------------------------------------------------------
    # ok
    PS_id = strategy["pedagogic_strategy"]["Object_id"]
    PS_name = strategy["pedagogic_strategy"]["Object_name"]
    PS_class = strategy["pedagogic_strategy"]["Object_class"]
    PS_type = strategy["pedagogic_strategy"]["Object_type"]
    PS_descr = strategy["pedagogic_strategy"]["Object_description"]
    PS_components = strategy["pedagogic_strategy"]["components"]
    PS_objective_parameters = strategy["pedagogic_strategy"]["content"]["objective"]
    PS_selection_parameters = strategy["pedagogic_strategy"]["content"]["selection_parameters"]
    PS_ordering_parameters = strategy["pedagogic_strategy"]["content"]["ordering_parameters"]
    PS_resources_parameters = strategy["pedagogic_strategy"]["content"]["resource_parameters"]

    objects[PS_id] = PedagogicStrategy(PS_id, PS_name, PS_descr, PS_type, PS_class, PS_components,
                                       PS_objective_parameters, PS_selection_parameters, PS_ordering_parameters, PS_resources_parameters)

    # ------------------------------------------------------
    for selection_procedure in strategy["selection_procedures"]:
        SP_id = selection_procedure["Object_id"]
        SP_name = selection_procedure["Object_name"]
        SP_class = selection_procedure["Object_class"]
        SP_type = selection_procedure["Object_type"]
        SP_descr = selection_procedure["Object_description"]
        SP_components = selection_procedure["components"]
        SP_content = selection_procedure["content"]

        objects[SP_id] = SelectionProcedure(
            SP_id, SP_name, SP_descr, SP_type, SP_class, SP_components, SP_content)

    for selection_rule in strategy["selection_rules"]:
        SR_id = selection_rule["Object_id"]
        SR_name = selection_rule["Object_name"]
        SR_class = selection_rule["Object_class"]
        SR_type = selection_rule["Object_type"]
        SR_descr = selection_rule["Object_description"]
        SR_components = selection_rule["components"]
        SR_content = selection_rule["content"]

        objects[SR_id] = SelectionRule(
            SR_id, SR_name, SR_descr, SR_type, SR_class, SR_components, SR_content)

    for predicate in strategy["predicates"]:
        P_id = predicate["Object_id"]
        P_name = predicate["Object_name"]
        P_class = predicate["Object_class"]
        P_type = predicate["Object_type"]
        P_descr = predicate["Object_description"]
        P_components = predicate["components"]
        P_formula = predicate["formula"]

        P = Predicate(P_id, P_name, P_descr, P_type,
                      P_class, P_formula, P_components)
        P.compil()
        objects[P_id] = P

    for obj in strategy["parameters"]:  # ok
        objects[obj["name"]] = obj["value"]

    t = [("parameter" if not ManipulableObject.isAManipulableObject(
        v) else v.getClass(), k) for k, v in objects.items()]
    d = {c: (len([i2 for (c2, i2) in t if c2 == c]), [
             i2 for (c2, i2) in t if c2 == c]) for (c, i) in t}
    # d["NumberOfObject"] = len(t)

    logging.info(" --> %s objects imported", str(len(objects)))

    details = ""
    for k, v in d.items():
        details += f"\t\t {k} : {v} \n"
    logging.info(" details : \n %s", details)

    return objects, PS_id


def verifyComponentsIntegrity(dictObjects):
    missing = []
    used = {id_o: (False if "PS" not in id_o else True)
            for id_o in dictObjects.keys()}
    for id_o, obj in dictObjects.items():
        if ComponentObject.isAComponentObject(obj):
            components_l = obj.getComponentsList()
            for component in components_l:
                if component not in dictObjects.keys():
                    logging.error(
                        "[Error] Component %s, required by %s, is missing", component, obj.getName())
                    if component not in missing:
                        missing.append(component)
                else:
                    used[component] = True

    if len(missing) != 0:
        logging.error("[Error] %s components are missing : %s",
                      len(missing), str(missing))
        raise ComponentMissingError("", "")

    t = [id_o for id_o, used_id in used.items() if not used_id]
    if len(t) != 0:
        logging.warning(
            "[Warning] %s components are not used : %s", len(t), str(t))

    return None if len(missing) else missing


def insertingComponents(dictObjects):
    componentObjects = [obj for k, obj in dictObjects.items(
    ) if ComponentObject.isAComponentObject(obj)]

    logging.info("Updating %s components ...", len(
        [obj.getId() for obj in componentObjects]))

    while len(componentObjects) != 0:
        for obj in componentObjects:
            if obj.canUpdateComponents(dictObjects):
                logging.debug("Updating %s", obj.getId())
                time.sleep(0.01)
                obj.updateComponents(dictObjects)
                componentObjects.remove(obj)

    # on recompile les predicats
    for k, obj in dictObjects.items():
        if Predicate.isAPredicate(obj):
            obj.compil()

    logging.info("Updating done")
