#!/usr/bin/python3
# -*- coding: utf-8 -*-

import datetime
import functools

from . import logs


def selectResources(profile, ORDERED_NODES, f):
    resources = []
    i = 1
    for obj, nodes in ORDERED_NODES.items():
        j = 1
        ressource_ids = []
        for node in nodes:
            j += 1
            # print(node)
            # hasTraining > hasLearning
            if node[0].hasLink("hasTraining") or node[0].hasLink("hasLearning"):
                for resource in node[0].getDescendants("hasLearning"):
                    res = profile.getNodeById(
                        profile.getIdByName(resource.getName()))
                    if res.getTypeN() == "Resource":
                        if res.getId() not in ressource_ids:
                            # print("\t", res, (i,j))
                            ressource_ids.append(res.getId())
                            f.write(datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d_%H%M%S_%f") + "[Selection][resources][Obj <" + str((obj.getNode().getId(), obj.getNode().getName(
                            ))) + ", " + obj.getIntention() + ">]" + str({"resource": (res.getId(), res.getName()), "tagSelection": node[1], "weight": node[2], "fromNode": (node[0].getId(), node[0].getName())}) + "\n")
                            resources.append({"res": res, "objectiveNode": obj.getNode(), "nobj": str(
                                i), "node": node[0], "tag": node[1], "weight": node[2], "id": res.getId(), "order_node": [i, j], "relation": "hasLearning"})
                for resource in node[0].getDescendants("hasTraining"):
                    res = profile.getNodeById(
                        profile.getIdByName(resource.getName()))
                    if res.getTypeN() == "Resource":
                        if res.getId() not in ressource_ids:
                            # print("\t", res, (i,j))
                            ressource_ids.append(res.getId())
                            f.write(datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d_%H%M%S_%f") + "[Selection][resources][Obj <" + str((obj.getNode().getId(), obj.getNode().getName(
                            ))) + ", " + obj.getIntention() + ">]" + str({"resource": (res.getId(), res.getName()), "tagSelection": node[1], "weight": node[2], "fromNode": (node[0].getId(), node[0].getName())}) + "\n")
                            resources.append({"res": res, "objectiveNode": obj.getNode(), "nobj": str(
                                i), "node": node[0], "tag": node[1], "weight": node[2], "id": res.getId(), "order_node": [i, j], "relation": "hasTraining"})
        i += 1
        logs.blankToFile(f)
    return resources


def compareResourcesForANode(r1, r2):
    # to send in ressources metadata augment by list_metadata_order, ordering_metadata

    for metadata in r1["list_metadata_order"]:
        # we choose the right method of ordering
        if str(type(r1["ordering_metadata"][metadata])) == str(type("")):
            # ascending or descending --> we just look th numeric values
            if r1["res"].getMetaDataValue(metadata) > r2["res"].getMetaDataValue(metadata):
                return 1 if r1["ordering_metadata"][metadata] == "ascending" else -1
            elif r1["res"].getMetaDataValue(metadata) < r2["res"].getMetaDataValue(metadata):
                return -1 if r1["ordering_metadata"][metadata] == "ascending" else 1
        else:
            # we need to look the order giving by the SP
            index_r1 = r1["ordering_metadata"][metadata].index(
                r1["res"].getMetaDataValue(metadata))
            index_r2 = r2["ordering_metadata"][metadata].index(
                r2["res"].getMetaDataValue(metadata))
            if index_r1 > index_r2:
                return 1
            elif index_r1 < index_r2:
                return -1

    # we can't order them
    return 0


