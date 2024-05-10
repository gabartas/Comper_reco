#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

from recommandations.referential.objectives import Objectif

from .. import logs
from .initialisation import initialisationSelectionProcedure
from .preTraitement import preTraitementSelectionProcedure
from .traitement import traitementSelectionProcedure


sys.path.append("..")
sys.path.append("../..")


def selectionNodes(strategy, framework, objectifs_list, profil, f_log):
    errors = []

    # we loop over all objectives
    selectedNodesGroupByObj = {}

    for initial_objective in objectifs_list:
        objectifs = [initial_objective]
        SELECTED_NODES = []
        errors = []
        treated_nodes = {intention: []
                         for intention in Objectif.INTENTION_LIST}
        intention_obj_init = initial_objective.getIntention()

        while len(objectifs) != 0:
            current_objective = objectifs.pop(0)

            # we get information from the current objective
            node_obj, intention_obj = current_objective.getNode(), current_objective.getIntention()

            if node_obj.getId() in treated_nodes[intention_obj]:
                logs.logToFile(
                    f_log, "[Selection][KSC]"+logs.formatObjective(current_objective), "Node already treated")
            else:
                # we add the node to the set of treated_nodes for this intention
                treated_nodes[intention_obj].append(node_obj.getId())

                # we look for selection procedure applicable
                applicables_procedures = [procedure for procedure in strategy.getKSCSelectionProcedures()
                                          if procedure.getIntentions().evaluate(intention_obj)]

                if applicables_procedures != []:
                    # find a way to order if more than one procedure can be applied
                    proceduresToApply = applicables_procedures.copy()

                    # ----------------------------------------------------------------------------------------------------------
                    for procedure in proceduresToApply:
                        modules = "[Selection][KSC]"+logs.formatObjective(current_objective)+"["+str(procedure.getId())+"]"
                        logs.logToFile(f_log, modules, "")

                        objectifs, SELECTED_NODES, errors = applySelectionprocedure(strategy,
                                                                                    procedure,
                                                                                    objectifs,
                                                                                    current_objective,
                                                                                    framework,
                                                                                    intention_obj_init,
                                                                                    SELECTED_NODES,
                                                                                    errors,
                                                                                    modules,
                                                                                    f_log)
                else:
                    logs.logToFile(
                        f_log, "[Selection][KSC]"+logs.formatObjective(current_objective), "No selection procedure for this objective")

        for selected in SELECTED_NODES:
            contentSelected = {
                "node": (selected[0].getId(), selected[0].getName()),
                "tagSelection": selected[1],
                "priority": selected[2],

            }

            logs.logToFile(
                f_log, "[Selection][KSC]"+logs.formatObjective(current_objective)+"[Output]", str(contentSelected))

        selectedNodesGroupByObj[initial_objective] = SELECTED_NODES.copy()
        logs.blankToFile(f_log)

    return selectedNodesGroupByObj, errors


def applySelectionprocedure(strategy, procedure, objectives, current_obj, referential, intention_obj_init, SELECTED_NODES, errors, modules, f_log):
    intention_obj = current_obj.getIntention()
    weight_r = strategy.getWeightR()

    # *******************************************************************************
    # INITIALISATION
    A_TRAITER = initialisationSelectionProcedure(procedure.getInitialisation(),
                                                 current_obj,
                                                 weight_r[intention_obj],
                                                 strategy.getAlpha(),
                                                 modules,
                                                 f_log)
    # *******************************************************************************

    # *******************************************************************************
    # PRE_TRAITEMENT
    CIBLES, errors = preTraitementSelectionProcedure(procedure.getPreTraitementParam(),
                                                     current_obj,
                                                     A_TRAITER,
                                                     weight_r[intention_obj],
                                                     strategy.getAlpha(),
                                                     errors,
                                                     modules,
                                                     f_log)
    # *****************************************************************************************************

    # *****************************************************************************************************
    # TRAITEMENT
    traitement_param = procedure.getTraitementParam()
    objectives, SELECTED_NODES, errors = traitementSelectionProcedure(traitement_param,
                                                                      traitement_param["selection_rules"],
                                                                      current_obj,
                                                                      CIBLES,
                                                                      referential,
                                                                      objectives,
                                                                      SELECTED_NODES,
                                                                      errors,
                                                                      strategy.getAlpha(),
                                                                      strategy.getPrioTags(),
                                                                      intention_obj_init,
                                                                      modules,
                                                                      f_log)

    return objectives, SELECTED_NODES, errors
