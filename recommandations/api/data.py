#!/usr/bin/python3
# -*- coding: utf-8 -*-

import copy
import datetime
import json
import os
import sys

from ..algorithm.algo import applyStrategy
from ..logger import loggering
from ..pedagogicStrategy import ioStrategy as ps
from ..referential.errors import NodeObjectError, ObjectiveError
from ..referential.objectives import Objectif
from ..referential.profile import Profil
from ..referential.referential import Node, Referential, ResourceNode
from .consts import DATA_PATH, SCHEMA_PS_FILE, inverse_relations


logger = loggering.getLogger()
sys.path.append("..")


def primitiveReferential(inv_relations=inverse_relations):
    my_ref = Referential("Init", inv_relations)
    return my_ref


def loadReferential(inv_relations, idReferential, profile_data):
    # to do before importing data
    referential = Referential("Framework-"+str(idReferential), inv_relations)

    referential.id = idReferential

    referential.add_node(Node(1, "Framework-"+str(idReferential), "Framework"))
    referential.setRacine(1)

    id_n = 1
    # we add nodes
    added = []
    for obj in profile_data["objects"]:
        id_n += 1
        if obj["name"] not in added:
            added.append(obj["name"])
            referential.add_node(
                Node(id_n, obj["name"], obj["type"].replace("Skills", "Skill")))

    # we add ressources
    if profile_data["resources"] == []:
        try:
            raise NodeObjectError(
                profile_data["ressources"], "profile has no ressources")
        except Exception as e:
            logger.error("[Warning] No ressources found : %s", e)
    else:
        added = []
        for obj in profile_data["resources"]:
            if obj["id"] not in added:
                added.append(obj["id"])
                referential.add_node(ResourceNode(obj["id"],
                                                  obj["name"],
                                                  obj["interactivityType"],
                                                  obj["learningResourceType"],
                                                  obj["significanceLevel"],
                                                  obj["difficulty"],
                                                  obj["typicalLearningTime"],
                                                  obj["learningPlatform"],
                                                  obj["location"],
                                                  obj["author"],
                                                  obj["language"],
                                                  obj["generative"]))

    # we add relations
    seen = []
    for obj in profile_data["objects"]:
        if obj["name"] not in seen:
            seen.append(obj["name"])

            # All nodes with no links composes, isSkillOf nor isKnowledgeOf are link to the root
            if len(obj["relations"]["composes"] + obj["relations"]["isSkillOf"] + obj["relations"]["isKnowledgeOf"]) == 0:
                referential.add_link(
                    1, referential.getIdByName(obj["name"]), "comprises")

            for relation, nodes in obj["relations"].items():
                for nodeName in nodes:
                    nameFrom = obj["name"]
                    nameTo = nodeName

                    if relation not in ["isTrainingOf", "isLearningOf"]:
                        id_from = referential.getIdByName(nameFrom)
                    else:
                        id_from = nameFrom

                    if relation not in ["hasTraining", "hasLearning"]:
                        id_to = referential.getIdByName(nameTo)
                    else:
                        id_to = nameTo

                    if id_from == -1:
                        raise NodeObjectError(
                            "nameFrom", nameFrom + " from Not in referential")
                    if id_to == -1:
                        raise NodeObjectError(
                            "nameTo", nameTo + " to Not in referential")

                    referential.add_link(id_from, id_to, relation)

    return referential


def reloadReferential(idReferential, profile_data):
    return loadReferential(inverse_relations, idReferential, profile_data)


def loadProfile(referential, profileValues):

    def keysNameToIds(referential, profileValues):
        idProfileValues = {}

        for k, v in profileValues.items():
            idProfileValues[referential.getIdByName(k)] = v

        return idProfileValues

    return Profil(copy.copy(referential), keysNameToIds(referential, profileValues))


def loadObjectives(profile, objectives_SP_param, liste_objectives=[]):
    # default intention
    default_intention = objectives_SP_param["defaultIntention"]
    # number max of objectives
    max_objectives = objectives_SP_param["maxObjectives"]

    if not isinstance(liste_objectives, list):
        logger.error("[Objectives] Empty Objective List")
        raise ObjectiveError(liste_objectives, "Objective List empty")
    else:
        for i in liste_objectives:
            if not isinstance(i, list) and len(i) == 2:
                logger.error(
                    "[Objectives] Form [[name_node, intention], ...] not found")
                raise ObjectiveError(
                    liste_objectives, "Form [[name_node, intention], ...] not found")

    objs = []
    if liste_objectives == []:
        """
        if no objectives set
        l'objectif n'est pas défini on prend les compétences liées à la racine avec l'intention révision
        competencies_1st_level = profile.getRacine().getDescendants("comprises")
        for comp in sorted(competencies_1st_level, key=functools.cmp_to_key(
                ref.sortCompetenciesByMastery_KnownANDTrust_Id)):
            if ref.Objectif(profile, profile.getNodeById(comp.getId()),
                default_intention) not in objs:
            objs.append(ref.Objectif(profile, profile.getNodeById(comp.getId()), default_intention))
        """

        pass
    else:
        for name_node, intention in liste_objectives:
            # on ne passe pas d'intention on récupère l'intention par défaut
            if intention == "":
                intention = default_intention
            # Si noeud non défini on prend les compétences liées à la racine
            if name_node == "":
                for comp in sorted(profile.getRacine().
                                   getDescendants("comprises"),
                                   key=lambda node: node.getId()):
                    if Objectif(profile, profile.getNodeById(comp.getId()),
                                intention) not in objs:
                        objs.append(Objectif(
                            profile, profile.getNodeById(comp.getId()), intention))
            else:
                try:
                    node = profile.getNodeById(profile.getIdByName(name_node))
                    objs.append(Objectif(profile, node, intention))
                except NodeObjectError:
                    raise NodeObjectError(
                        name_node, "can't find a node with this name")

    if max_objectives != 0 and len(objs) > max_objectives:
        objs = objs[:max_objectives]

    if objs == []:
        raise ObjectiveError(objs, "Empty objectives")

    return objs