def orderSelectedResources(SELECTED_RESOURCES, SP_resources, f):
    # print("SP_resources", SP_resources)
    f.write("\n\n")

    # order ressources by nodes ordered
    resources = sorted(SELECTED_RESOURCES, key=lambda t: t["id_in_list_res"])
    resources_by_nodes_ordered = groupResourcesByNodes(resources)

    # we augment the ressources with parameters
    for node in resources_by_nodes_ordered.keys():
        for res in resources_by_nodes_ordered[node]:
            res["list_metadata_order"] = SP_resources["list_metadata_order"]
            res["ordering_metadata"] = SP_resources["ordering_metadata"]

    # order resources inside each node
    resources_list_final = []
    for node, resources in resources_by_nodes_ordered.items():
        if len(resources) < 2:  # simple add the ressources or the no resources
            resources_list_final.extend(resources)
        else:  # we need to order them

            """f.write(datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d_%H%M%S_%f")+"[Ordering][resources] need to order for "+str(node)+" #"+str(resources[0]["node"].getId())+"\n")
            for r in resources:
                f.write(datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d_%H%M%S_%f")+"[Ordering][resources]\t"+str(r["res"].getMetadata())+"\n")
            """

            # we order them
            sorted_res = sorted(
                resources, key=functools.cmp_to_key(compareResourcesForANode))

            # we unaugment them
            for r in sorted_res:
                del r["list_metadata_order"]
                del r["ordering_metadata"]

                resources_list_final.append(r)

            f.write(datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d_%H%M%S_%f") + "[Ordering][resources] Ordered for node " + str((resources[0]["node"].getId(
            ), resources[0]["node"].getName())) + " in " + str((resources[0]["objectiveNode"].getId(), resources[0]["objectiveNode"].getName())) + "-->\n")
            for r in sorted_res:
                f.write(datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d_%H%M%S_%f") + "[Ordering][resources]\t id #" + str(r["id"]) + " " + str(r["res"].getMetadata()) + "\n")

    for res in resources:
        dico = dict(res)
        dico['objectiveNode'] = (
            res["objectiveNode"].getId(), res["objectiveNode"].getName())
        dico["node"] = (res["node"].getId(), res["node"].getName())
        f.write(datetime.datetime.strftime(datetime.datetime.now(),
                "%Y%m%d_%H%M%S_%f") + "[Ordering][resources][Out]" + str(dico) + "\n")

    logs.blankToFile(f)

    return resources_list_final


def sommeOfTypicalLearningTime(l_selected_resources):
    total_time = 0
    for r in l_selected_resources:
        total_time += r["res"].getTypicalLearningTime()

    return total_time


def groupResourcesByNodes(resources):
    resources_by_nodes_ordered = {}
    for r in resources:
        if "id_in_list_res" in r.keys():
            del r["id_in_list_res"]  # we no need it no more

        if tuple(r["order_node"]) not in list(resources_by_nodes_ordered.keys()):
            resources_by_nodes_ordered[tuple(r["order_node"])] = [r]
        else:
            resources_by_nodes_ordered[tuple(r["order_node"])].append(r)

    return resources_by_nodes_ordered


def groupResourcesByObjectives(resources):
    resources_by_obj_ordered = {}
    for r in resources:
        if r["objectiveNode"] not in list(resources_by_obj_ordered.keys()):
            resources_by_obj_ordered[r["objectiveNode"]] = [r]
        else:
            resources_by_obj_ordered[r["objectiveNode"]].append(r)

    return resources_by_obj_ordered


def restrictResources(ORDERED_RESOURCES, SP_resources, f):
    # ================================================= NODE =================================================
    # we separate the global list to group resources by nodes
    resources = ORDERED_RESOURCES
    resources_by_nodes_ordered = groupResourcesByNodes(resources)

    if SP_resources["restriction_parameters"]["MAX_RESOURCES_NODE"] != 0:
        f.write("")
        for node, resources in resources_by_nodes_ordered.items():
            while len(resources) > SP_resources["restriction_parameters"]["MAX_RESOURCES_NODE"]:
                f.write(datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d_%H%M%S_%f") + "[Restricting][resources] MAX_RESOURCES_NODE(#" + str(
                    node) + "), limit:" + str(SP_resources["restriction_parameters"]["MAX_RESOURCES_NODE"]) + ", removed#" + str(resources[-1]["res"].getId()) + "\n")
                resources = resources[:-1]
            resources_by_nodes_ordered[node] = resources

    if SP_resources["restriction_parameters"]["MAX_TIME_WORK_NODE"] != 0:
        f.write("")
        for node, resources in resources_by_nodes_ordered.items():
            while sommeOfTypicalLearningTime(resources) > SP_resources["restriction_parameters"]["MAX_TIME_WORK_NODE"]:
                f.write(datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d_%H%M%S_%f") + "[Restricting][resources] MAX_TIME_WORK_NODE(#" + str(
                    node) + "), limit:" + str(SP_resources["restriction_parameters"]["MAX_TIME_WORK_NODE"]) + ", removed#" + str(resources[-1]["res"].getId()) + "\n")
                resources = resources[:-1]
            resources_by_nodes_ordered[node] = resources

    # we recombine to a global list
    resources_restricted = []
    for node, resources in resources_by_nodes_ordered.items():
        resources_restricted.extend(resources)

    # ================================================= OBJECTIVE =================================================
    # we separate the global list to group resources by nodes
    resources = resources_restricted
    resources_by_obj_ordered = groupResourcesByObjectives(resources)

    if SP_resources["restriction_parameters"]["MAX_RESOURCES_OBJECTIVE"] != 0:
        f.write("")
        for node, resources in resources_by_obj_ordered.items():
            while len(resources) > SP_resources["restriction_parameters"]["MAX_RESOURCES_OBJECTIVE"]:
                f.write(datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d_%H%M%S_%f") + "[Restricting][resources] MAX_RESOURCES_OBJECTIVE(#" + str(
                    node) + "), limit:" + str(SP_resources["restriction_parameters"]["MAX_RESOURCES_OBJECTIVE"]) + ", removed#" + str(resources[-1]["res"].getId()) + "\n")
                resources = resources[:-1]
            resources_by_obj_ordered[node] = resources

    if SP_resources["restriction_parameters"]["MAX_TIME_WORK_OBJECTIVE"] != 0:
        f.write("")
        for node, resources in resources_by_obj_ordered.items():
            while sommeOfTypicalLearningTime(resources) > SP_resources["restriction_parameters"]["MAX_TIME_WORK_OBJECTIVE"]:
                f.write(datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d_%H%M%S_%f") + "[Restricting][resources] MAX_TIME_WORK_OBJECTIVE(#" + str(
                    node) + "), limit:" + str(SP_resources["restriction_parameters"]["MAX_TIME_WORK_OBJECTIVE"]) + ", removed#" + str(resources[-1]["res"].getId()) + "\n")
                resources = resources[:-1]
            resources_by_obj_ordered[node] = resources

    # we recombine to a global list
    resources_restricted = []
    for node, resources in resources_by_obj_ordered.items():
        resources_restricted.extend(resources)

    # ================================================= RECOMMENDATION =================================================
    if SP_resources["restriction_parameters"]["MAX_TIME_WORK_RECO"] != 0:
        f.write("")
        while sommeOfTypicalLearningTime(resources_restricted) > SP_resources["restriction_parameters"]["MAX_TIME_WORK_RECO"]:
            f.write(datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d_%H%M%S_%f") + "[Restricting][resources] MAX_TIME_WORK_RECO, limit:" + str(
                SP_resources["restriction_parameters"]["MAX_TIME_WORK_RECO"]) + ", removed#" + str(resources[-1]["res"].getId()) + "\n")
            resources_restricted = resources_restricted[:-1]

    if SP_resources["restriction_parameters"]["MAX_RESOURCES_RECO"] != 0:
        f.write("")
        while len(resources_restricted) > SP_resources["restriction_parameters"]["MAX_RESOURCES_RECO"]:
            f.write(datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d_%H%M%S_%f") + "[Restricting][resources] MAX_RESOURCES_RECO, limit:" + str(
                SP_resources["restriction_parameters"]["MAX_RESOURCES_RECO"]) + ", removed#" + str(resources[-1]["res"].getId()) + "\n")
            resources_restricted = resources_restricted[:-1]

    f.write("\n")

    for res in resources_restricted:
        f.write(datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d_%H%M%S_%f") + "[Restricting][resources][out] #" + str((res["res"].getId(), res["node"].getId(), res["objectiveNode"].getId())) + "\n")

    logs.blankToFile(f)

    return resources_restricted


def prepareOutputFromRessources(resources):
    ret = []
    for res in resources:
        ret.append({
            "title": res["res"].getName(),
            "location": res["res"].getLocation(),
            "learning_type": res["res"].getLearningResourceType(),
            "learning_platform": res["res"].getLearningPlatform(),
            "objectiveNode": res["objectiveNode"].getName(),
            "nobj": res["nobj"],
            "node": res["node"].getName(),
            "tag": res["tag"],
            "weight": res["weight"],
            "id": res["id"]
        })

    return ret
