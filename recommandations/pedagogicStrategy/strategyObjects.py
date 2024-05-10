#!/usr/bin/python3
# -*- coding: utf-8 -*-

import datetime
import os
import sys  # for importation of ../modules
from pprint import pformat

from ..referential.referential import Node
from . import errors
from .const import CLASS_OBJECT_LIST


sys.path.append("..")


def verify_isString(obj, nameerror=""):
    if str(type(obj)) != "<class 'str'>":
        raise errors.PropertyObjectError(obj, f"{nameerror} must be a string not {type(obj)} ( {obj} )")

# definition des classes des objets à manipuler


def verify_id(id_o):
    verify_isString(id_o, "id")
    if id_o == "":
        raise errors.PropertyObjectError(id_o, "Id must be not empty")


def verify_class(class_o):
    if class_o not in CLASS_OBJECT_LIST:
        raise errors.PropertyObjectError(class_o, f"class must be in {CLASS_OBJECT_LIST}")


class ManipulableObject:
    def __init__(self, id_o, name_o, descr_o, type_o, class_o):
        verify_id(id_o)
        self.id_o = id_o
        self.name_o = name_o
        self.descr_o = descr_o
        self.type_o = type_o
        verify_class(class_o)
        self.class_o = class_o

    def isAManipulableObject(obj):
        return issubclass(obj.__class__, ManipulableObject)

    def getId(self):
        return self.id_o

    def getName(self):
        return self.name_o

    def getClass(self):
        return self.class_o

    def getType(self):
        return self.type_o

    def getDescr(self):
        return self.descr_o

    def __repr__(self):
        return str(self)

    def __str__(self):
        return str(self.__dict__)


class ComponentObject(ManipulableObject):
    def __init__(self, id_o, name_o, descr_o, type_o, class_o, components):
        super().__init__(id_o, name_o, descr_o, type_o, class_o)
        self.components = components.copy()
        self.update = False

    def isAComponentObject(obj):
        return issubclass(obj.__class__, ComponentObject)

    def getComponentsList(self):
        return [compo for compo in self.components if "str" in str(type(compo))]

    def canUpdateComponents(self, componentsDict):
        return all([componentsDict[compo].update for compo in self.getComponentsList() if ComponentObject.isAComponentObject(componentsDict[compo])])

    def listMissingComponents(self, componentsDict):
        return [compo for compo in self.getComponentsList() if compo not in componentsDict.keys()]

    def updateComponents(self, componentsDict):
        if not self.canUpdateComponents(componentsDict):
            raise errors.ComponentMissingError(f"Object id : {self.getId()}, missing : {self.listMissingComponents(componentsDict)}")