def loadingStrategy(STRATEGIES, strategy_name, defaultSP, directorySP, SCHEMA_PS_FILE):

    strategy_file = strategy_name + ".json"
    logger.info("Loading %s verify %s", strategy_file, SCHEMA_PS_FILE)

    # recuperation et validation de la strategie
    fileSP = directorySP + strategy_file
    strategy, strategy_grammar = ps.loadStrategy(
        directorySP + strategy_file, SCHEMA_PS_FILE)

    dateActuel = datetime.datetime.now()
    lastDateModif = datetime.datetime.fromtimestamp(os.path.getmtime(fileSP))

    if strategy_name not in list(STRATEGIES.keys()) or STRATEGIES[
            strategy_name]["dateLoading"] < lastDateModif:
        # we set the list of intentions as a class attribute for objectives
        list_of_intentions = strategy_grammar[
            "definitions"]["intention"]["enum"]
        Objectif.INTENTION_LIST = list_of_intentions

        ps.validationStrategySyntax(strategy, strategy_grammar)

        # creation des objets
        strategy_objects, id_strategy = ps.importStrategy(strategy)

        # verification et mise a jour des liens entre objets
        ps.verifyComponentsIntegrity(strategy_objects)
        ps.insertingComponents(strategy_objects)

        # ajout à la liste des SP
        # si la SP n'a pas été chargée
        if id_strategy not in STRATEGIES.keys():
            logger.info("Loading SP %s for the 1st time", id_strategy)
            STRATEGIES[id_strategy] = {"objects": dict(strategy_objects),
                                       "idSPobject": id_strategy,
                                       "dateLoading": dateActuel,
                                       "file": fileSP
                                       }
        else:
            # si la SP a été modifiée entre temps
            if STRATEGIES[id_strategy]["dateLoading"] < lastDateModif:
                logger.info("Reloading SP %s --> changed", id_strategy)
                STRATEGIES[id_strategy] = {"objects": dict(strategy_objects),
                                           "idSPobject": id_strategy,
                                           "dateLoading": dateActuel,
                                           "file": fileSP
                                           }
        logger.info("Loading done\n")
        if defaultSP:
            return STRATEGIES, id_strategy
        else:
            return STRATEGIES, id_strategy
    else:
        logger.warning("Didn't need to reload SP")
        return STRATEGIES, strategy_name


def initStrategy(STRATEGIES, strategy_name, directorySP=DATA_PATH + "PS/", SCHEMA_PS_FILE=SCHEMA_PS_FILE):
    strategy, id_strategy = loadingStrategy(STRATEGIES, strategy_name, True, directorySP, SCHEMA_PS_FILE)
    return strategy, id_strategy


def loadStrategy(STRATEGIES, strategy_name, directorySP=DATA_PATH + "PS/", SCHEMA_PS_FILE=SCHEMA_PS_FILE):
    strategy, id_strategy = loadingStrategy(STRATEGIES, strategy_name, False, directorySP, SCHEMA_PS_FILE)
    return strategy


def getRecommendation(referential, profile, liste_objectifs,
                      strategy_objects, id_strategy):
    reco = applyStrategy(strategy_objects, id_strategy,
                         referential, profile, liste_objectifs)
    return reco


def completeLogConsultation(additional_info: dict, filename: str):
    consultation_data = []
    logConsulFile = f"{DATA_PATH}{filename}"

    if not os.path.isfile(logConsulFile):
        with open(logConsulFile, 'w', encoding='utf-8') as f:
            consultation_data.append(additional_info)
            json.dump(consultation_data, f, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False)
            logger.debug(f"{logConsulFile} creation")
    else:
        with open(logConsulFile, 'r+', encoding='utf-8') as f:
            consultation_data = json.load(f)
            logger.debug(f"Open {logConsulFile}")
            consultation_data.append(additional_info)
            if len(consultation_data) > 10:
                consultation_data = consultation_data[-10:]
            f.seek(0)
            json.dump(consultation_data, f, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False)
            f.truncate()
            logger.debug(f"Writing {logConsulFile}")
