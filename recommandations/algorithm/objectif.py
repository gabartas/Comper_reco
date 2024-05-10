#!/usr/bin/python3
# -*- coding: utf-8 -*-

from . import logs


def setWeightObjectifs(objectifs, objective_weight_value, f_log):
    for i in range(len(objectifs)):
        weight = objective_weight_value
        objectifs[i].getNode().setWeight(weight)

        contentObjective = {"num": i,
                            "node": (objectifs[i].getNode().getId(), objectifs[i].getNode().getName()),
                            "intention": objectifs[i].getIntention(),
                            "weightInit": objectifs[i].getNode().getWeight()}
        logs.logToFile(f_log, "[Objective]", str(contentObjective))

    logs.blankToFile(f_log)
    return objectifs


def setPathObjectifs(objectifs, f_log):
    for i in range(len(objectifs)):
        objectifs[i].setPath([])
        objectifs[i].addPath(
            [(objectifs[i].getNode().getId(), objectifs[i].getNode().getName()), ""])

    return objectifs
