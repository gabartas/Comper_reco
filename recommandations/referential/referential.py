#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pprint

import graphviz

from recommandations.referential import errors

from .const import TYPE_NODE_LIST


def referentiel_relations_inv_duplicate(inv_rel):
    new_dict = inv_rel.copy()
    for k, v in inv_rel.items():
        new_dict[v] = k

    return new_dict


def verify_isString(obj, nameerror=""):
    if str(type(obj)) != "<class 'str'>":
        raise errors.PropertyObjectError(obj, nameerror + " must be a string not " + str(type(obj)) + " (" + str(obj) + ")")


def verify_typen(type_n):
    verify_isString(type_n, "type_n")

    if type_n not in TYPE_NODE_LIST:
        raise errors.NodeObjectError(type_n, "unknown node type " + type_n + ". Allowed type are " + str(TYPE_NODE_LIST))


class Node:
    def __init__(self, id_n, name, type_n):
        self.id_n = id_n

        verify_isString(name, "name")
        self.name = name

        verify_typen(type_n)
        self.type = type_n

        self.rel = {}

    def __str__(self):
        dico = self.__dict__.copy()

        dico["rel"] = {rel: [n.getId() for n in nodes]
                       for rel, nodes in self.rel.items()}
        return "Node " + pprint.pformat((self.__class__.mro()[0], dico), indent=2)

    def __repr__(self):
        return str(self)

    def getId(self):
        return self.id_n

    def getName(self):
        return self.name

    def getTypeN(self):
        return self.type

    def isANode(obj):
        if "." not in str(type(obj)):  # not an object
            return False

        for c in obj.__class__.mro():
            if "Node" in str(c):
                return True

        return False

    def addLink(self, dest, nameRel):
        if not Node.isANode(dest):
            raise errors.NodeObjectError(dest, "dest is not a node")

        if nameRel not in self.rel:
            if dest in self.rel:
                raise errors.NodeObjectError(dest, "relation (" + nameRel + "," + self.id_n + "," + Node.getId() + " already exist")
            self.rel[nameRel] = [dest]
        else:
            self.rel[nameRel].append(dest)

    def hasLink(self, nameRel):
        return nameRel in self.rel

    def getLinks(self):
        return self.rel

    def getDescendants(self, relation):
        # print({"id": self.getId(), "rel": relation, "rels": self.rel})
        if relation not in list(self.rel.keys()):
            return []
        else:
            return self.rel[relation]

    def relationWithNode(self, node):
        if not Node.isANode(node):
            raise errors.NodeObjectError(node, "node is not a node")

        rels = []
        for r, nodes in self.rel.items():
            for n in nodes:
                if n.getId() == node.getId():
                    rels.append(r)

        return rels

    def nbRessourcesTraining(self):
        return len(self.rel["hasTraining"]) if "hasTraining" in self.rel.keys() else 0

    def nbRessourcesLearning(self):
        return len(self.rel["hasLearning"]) if "hasLearning" in self.rel.keys() else 0

    def nbRessources(self):
        return self.nbRessourcesTraining() + self.nbRessourcesLearning()

    def hasRessourcesTraining(self):
        return self.nbRessourcesTraining() > 0

    def hasRessourcesLearning(self):
        return self.nbRessourcesLearning() > 0

    def hasRessources(self):
        return self.nbRessources() > 0

    def isFeuille(self):
        return all([k not in self.rel.keys() for k in ["isComposedOf", "hasKnowledge", "hasSkill"]])


class ResourceNode(Node):
    def __init__(self, id_n, name, interactivityType, learningResourceType, significanceLevel, difficulty, typicalLearningTime, learningPlatform, location, author, language, generative):

        super().__init__(id_n, name, "Resource")

        self.interactivityType = interactivityType
        self.learningResourceType = learningResourceType
        self.significanceLevel = significanceLevel
        self.difficulty = difficulty
        self.typicalLearningTime = typicalLearningTime
        self.learningPlatform = learningPlatform
        self.location = location
        self.author = author
        self.language = language
        self.generative = generative

    def getMetadata(self):
        return {"interactivityType": self.interactivityType,
                "learningResourceType": self.learningResourceType,
                "significanceLevel": self.significanceLevel,
                "difficulty": self.difficulty,
                "typicalLearningTime": self.typicalLearningTime,
                "learningPlatform": self.learningPlatform,
                "location": self.location,
                "author": self.author,
                "language": self.language,
                "generative": self.generative}

    def getMetaDataValue(self, name):
        return self.__dict__[name]

    def getInteractivityType(self):
        return self.interactivityType

    def getLearningResourceType(self):
        return self.learningResourceType

    def getSignificanceLevel(self):
        return self.significanceLevel

    def getDifficulty(self):
        return self.difficulty

    def getTypicalLearningTime(self):
        return self.typicalLearningTime

    def getLearningPlatform(self):
        return self.learningPlatform

    def getLocation(self):
        return self.location

    def getAuthor(self):
        return self.author

    def getLanguage(self):
        return self.language

    def isGenerative(self):
        return self.generative == "true"


