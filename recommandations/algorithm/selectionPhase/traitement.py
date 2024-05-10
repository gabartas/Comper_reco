#!/usr/bin/python3
# -*- coding: utf-8 -*-

import datetime  # to remove after logs ok
import sys

from recommandations.referential.objectives import Objectif

from ..logs import logWriter
from ..priority import weightNodeNodePart


sys.path.append("..")
sys.path.append("../..")


def traitementSelectionProcedure(traitement_param, selection_rules, current_obj, CIBLES, referentiel, objectifs, SELECTED_NODES, errors, alpha, prioTags, intention_obj_init, modules, f):
    # node_obj = current_obj.getNode()
    # intention_obj = current_obj.getIntention()

    for data in CIBLES:
        node = data["node"]
        path = data["path"]
        # Weight_node = data["Weight"]
        # profondeur_node = data["profondeur"]
        # relationFather = data["relationFromFather"]
        # father = data["father"]

        a_ete_traiter = False
        for r in selection_rules:
            if r.getCondition().evaluate(node):
                logWriter(f, datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d_%H%M%S_%f"),
                          modules, "[treatment][", r.getId(), "]",
                          {"node": (node.getId(), node.getName())})
                a_ete_traiter = True

                # APPLICATION de la règle
                selection_part = r.getSelectionParameters()
                recursion_part = r.getRecursionParameters()

                # sélection du noeud
                if selection_part["isSelected"]:
                    for tag in selection_part["tagSelection"]:
                        logWriter(f, datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d_%H%M%S_%f"),
                                  modules, "[treatment][", r.getId(
                        ), "][selection]",
                            {"node": (node.getId(), node.getName()),
                             "weight": node.getWeight(),
                             "tag": tag,
                             "path": path})
                        SELECTED_NODES.append((node,
                                              tag,
                                              node.getWeight(),
                                              path
                                               ))
                    tag_for_prio = selection_part["tagSelection"][0]
                    # on ajoute f_node
                    p_expert = weightNodeNodePart(
                        alpha, prioTags, intention_obj_init, tag_for_prio)
                    p = (1.0 - alpha) * node.getWeight() + alpha * p_expert
                    logWriter(f, datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d_%H%M%S_%f"),
                              modules, "[treatment][", r.getId(), "][weight]",
                              {"node": (node.getId(), node.getName()),
                                       "hierachical_part": node.getWeight(),
                                       "alpha": alpha,
                                       "node_part": p_expert,
                                       "weight_node": p})
                    node.setWeight(p)

                # récursion du noeud
                if recursion_part["hasRecursion"]:
                    logWriter(f, datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d_%H%M%S_%f"),
                              modules, "[treatment][", r.getId(), "][recursion]",
                              {"node": (node.getId(), node.getName()),
                                       "intention": recursion_part["intention"]})

                    for intention in recursion_part["intention"]:
                        new_obj = Objectif(referentiel, node, intention)
                        new_obj.setPath(path)
                        objectifs.append(new_obj)

        if not a_ete_traiter:
            logWriter(f, datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d_%H%M%S_%f"),
                      modules, "[treatment] No selection rules applicable for this node")

    return objectifs, SELECTED_NODES, errors
