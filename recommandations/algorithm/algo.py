#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

from . import logs, objectif, ordonnancement
from . import resources as res
from .selectionPhase.selectionNodes import selectionNodes


sys.path.append("..")


def applyStrategy(objects, id_strategy, framework, profile, objectives_list):
    # creation of log rep and files
    date = logs.getDateTime()
    ref_id = str(framework.id)

    repertory = logs.createRepertory(date, ref_id)
    logs.saveProfile(repertory, date, profile)
    # saveGraphProfile(repertory, date, profile)
    f_log = logs.createLogFile(repertory, date, debug=False)

    # ----------------------------------------------------------------
    # we save the referential
    logs.saveFrameworkToLog(f_log, framework)
    # we save the profile
    logs.saveProfileToLog(f_log, profile)
    # -----------------------------------------------------------------

    strategy = objects[id_strategy]
    objectives = objectives_list.copy()

    # set priority 0
    profile.resetWeights()
    # we set priority of objectives
    objectives = objectif.setWeightObjectifs(
        objectives, strategy.getWeightObjective(), f_log)
    # set the path for objectives
    objectives = objectif.setPathObjectifs(objectives, f_log)
    # -----------------------------------------------------------------

    # selection des noeuds
    logs.startTimer("[Selection][KSC]")
    SELECTED_NODES, errors = selectionNodes(strategy,
                                            framework,
                                            objectives,
                                            profile,
                                            f_log)
    # on sauvegarde les chemins
    SELECTED_NODES = logs.savePathsToLog(f_log, SELECTED_NODES)
    logs.logStopTimer()

    # UNICITY --> DOUBLONS
    logs.startTimer("[Ordering][KSC] Unique")
    SELECTED_NODES = ordonnancement.unicitySelectedNodes(SELECTED_NODES, strategy.getPrioTags(), f_log)
    logs.logStopTimer()

    # ordonnancement
    logs.startTimer("[Ordering][KSC]")
    ORDERED_NODES = ordonnancement.orderSelectedNodes(SELECTED_NODES, strategy.getPrioTags(), f_log)
    logs.logStopTimer()

    # selection ressources
    logs.startTimer("[Resources][Selection]")
    resources = res.selectResources(profile, ORDERED_NODES, f_log)
    logs.logStopTimer()

    # UNICITY --> DOUBLONS
    logs.startTimer("[Resources][Selection] Unique")
    resources = ordonnancement.unicitySelectedRessources(resources, f_log)
    logs.logStopTimer()

    # ordonnancement
    logs.startTimer("[Resources][Order]")
    resources = res.orderSelectedResources(resources, strategy.getResourcesParameters(), f_log)
    logs.logStopTimer()

    # restriction
    logs.startTimer("[Resources][Restriction]")
    resources = res.restrictResources(resources, strategy.getResourcesParameters(), f_log)
    logs.logStopTimer()

    # pprint.pprint(resources)
    ret = res.prepareOutputFromRessources(resources)

    return ret, repertory
