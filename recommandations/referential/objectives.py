#!/usr/bin/python3
# -*- coding: utf-8 -*-

from recommandations.referential import const, errors
from recommandations.referential.referential import Node


class Objectif:
    INTENTION_LIST = []

    def __init__(self, profile, node, intention):
        INTENTION_LIST = Objectif.INTENTION_LIST

        if not Node.isANode(node):
            raise errors.ObjectiveError(node, "node is not a Node")

        if not profile.nodeIdExist(node.getId()):
            raise errors.ObjectiveError(node, "node doesn't exist in referential")
        self.node = node

        if intention not in INTENTION_LIST:
            raise errors.ObjectiveError(
                intention, "Unknown intention. Allowed intention are :" + str(const.INTENTION_LIST))

        self.intention = intention

        self.path = []

    def setIntention(self, intention):
        if intention not in const.INTENTION_LIST:
            raise errors.ObjectiveError(
                intention, "Unknown intention. Allowed intention are :" + str(const.INTENTION_LIST))
        self.intention = intention

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "Objectif <Node#" + str(self.node.getId()) + ", Intention#" + self.intention + ">"

    def getNode(self):
        return self.node

    def getIntention(self):
        return self.intention

    def getPath(self):
        return self.path

    def addPath(self, path):
        self.path.extend(path)

    def setPath(self, path):
        self.path = list(path)
