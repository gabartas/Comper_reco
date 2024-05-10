#!/usr/bin/python3
# -*- coding: utf-8 -*-

import datetime
import functools

from . import logs


def unicitySelectedNodes(SELECTED_NODES, prioTags, f):  # v2
    new_selected = {}

    # calc of max value in prioTags tab
    v_max_prioTags = max([v for intent in prioTags.keys()
                         for v in prioTags[intent].values()])

    for obj, nodes_selected in SELECTED_NODES.items():
        nodes = {}
        for node, tag, weight in nodes_selected:
            if node not in nodes.keys():
                nodes[node] = {"tag": [tag], "weight": [
                    weight], "intention": obj.getIntention()}
            else:
                nodes[node]["tag"].append(tag)
                nodes[node]["weight"].append(weight)

        # elimination of duplicate selected nodes
        nodes2 = {k: {} for k in nodes.keys()}
        for node in nodes.keys():
            if len(nodes[node]["tag"]) > 1:
                # we have multiple intentions so the nodes has been selected multiple times
                # we have to combines them
                # logs.logWriter(f, datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d_%H%M%S_%f"),
                #                "[Selection][KSC][Obj < ", str((obj.getNode().getId(), obj.getNode().getName())), ", ",
                #                obj.getIntention(), ">][Unicity] Mulitple ",
                #                str({"node": (node.getId(), node.getName()), "data": nodes[node]}))
                f.write(datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d_%H%M%S_%f")+"[Selection][KSC][Obj <"+str((obj.getNode().getId(), obj.getNode().getName()))+", "+obj.getIntention()+">][Unicity] Mulitple "+str({"node": (node.getId(), node.getName()), "data": nodes[node]})+"\n")

                # new formula
                # we get the index of the first occ of max
                i_max = nodes[node]["weight"].index(max(nodes[node]["weight"]))

                combiselected = 0
                combitags = 0
                intention = nodes[node]["intention"]
                for tag, weight in zip(nodes[node]["tag"], nodes[node]["weight"]):
                    combiselected += weight * \
                        (v_max_prioTags - prioTags[intention][tag])
                    combitags += v_max_prioTags - prioTags[intention][tag]

                    # max_v = max(prioTags[intention].values())
                    # return (max_v-prioTags[intention][tag])/max_v

                nodes2[node]["weight"] = max(
                    nodes[node]["weight"]) + (1.0 - max(nodes[node]["weight"])) * (combiselected / combitags)
                nodes2[node]["tag"] = nodes[node]["tag"][i_max]

                # logs.logWriter(f, datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d_%H%M%S_%f"),
                #                "[Selection][KSC][Obj <",
                #                obj.getNode().getId(), obj.getNode().getName(), ", ", obj.getIntention(),
                #                ">][Unicity] into ",
                #                {"node": (node.getId(), node.getName()), "data": nodes2[node]},
                #                " gain of ",
                #                "{:.3f}".format((nodes2[node]["weight"] - max(nodes[node]["weight"])) / max(nodes[node]["weight"]) * 100),
                #                "% from prio max")
                f.write(datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d_%H%M%S_%f")+"[Selection][KSC][Obj <"+str((obj.getNode().getId(), obj.getNode().getName()))+", "+obj.getIntention()+">][Unicity] into "+str({"node": (node.getId(), node.getName()), "data": nodes2[node]})+" gain of "+str("{:.3f}".format((nodes2[node]["weight"]-max(nodes[node]["weight"]))/max(nodes[node]["weight"])*100))+"\% from prio max\n")

            else:
                nodes2[node]["weight"] = nodes[node]["weight"][0]
                nodes2[node]["tag"] = nodes[node]["tag"][0]
                # logs.logWriter(f, datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d_%H%M%S_%f"),
                #                "[Selection][KSC][Obj <",
                #                obj.getNode().getId(), obj.getNode().getName(),
                #                ", ", obj.getIntention(), ">][Unicity] Single ",
                #                {"node": (node.getId(), node.getName()), "data": nodes[node]})
                f.write(datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d_%H%M%S_%f")+"[Selection][KSC][Obj <"+str((obj.getNode().getId(), obj.getNode().getName()))+", "+obj.getIntention()+">][Unicity] Single "+str({"node": (node.getId(), node.getName()), "data": nodes[node]})+"\n")

        # set the data for the output format
        new_selected[obj] = [(node, data["tag"], data["weight"])
                             for node, data in nodes2.items()]

        logs.blankToFile(f)
    return new_selected


def unicitySelectedRessources(SELECTED_RESOURCES, f):
    resources = {}
    i = 0
    f.write("\n\n")
    for res in SELECTED_RESOURCES:
        if (res["id"], int(res["nobj"])) not in resources.keys():
            resources[(res["id"], int(res["nobj"]))] = {"res": res["res"],
                                                        "objectiveNode": res["objectiveNode"],
                                                        "order_node": res["order_node"],
                                                        "tag": res["tag"],
                                                        "weight": res["weight"],
                                                        "nobj": res["nobj"],
                                                        "id": res["id"],
                                                        "node": res["node"],
                                                        "id_in_list_res": i
                                                        }
            dicNode = {"node": (res["id"], res["node"].getName()),
                       "objective": {"node": (res["objectiveNode"].getId(), res["objectiveNode"].getName()),
                                     "idObj": int(res["nobj"])}
                       }
            # logs.logWriter(f, datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d_%H%M%S_%f"),
            #                "[Selection][resources][Unicity] Single ", dicNode)
            f.write(datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d_%H%M%S_%f")+"[Selection][resources][Unicity] Single "+str(dicNode)+"\n")

        else:
            dicNode = {"node": (res["id"], res["node"].getName()),
                       "objective": {"node": (res["objectiveNode"].getId(), res["objectiveNode"].getName()),
                                     "idObj": int(res["nobj"])}
                       }
            dic1 = {"tag": resources[(res["id"], int(res["nobj"]))]["tag"], "weight": resources[(
                res["id"], int(res["nobj"]))]["weight"]}
            dic2 = {"tag": res["tag"], "weight": res["weight"]}

            # logs.logWriter(f, datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d_%H%M%S_%f"),
            #                "[Selection][resources][Unicity] Merging for ", dicNode,
            #                " of duplicate selection #1:(", dic1, ") #2:(", dic2, ")")
            f.write(datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d_%H%M%S_%f")+"[Selection][resources][Unicity] Merging for "+str(dicNode)+" of duplicate selection #1:("+str(dic1)+") #2:("+str(dic2)+")\n")

            # we found a selection with a weight more important we adjust the tag and weight
            if max(resources[(res["id"], int(res["nobj"]))]["weight"], res["weight"]) == res["weight"]:
                resources[(res["id"], int(res["nobj"]))]["tag"] = res["tag"]
                resources[(res["id"], int(res["nobj"]))
                          ]["weight"] = res["weight"]

                resources[(res["id"], int(res["nobj"]))
                          ]["order_node"] = res["order_node"]
                resources[(res["id"], int(res["nobj"]))]["node"] = res["node"]

            # logs.logWriter(f, datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d_%H%M%S_%f"),
            #                "[Selection][resources][Unicity] Merging for ", dicNode, " into ",
            #                {"tag": resources[(res["id"], int(res["nobj"]))]["tag"],
            #                 "weight": resources[(res["id"], int(res["nobj"]))]["weight"]})
            f.write(datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d_%H%M%S_%f")+"[Selection][resources][Unicity] Merging for "+str(dicNode)+" into "+str({"tag":resources[(res["id"], int(res["nobj"]))]["tag"], "weight": resources[(res["id"], int(res["nobj"]))]["weight"]})+"\n")

        i += 1
    return sorted([v for k, v in resources.items()], key=lambda t: t["id_in_list_res"])

# ---------------------------------------------------------------------------------------------------------------------


def compareNodes(selected1, selected2):
    n1, tag1, prio1, priotags = selected1
    n2, tag2, prio2, _ = selected2

    mait_n1, conf_n1, couv_n1 = [float(v) for v in n1.getData()]
    mait_n2, conf_n2, couv_n2 = [float(v) for v in n2.getData()]

    # on trie par priorité d'abord
    if prio1 > prio2:  # on prend la valeur la plus forte
        return 1
    elif prio2 > prio1:
        return -1

    # on tri par tag ensuite
    if priotags[tag1] > priotags[tag2]:  # on prend la valeur la plus faible
        return -1
    elif priotags[tag1] < priotags[tag2]:
        return 1
    """
    #on tri par maitrise
    if mait_n1 > mait_n2: #on prend la valeur la plus faible
        return -1
    elif mait_n1 < mait_n2:
        return 1

    #on tri par confiance
    if conf_n1 > conf_n2: #on prend la valeur la plus faible
        return -1
    elif conf_n1 < conf_n2:
        return 1
    """
    return 0


def orderSelectedNodes(SELECTED_NODES, prioTags, f):
    ORDERED_NODES = {}
    for obj, selected in SELECTED_NODES.items():  # deja trié par obj

        # on ajoute a chaque noeud l'ordre de prio des tags pour les recuperer dans la fonction de comp
        augment_selected = [(n, tag, prio, prioTags[obj.getIntention()])
                            for (n, tag, prio) in selected]

        new_selected = sorted(augment_selected, key=functools.cmp_to_key(
            compareNodes), reverse=True)  # on trie par ordre décroissant

        new_unaugment_selected = [(n, tag, prio)
                                  for (n, tag, prio, prioTags) in new_selected]
        ORDERED_NODES[obj] = new_unaugment_selected.copy()

        for order in ORDERED_NODES[obj]:
            # logs.logWriter(f, datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d_%H%M%S_%f"),
            #                "[Ordering][KSC][Obj <", (obj.getNode().getId(), obj.getNode().getName()), ", ",
            #                obj.getIntention(), ">][Out]",
            #                {"node": (order[0].getId(), order[0].getName()),
            #                 "tag": order[1],
            #                 "weight": order[2],
            #                 "values": [float(v) for v in order[0].getData()]})
            f.write(datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d_%H%M%S_%f")+"[Ordering][KSC][Obj <"+str((obj.getNode().getId(), obj.getNode().getName()))+", "+obj.getIntention()+">][Out]"+str({"node": (order[0].getId(), order[0].getName()), "tag": order[1], "weight": order[2], "values": [float(v) for v in order[0].getData()]})+"\n")

        logs.blankToFile(f)
    return ORDERED_NODES
