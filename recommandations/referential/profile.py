#!/usr/bin/python3
# -*- coding: utf-8 -*-

import copy
import pprint
import random

import graphviz
import numpy

from recommandations.referential import errors
from recommandations.referential.referential import (Node, Referential,
                                                     ResourceNode)


class ProfileNode(Node):
    def __init__(self, id_n, name, type_n, values=(0, 0, 0)):

        super().__init__(id_n, name, type_n)

        self.values = values
        self.state = "OK"

        self.weight = 0

    def resetWeight(self):

        self.weight = 0
        if "int" not in str(type(self.weight)) and "float" not in str(type(self.weight)):
            raise TypeError("", "weight of profileNode " + str(self.getId()) + " is not a number")

    def setWeight(self, weight):

        self.weight = weight
        if "int" not in str(type(self.weight)) and "float" not in str(type(self.weight)):
            raise TypeError("", "weight of profileNode " + str(self.getId()) + " is not a number")

    def getWeight(self):

        if "int" not in str(type(self.weight)) and "float" not in str(type(self.weight)):
            raise TypeError("", "weight of profileNode " + str(self.getId()) + " is not a number")

        return self.weight

    def setData(self, values):

        self.values = values
        self.state = "OK"

    def getData(self):

        return self.values

    def isAProfileNodeObject(obj):

        if "." not in str(type(obj)):  # not an object
            return False

        for c in obj.__class__.mro():
            if "ProfileNode" in str(c):
                return True

        return False

    def addLink(self, dest, nameRel):

        if nameRel not in ["hasTraining", "hasLearning"]:
            if not ProfileNode.isAProfileNodeObject(dest):
                raise errors.NodeObjectError(dest, "dest is not a profile node")

        if nameRel not in self.rel:
            if dest in self.rel:
                raise errors.NodeObjectError(
                    dest, "relation (" + nameRel + "," + self.id_n + "," + Node.getId() + " already exist")
            self.rel[nameRel] = [dest]
        else:
            self.rel[nameRel].append(dest)

    def getMaitrise(self):

        if self.state != "OK":
            raise errors.NodeProfileObjectError(
                self, "NodeProfile " + self.getId() + " empty node --> use setData() method")
        return float(self.values[0])

    def getConfiance(self):

        if self.state != "OK":
            raise errors.NodeProfileObjectError(
                self, "NodeProfile " + self.getId() + " empty node --> use setData() method")
        return float(self.values[1])

    def getCouverture(self):

        if self.state != "OK":
            raise errors.NodeProfileObjectError(
                self, "NodeProfile " + self.getId() + " empty node --> use setData() method")
        return float(self.values[2])

    def __str__(self):
        return "ProfileNode id#" + str(self.getId())

    def __repr__(self):
        return "ProfileNode id#" + str(self.getId())

    def fullprint(self):

        dico = self.__dict__.copy()

        dico["rel"] = {rel: [n.getId() for n in nodes]
                       for rel, nodes in self.rel.items()}
        return "ProfileNode " + str(self.values) + "" + pprint.pformat((self.__class__.mro()[0], dico), indent=2)


class ResourceProfileNode(ProfileNode, ResourceNode):
    def __init__(self, dico):
        node = ProfileNode(dico["id_n"], dico["name"], "Resource")
        dico.update(node.__dict__)
        for k, v in dico.items():
            if isinstance(v, dict):
                self.__dict__[k] = v.copy()
            else:
                self.__dict__[k] = v

    def __str__(self):
        return "ResourceProfileNode id#" + str(self.getId())

    def __repr__(self):
        return "ResourceProfileNode id#" + str(self.getId())