class PedagogicStrategy(ComponentObject):
    def __init__(self, id_o, name_o, descr_o, type_o, class_o, components, objective_parameters, selection_parameters, ordonnancement_parameters, resources_parameters):
        super().__init__(id_o, name_o, descr_o, type_o, class_o, components)
        self.objective_parameters = objective_parameters
        self.objective_parameters["maxObjectives"] = int(
            self.objective_parameters["maxObjectives"])

        self.selection_parameters = selection_parameters

        self.selection_parameters["alpha"] = float(
            self.selection_parameters["alpha"])
        self.selection_parameters["weightInitObjectif"] = float(
            self.selection_parameters["weightInitObjectif"])

        for k in self.selection_parameters["weight_r"].keys():
            for k2 in self.selection_parameters["weight_r"][k].keys():
                # use +1 to be usable by the algorithm ([-1, 1] -> [0, 2])
                self.selection_parameters["weight_r"][k][k2] = float(
                    self.selection_parameters["weight_r"][k][k2]) + 1.0

        self.ordonnancement_parameters = ordonnancement_parameters

        for k in self.ordonnancement_parameters["prioTags"].keys():
            for k2 in self.ordonnancement_parameters["prioTags"][k].keys():
                self.ordonnancement_parameters["prioTags"][k][k2] = int(
                    self.ordonnancement_parameters["prioTags"][k][k2])

        self.resources_parameters = resources_parameters

    def isAPedagogicStrategy(obj):
        return issubclass(obj.__class__, PedagogicStrategy)

    def updateComponents(self, componentsDict):
        super().updateComponents(componentsDict)
        if not self.update:
            for i in range(len(self.selection_parameters["selection_procedures"])):
                if "str" in str(type(self.selection_parameters["selection_procedures"][i])):
                    # print("[Update]", self.getId(), "selection rule", self.reglesSelection[i])
                    self.selection_parameters["selection_procedures"][i] = componentsDict[
                        self.selection_parameters["selection_procedures"][i]]
            self.update = True

    def getObjectiveParameters(self):
        return self.objective_parameters

    def getWeightObjective(self):
        return self.selection_parameters["weightInitObjectif"]

    def getKSCSelectionProcedures(self):
        return self.selection_parameters["selection_procedures"]

    def getAlpha(self):
        return self.selection_parameters["alpha"]

    def getWeightR(self):
        return self.selection_parameters["weight_r"]

    def getPrioTags(self):
        return self.ordonnancement_parameters["prioTags"]

    def getResourcesParameters(self):
        return self.resources_parameters

    def __str__(self):
        return f"PedagogicStrategy # {self.getId()}: {self.getName()} \nType:  {self.getType()} \nDescription : {self.getDescr()}\n\n\tweightInitObjectif= {self.getWeightObjective()}\n\tKSCselectionProcedures= {[(ps if isinstance(ps, None) else ps.getId()) for ps in self.getKSCSelectionProcedures()]} \n\tPriotags{pformat(self.getPrioTags(), indent=8)}"

    def __repr__(self):
        return str(self)


class SelectionProcedure(ComponentObject):
    def __init__(self, id_o, name_o, descr_o, type_o, class_o, components, content):
        super().__init__(id_o, name_o, descr_o, type_o, class_o, components)
        self.intentions = Intentions(content["intentions"])

        self.initialisation_parameters = content["initialisation_parameters"]
        self.pre_traitement_parameters = content["pretreatement_parameters"]
        self.traitement_parameters = content["treatment_parameters"]

    def updateComponents(self, componentsDict):
        super().updateComponents(componentsDict)
        if not self.update:

            if "str" in str(type(self.pre_traitement_parameters["condition_selection"])) and self.pre_traitement_parameters["condition_selection"] != "":
                if self.pre_traitement_parameters["condition_selection"] == "maitrise":
                    self.pre_traitement_parameters["condition_selection"] = componentsDict[f"p_{self.pre_traitement_parameters['condition_selection']}d"]
                    print("-----------------CORRECTION CLE FAITE----------------------")
                else:
                    self.pre_traitement_parameters["condition_selection"] = componentsDict[
                        self.pre_traitement_parameters["condition_selection"]]

            for i in range(len(self.traitement_parameters["selection_rules"])):
                if "str" in str(type(self.traitement_parameters["selection_rules"][i])):
                    self.traitement_parameters["selection_rules"][i] = componentsDict[
                        self.traitement_parameters["selection_rules"][i]]
            self.update = True

    def getIntentions(self):
        return self.intentions

    def getInitialisation(self):
        return self.initialisation_parameters

    def getPreTraitementParam(self):
        return self.pre_traitement_parameters

    def getTraitementParam(self):
        return self.traitement_parameters

    def isASelectionProcedure(obj):
        return issubclass(obj.__class__, SelectionProcedure)

    def __str__(self):
        return f"SelectionProcedure #{self.getId()} : {self.getName()}\n Type: {self.getType()}\nDescription : {self.getDescr()}\n\n\tintentions= {self.getIntentions()} \n\tinitialisation_parameters= {pformat(self.initialisation_parameters, indent=16)}\n\tpretraitement_parameters=\n {pformat(self.pre_traitement_parameters, indent=16)}\n\ttraitement_parameters=\n{pformat(self.traitement_parameters, indent=16)}\n"

    def __repr__(self):
        return str(self)


class Intentions():
    def __init__(self, intentions):
        self.intentions = intentions.copy()

    def evaluate(self, intention):
        return intention in self.intentions

    def __str__(self):
        return f"Intention in {self.intentions}"

    def __repr__(self):
        return str(self)