class Referential:
    # relation_invs = {"rel" : "inv-rel", "inv-rel": "rel", ...}
    def __init__(self, name, relation_invs):
        verify_isString(name, "name")
        self.name = name

        self.nodes = {}
        self.id_by_name = {}
        self.racine = None

        self.invs_rel = relation_invs

    def getInvsRels(self):
        return self.invs_rel

    def __str__(self):
        return pprint.pformat((self.__class__.mro()[0], self.__dict__))

    def __repr__(self):
        return str(self)

    def getIdByName(self, name):
        if name not in self.id_by_name.keys():
            return -1
        else:
            return self.id_by_name[str(name)]

    def getNodes(self):
        return self.nodes

    def getRacine(self):
        if self.racine is None:
            raise errors.NodeObjectError(self.racine, "racine is not defined")
        return self.racine

    def setRacine(self, id_n):
        if not self.nodeIdExist(id_n):
            raise errors.NodeObjectError(id_n, "node with id:" + str(id_n) + " don't exist")
        self.racine = self.getNodeById(id_n)

    def nodeIdExist(self, id_n):
        return id_n in self.nodes.keys()

    def getNodeById(self, id_n):
        if not self.nodeIdExist(id_n):
            raise errors.NodeObjectError(id_n, "node with id " + str(id_n) + " doesn't exist")
        return self.nodes[id_n]

    def getNodesIds(self):
        return self.nodes.keys()

    def getFeuilleIds(self):
        return [id_n for id_n, n in self.nodes.items() if n.isFeuille()]

    def add_node(self, node):
        if not Node.isANode(node):
            raise errors.NodeObjectError(node, "node is not a node")

        if self.nodeIdExist(node.getId()):
            raise errors.NodeObjectError(node, "node with id:" + str(node.getId()) + " already exist")

        self.nodes[node.getId()] = node
        self.id_by_name[node.getName()] = node.getId()

    def add_link(self, id_src, id_dest, nameRel):
        if not self.nodeIdExist(id_src):
            raise errors.NodeObjectError(id_src, "node with id:" + str(id_src) + " don't exist")
        if not self.nodeIdExist(id_dest):
            raise errors.NodeObjectError(id_dest, "node with id:" + str(id_dest) + " don't exist")

        self.nodes[id_src].addLink(self.getNodeById(id_dest), nameRel)

        # ajout de la relation inverse
        # self.nodes[id_dest].addLink(self.getNodeById(id_src), self.invs_rel[nameRel])

    def getGraphviz(self, relation_a_afficher=[]):
        dot = graphviz.Digraph(format='png')
        COLOR = {"Framework": "lightgrey", "Competency": "mediumslateblue",
                 "Knowledge": "palegreen2", "Skill": "lightgoldenrod1", "Resource": "orange"}
        for id_n, node in self.nodes.items():
            c = COLOR[node.getTypeN()]
            if node.getTypeN() == "Resource":
                dot.node(str(id_n).replace(":", "_"), label=str(id_n) + ", " + str(node.getName()), style="filled", color=str(c))
            else:
                dot.node(str(id_n), label=str(id_n) + ", " + str(node.getName()), style="filled", color=str(c))
            # dot.node(str(id_n))
        for id_n, node in self.nodes.items():
            for name_rel, nodes in node.getLinks().items():
                if name_rel in self.invs_rel.keys():
                    for node in nodes:
                        if relation_a_afficher == [] or name_rel in relation_a_afficher:
                            dot.edge(str(id_n).replace(":", "_"), str(
                                node.getId()).replace(":", "_"), label=str(name_rel))

        dot.graph_attr['rankdir'] = 'LR'

        return dot

    def isAReferentialObject(obj):
        if "." not in str(type(obj)):  # not an referentiel
            return False

        for c in obj.__class__.mro():
            if "Referential" in str(c):
                return True

        return False
