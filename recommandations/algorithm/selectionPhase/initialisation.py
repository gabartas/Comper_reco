#!/usr/bin/python3
# -*- coding: utf-8 -*-
import datetime  # to remove after logs ok
import sys

from ..logs import logWriter
from ..priority import weightNodeHierarchicalPart


sys.path.append("..")


def initialisationSelectionProcedure(init_param, current_obj, weight_r, alpha, modules, f):
    node_obj = current_obj.getNode()
    # intention_obj = current_obj.getIntention()
    path_obj = current_obj.getPath()

    init_relations_to_follow = init_param["relations_to_follow"]
    profondeur_max = init_param["depth_max"]

    logWriter(f, datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d_%H%M%S_%f"),
              modules, "[initialisation][parameters] init_relations_to_follow = ",
              init_relations_to_follow)
    logWriter(f, datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d_%H%M%S_%f"),
              modules, "[initialisation][parameters] profondeur_max = ",
              profondeur_max)

    A_TRAITER = [{"node": node_obj,
                  "Weight": node_obj.getWeight(),
                  "profondeur": 0,
                  "relationFromFather": None,
                  "father": None,
                  "path": path_obj
                  }]

    if init_relations_to_follow != []:
        listNodeParcours = [
            {"node": node_obj, "profondeur": 0, "relation": None, "path": path_obj}]

        id_list = [node_obj.getId()]

        while len(listNodeParcours) != 0:
            data = listNodeParcours.pop(0)

            node = data["node"]
            path = data["path"]
            profondeur_node = data["profondeur"]

            logWriter(f, datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d_%H%M%S_%f"),
                      modules, "[initialisation][node] Followed ",
                      {"node": (node.getId(), node.getName())})

            for relation in init_relations_to_follow:
                for descendant in node.getDescendants(relation):
                    # priorité des descendants
                    p = weightNodeHierarchicalPart(
                        alpha, profondeur_node + 1, weight_r[relation], node.getWeight())
                    descendant.setWeight(p)
                    logWriter(f, datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d_%H%M%S_%f"),
                              modules, "[initialisation][node][weight] ",
                              {"node": (descendant.getId(), descendant.getName()),
                                       "alpha": alpha,
                                       "depth": profondeur_node + 1,
                                       "weight_r": weight_r[relation],
                                       "weight_father": node.getWeight(),
                                       "Weight_node": p})

                    if descendant.getId() not in id_list:
                        id_list.append(descendant.getId())
                        new_path = list(path)
                        new_path.append(
                            [(descendant.getId(), descendant.getName()), relation])
                        new_A_TRAITER = {"node": descendant,
                                         "Weight": descendant.getWeight(),
                                         "profondeur": profondeur_node + 1,
                                         "relationFromFather": relation,
                                         "father": node,
                                         "path": new_path
                                         }
                        logWriter(f, datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d_%H%M%S_%f"),
                                  modules, "[initialisation][node] Added ",
                                  {"node": (descendant.getId(), descendant.getName()),
                                           "weight": descendant.getWeight(),
                                           "depth": profondeur_node + 1,
                                           "relation": relation,
                                           "father": (node.getId(), node.getName()),
                                           "path": new_path})
                        A_TRAITER.append(new_A_TRAITER)

                        if profondeur_max == 0 or profondeur_node + 1 <= profondeur_max:
                            new_path = list(path)
                            new_path.append(
                                [(descendant.getId(), descendant.getName()), relation])
                            listNodeParcours.append({"node": descendant,
                                                     "profondeur": profondeur_node + 1,
                                                     "relation": relation,
                                                     "path": new_path
                                                     })

    for data in A_TRAITER:
        logWriter(f, datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d_%H%M%S_%f"),
                  modules, "[initialisation][output] ",
                  {"node": (data["node"].getId(), data["node"].getName()),
                   "weight": data["node"].getWeight(),
                   "depth": data["profondeur"],
                   "relation": data["relationFromFather"],
                   "father": (data["father"].getId(), data["father"].getName()) if data["father"] is not None else (None, None),
                   "path": data["path"]})

    return A_TRAITER