class SelectionRule(ComponentObject):
    def __init__(self, id_o, name_o, descr_o, type_o, class_o, components, content):
        super().__init__(id_o, name_o, descr_o, type_o, class_o, components)
        self.selection_condition_predicate = content["selection_condition"]
        self.selection_condition = content["selection_condition"]
        self.selection_parameters = content["selection_parameters"]
        self.recursion_parameters = content["recursion_parameters"]

    def updateComponents(self, componentsDict):
        super().updateComponents(componentsDict)
        if not self.update:
            if isinstance(self.selection_condition, type("")):
                # print("[Update]", self.getId(), "condition_traitement")
                self.selection_condition = componentsDict[self.selection_condition]
            self.update = True

    def getCondition(self):
        return self.selection_condition

    def getSelectionParameters(self):
        return self.selection_parameters

    def getRecursionParameters(self):
        return self.recursion_parameters

    def __str__(self):
        return f"SelectionRule #{self.getId()} : {self.getName()}\n Type: {self.getType()}\nDescription : {self.getDescr()}\n\n\tselection_condition={self.getCondition()}\n\tselection_parameters={pformat(self.getSelectionParameters(), indent=16)}\n\trecursion_parameters=\n{pformat(self.getRecursionParameters(), indent=16)}\n"

    def __repr__(self):
        return str(self)


class Predicate(ComponentObject):
    def __init__(self, id_o, name_o, descr_o, type_o, class_o, formula, components):
        super().__init__(id_o, name_o, descr_o, type_o, class_o, components)
        self.formula = formula
        self.baseformula = formula

    def isAPredicate(obj):
        return issubclass(obj.__class__, Predicate)

    def getFormula(self):
        return self.formula

    def updateComponents(self, componentsDict):
        super().updateComponents(componentsDict)
        if not self.update:
            for id_compo in self.getComponentsList():
                # print("[Update]", self.getId(), "formula with ", id_compo)
                if "str" in str(type(id_compo)):
                    if Predicate.isAPredicate(componentsDict[id_compo]):
                        self.formula = self.formula.replace(
                            id_compo, componentsDict[id_compo].getFormula())
                    elif str(type(componentsDict[id_compo])) in ["<class 'int'>", "<class 'float'>"]:
                        # constante
                        self.formula = self.formula.replace(
                            id_compo, str(componentsDict[id_compo]))
                    else:
                        raise errors.ComponentTypeError(id_compo, f"{self.getId()} type of component {id_compo} is not a predicate or a parameter {type(componentsDict[id_compo])}")
            self.update = True

    def compil(self):
        self.formula = f"({self.formula})"
        # devra etre parenthesée au max à l'init dans le fichier
        for left, right in (("", ""), (" = ", " == ")):
            self.formula = self.formula.replace(left, right)

    def evaluate(self, node: Node, details=False):
        formula = str(self.formula)

        # on remplace les données
        formula = formula.replace("maitrise_noeud", str(node.getMaitrise()))
        formula = formula.replace("confiance_noeud", str(node.getConfiance()))
        formula = formula.replace("couverture_noeud", str(node.getCouverture()))

        evalFormula = eval(formula)

        if details:
            return (evalFormula, formula, self.formula)
        else:
            return evalFormula

    def __str__(self):
        return str(self.formula)

    def __repr__(self):
        return str(self)


class StrategyDescription:
    def __init__(self, SPfile, id_sp, name, description, authors, version, type_sp, public_visibility):
        self.SPfile = SPfile
        self.id = id_sp
        self.name = name
        self.authors = authors
        self.description = description
        self.version = version
        self.type = type_sp
        self.public_visibility = public_visibility

    def getListAuthors(self):
        return ", ".join([author for author in self.authors])

    def getLastModification(self):
        return datetime.datetime.fromtimestamp(os.path.getmtime(self.SPfile)).strftime("%Y-%m-%d %H:%M:%S")

    def __repr__(self):
        return str(self)

    def __str__(self):
        return str(self.__dict__)

# function to get all the predicates from a list of objects:


def getPredicates(objectsStrategy):
    return {o.getId(): o for o in objectsStrategy if Predicate.isAPredicate(o)}
