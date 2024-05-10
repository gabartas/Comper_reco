#!/usr/bin/python3
# -*- coding: utf-8 -*-
import datetime  # to remove after logs ok
import sys

from ..logs import logWriter
from ..priority import weightNodeHierarchicalPart


sys.path.append("..")


def preTraitementSelectionProcedure(preTraitements_param, current_obj, A_TRAITER, weight_r, alpha, errors, modules, f):
    node_obj = current_obj.getNode()
    intention_obj = current_obj.getIntention()

    relations = preTraitements_param["relations_to_follow"]
    if relations == []:
        logWriter(f, datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d_%H%M%S_%f"),
                  modules, "[preTreatment] Same output as initialisation (no relation to follow)")
        CIBLES = A_TRAITER.copy()
    else:
        preTraitement_relation_to_follow = relations

        logWriter(f, datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d_%H%M%S_%f"),
                  modules, "[preTreatment][parameters] relation_to_follow = ",
                  preTraitement_relation_to_follow)

        CIBLES = []
        id_list = []

        # print("\n A_TRAITER", [d["node"] for d in A_TRAITER])

        # we set the number of transversal relations followed
        for i in range(len(A_TRAITER)):
            A_TRAITER[i]["nb_transversal_follow"] = 0

        while len(A_TRAITER) != 0:
            # print("\n A_TRAITER", [d["node"] for d in A_TRAITER])
            data = A_TRAITER.pop(0)

            node = data["node"]
            # Weight_node = data["Weight"]
            profondeur_node = data["profondeur"]
            # relationFather = data["relationFromFather"]
            # father = data["father"]
            path = data["path"]
            nb_transversal_follow = data["nb_transversal_follow"]

            logWriter(f, datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d_%H%M%S_%f"),
                      modules, "[preTreatment][node] Follow ", {"node": (node.getId(), node.getName())})

            if preTraitements_param["depth_max"] == 0 or nb_transversal_follow < preTraitements_param["depth_max"]:

                for relation in preTraitement_relation_to_follow:
                    for fils in node.getDescendants(relation):
                        # priorité des descendants
                        weight_descendant = weightNodeHierarchicalPart(
                            alpha, profondeur_node + 1, weight_r[relation], node.getWeight())
                        fils.setWeight(weight_descendant)

                        logWriter(f, datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d_%H%M%S_%f"),
                                  modules, "[preTreatment][node][weight] ",
                                  {"node": (fils.getId(), fils.getName()),
                                   "alpha": alpha,
                                   "depth": profondeur_node + 1,
                                   "weight_r": weight_r[relation],
                                   "weight_father": node.getWeight(),
                                   "Weight_node": weight_descendant})

                        if fils.getId() not in id_list:
                            if preTraitements_param["condition_selection"] == "":
                                new_path = list(path)
                                new_path.append(
                                    [(fils.getId(), fils.getName()), relation])
                                id_list.append(fils.getId())
                                new_CIBLE = {"node": fils,
                                             "Weight": weight_descendant,
                                             "profondeur": profondeur_node + 1,
                                             "relationFromFather": relation,
                                             "father": node,
                                             "path": new_path}

                                logWriter(f, datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d_%H%M%S_%f"),
                                          modules, "[preTreatment][node] Added ",
                                          {"node": (fils.getId(), fils.getName()),
                                           "father": (node.getId(), node.getName()),
                                           "relation": relation,
                                           "depth": profondeur_node + 1,
                                           "path": new_path})

                                CIBLES.append(new_CIBLE)
                            elif preTraitements_param["condition_selection"].evaluate(node):
                                new_path = list(path)
                                new_path.append(
                                    [(fils.getId(), fils.getName()), relation])
                                id_list.append(fils.getId())

                                logWriter(f, datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d_%H%M%S_%f"),
                                          modules, "[preTreatment][node] Added ",
                                          {"node": (fils.getId(), fils.getName()),
                                           "father": (node.getId(), node.getName()),
                                           "relation": relation,
                                           "depth": profondeur_node + 1,
                                           "path": new_path})

                                CIBLES.append({"node": fils,
                                               "Weight": weight_descendant,
                                               "profondeur": profondeur_node + 1,
                                               "relationFromFather": relation,
                                               "father": node,
                                               "path": new_path})
                            else:
                                new_path = list(path)
                                new_path.append(
                                    [(fils.getId(), fils.getName()), relation])

                                errors.append({"Objectif": ((node_obj.getId(), node_obj.getName()), intention_obj),
                                               "Node": (node.getId(), node.getName()),
                                               "Error": preTraitements_param["message_erreur"]})

                                logWriter(f, datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d_%H%M%S_%f"),
                                          modules, "[preTreatment][node][error] ",
                                          {"node": (fils.getId(), fils.getName()),
                                           "father": (node.getId(), node.getName()),
                                           "relation": relation,
                                           "depth": profondeur_node + 1,
                                           "message": preTraitements_param["message_erreur"],
                                           "path": new_path})

                        if profondeur_node + 1 < preTraitements_param["depth_max"]:
                            new_path = list(path)
                            new_path.append(
                                [(fils.getId(), fils.getName()), relation])
                            A_TRAITER.append({"node": fils,
                                              "profondeur": profondeur_node + 1,
                                              "relationFromFather": relation,
                                              "father": node,
                                              "path": new_path,
                                              "nb_transversal_follow": nb_transversal_follow + 1})

    for data in CIBLES:
        logWriter(f, datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d_%H%M%S_%f"),
                  modules, "[preTreatment][output] ",
                  {"node": (data["node"].getId(), data["node"].getName()),
                   "weight": data["node"].getWeight(),
                   "depth": data["profondeur"],
                   "relation": data["relationFromFather"],
                   "father": (data["father"].getId(), data["father"].getName()) if data["father"] is not None else (None, None)})

    return CIBLES, errors