class Profil(Referential):
    # triplet_nodes_byId : {"id": (maitrise, confiance, couverture)}
    def __init__(self, referential, triplet_nodes_byId):
        referentiel = copy.deepcopy(referential)

        self.invs_rel = referential.getInvsRels()
        self.nodes = {}

        for id_n, node in referentiel.getNodes().items():
            if id_n not in triplet_nodes_byId and node.getTypeN() not in ['Framework', 'Resource']:
                print(node.getName())
                raise errors.NodeProfileObjectError(
                    id_n, "can't find triplet of values for id_n : " + str(id_n))

            if node.getTypeN() != "Resource":
                self.nodes[id_n] = ProfileNode(
                    node.getId(), node.getName(), node.getTypeN())
            else:
                self.nodes[id_n] = ResourceProfileNode(
                    copy.deepcopy(node.__dict__))

            if node.getTypeN() not in ['Framework', 'Resource']:
                self.nodes[id_n].setData(triplet_nodes_byId[id_n])

        self.id_by_name = referentiel.id_by_name

        # maj rel ==> Nodes en ProfilNodes
        for id_n, node in referentiel.getNodes().items():
            for name_rel, nodes in node.getLinks().items():
                for n2 in nodes:
                    self.nodes[id_n].addLink(self.nodes[n2.getId()], name_rel)

        self.racine = self.nodes[referentiel.getRacine().getId()]

    def getNodes(self):
        return self.nodes

    def __str__(self):
        return pprint.pformat([(n.getId(), n.getName(), n.getData()) for k, n in self.nodes.items()])

    def __repr__(self):
        return str(self)

    def resetWeights(self):
        for idn, n in self.nodes.items():
            n.resetWeight()

    def getRacine(self):
        if self.racine is None:
            raise errors.NodeObjectError(self.racine, "racine is not defined")
        return self.racine

    def nodeIdExist(self, id_n):
        return id_n in self.nodes.keys()

    def getNodeById(self, id_n):
        if not self.nodeIdExist(id_n):
            raise errors.NodeObjectError(id_n, "node with id " + str(id_n) + " doesn't exist")
        return self.nodes[id_n]

    def getIdByName(self, name):
        if name not in self.id_by_name.keys():
            return -1
        else:
            return self.id_by_name[name]

    def getGraphviz(self, edges=True, list_relations=["comprises", "hasKnowledge", "hasSkill", "isComposedOf", "requires", "isUnderstoodBy", "isComplexifiedBy"]):
        dot = graphviz.Digraph(format='png')
        COLOR = {"Framework": "lightgrey", "Competency": "gold",
                 "Knowledge": "mediumpurple", "Skill": "deepskyblue", "Resource": "orange"}
        for id_n, node in self.nodes.items():
            c = COLOR[node.getTypeN()]
            if "ResourceProfileNode" not in str(node):
                dot.node(str(id_n), label=str(node.getName()) + str(node.getData()), style="filled", color=str(c))
                # dot.node(str(id_n))
        if edges:
            for id_n, node in self.nodes.items():
                for name_rel, nodes in node.getLinks().items():
                    if name_rel in list_relations:
                        for node in nodes:
                            if name_rel in ["requires", "isRequiredBy"]:
                                dot.edge(str(id_n), str(node.getId()), label=str(
                                    name_rel), color="blue", penwidth="4")
                            elif name_rel in ["isComplexifiedBy", "complexifies"]:
                                dot.edge(str(id_n), str(node.getId()), label=str(
                                    name_rel), color="orange", penwidth="4")
                            elif name_rel in ["isLeverOfUnderstandingOf", "isUnderstoodBy"]:
                                dot.edge(str(id_n), str(node.getId()), label=str(
                                    name_rel), color="green", penwidth="4")
                            else:
                                dot.edge(str(id_n), str(node.getId()),
                                         label=str(name_rel))

        return dot

    def resetData(self):
        for id_n in self.nodes.keys():
            self.nodes[id_n].setData([0.0, 0.0, 0.0])

    def buildRandomFromObjectiveInDescendants(self,
                                              nodeObj,
                                              relationsToFollow=[
                                                  "isComposedOf", "hasKnowledge", "hasSkill"],
                                              initFeuille={"nonMaitrise": True,  # has nonMaitrise if yes 1/nb(predicat with yes) of nodes wil be in that predicates\
                                                           "peuMaitrise": True,  # has peuMaitrise if yes 1/nb(predicat with yes) of nodes wil be in that predicates\
                                                           "partiellementMaitrise": True,  # has partiellementMaitrise if yes 1/nb(predicat with yes) of nodes wil be in that predicates\
                                                           "maitrise": True,  # has maitrise if yes 1/nb(predicat with yes) of nodes wil be in that predicates\
                                                           "maitriseInconnue": 0.0},  # percentage of nodes with tust = 0 \
                                              seuilsPredicates={"nonMaitrise": [0, 0.24], \
                                                                "peuMaitrise": [0.25, 0.49], \
                                                                "partiellementMaitrise": [0.5, 0.74], \
                                                                "maitrise": [0.75, 1.0]
                                                                }\
                                              ):
        # NOTE // if predicate is apply trust will be between 0.3 et 0.9

        predicatesNamesToApply = []
        nbSelectedPredicate = 0
        if initFeuille["nonMaitrise"]:
            predicatesNamesToApply.append("nonMaitrise")
            nbSelectedPredicate += 1
        if initFeuille["peuMaitrise"]:
            predicatesNamesToApply.append("peuMaitrise")
            nbSelectedPredicate += 1
        if initFeuille["partiellementMaitrise"]:
            predicatesNamesToApply.append("partiellementMaitrise")
            nbSelectedPredicate += 1
        if initFeuille["maitrise"]:
            predicatesNamesToApply.append("maitrise")
            nbSelectedPredicate += 1

        descendants = {0: [nodeObj]}
        feuilles = []

        depth = 0
        index_in_depth = 0
        ended = False

        # we get all the descendants from the objective
        while not ended:
            # treatment of the nodes
            current_node = descendants[depth][index_in_depth]
            if not current_node.isFeuille():
                for r in relationsToFollow:
                    print("From", current_node.getName(), "follow",
                          r,
                          [n.getName() for n in current_node.getDescendants(r)])
                    for descendant in current_node.getDescendants(r):
                        depth1 = depth + 1
                        if depth1 in descendants.keys():
                            # we already have descendants at this level
                            descendants[depth1].append(descendant)
                        else:
                            # we create a new level
                            descendants[depth1] = [descendant]
                        if descendant.isFeuille():
                            feuilles.append(descendant)

            # we increased the indexes
            if index_in_depth < len(descendants[depth]) - 1:
                # treatment of depth-th descendants
                index_in_depth += 1
            else:
                # we go down in the tree
                if depth + 1 in descendants.keys():
                    # we have descendants at level +1
                    index_in_depth = 0
                    depth += 1
                else:
                    # we finish to follow all descendants
                    ended = True

        pprint.pprint([node.getName() for node in feuilles])

        # now that we have the descendants and leaves we can put the mastery levels and next propagate
        for i in range(len(feuilles)):

            nonMaitriseValue = random.randint(
                seuilsPredicates["nonMaitrise"][0] * 100, seuilsPredicates["nonMaitrise"][1] * 100) / 100  # nonMaitrise
            peuMaitriseValue = random.randint(
                seuilsPredicates["peuMaitrise"][0] * 100, seuilsPredicates["peuMaitrise"][1] * 100) / 100  # peuMaitrise
            partiellementMaitriseValue = random.randint(
                seuilsPredicates["partiellementMaitrise"][0] * 100, seuilsPredicates["partiellementMaitrise"][1] * 100) / 100  # partiellementMaitrise
            maitriseRandomValue = random.randint(
                seuilsPredicates["maitrise"][0] * 100, seuilsPredicates["maitrise"][1] * 100) / 100  # maitrise

            randomValues = {"nonMaitrise": nonMaitriseValue,
                            "peuMaitrise": peuMaitriseValue,
                            "partiellementMaitrise": partiellementMaitriseValue,
                            "maitrise": maitriseRandomValue}

            numPredicateToApply = i % nbSelectedPredicate
            # cover = 1 if mastery known
            feuilles[i].setData(
                [randomValues[predicatesNamesToApply[numPredicateToApply]], random.randint(30, 90) / 100, 1])

        nb_nodes_unknown = int(initFeuille["maitriseInconnue"] * len(feuilles))
        # we shuffle the leaves
        random.shuffle(feuilles)
        # we set mastery unknown
        for i in range(nb_nodes_unknown):
            # cover = 0 if mastery unknown
            feuilles[i].setData([0, 0, 0])

        # next we need to propagate mastery, trust and cover from bottom to objective
        # mastery : mean of child mastery if != 0
        # trust : mean of child trust
        # cover : number of child != 0 / number of child
        for depth in reversed(list(descendants.keys())):
            for node in descendants[depth]:
                if not node.isFeuille():
                    mastery_sons = []
                    trust_sons = []
                    cover_sons = []

                    for relation in relationsToFollow:
                        for target in node.getDescendants(relation):
                            mastery_target, trust_target, cover_target = target.getData()
                            mastery_sons.append(mastery_target)
                            trust_sons.append(trust_target)
                            cover_sons.append(cover_target)

                    if len(trust_sons) > 0:

                        mastery_son_diff_0 = [
                            m for m in mastery_sons if m != 0]
                        if len(mastery_son_diff_0) > 0:
                            mastery_calculate = numpy.mean(mastery_son_diff_0)
                        else:
                            mastery_calculate = 0.0
                        trust_calculate = numpy.mean(trust_sons)
                        # cover_calculate = len([m for m in mastery_sons if m != 0]) / len(mastery_sons)
                        cover_calculate = numpy.mean(cover_sons)

                        # we set the new data we calculate for the node
                        node.setData(
                            [mastery_calculate, trust_calculate, cover_calculate])
