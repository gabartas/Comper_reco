#!/usr/bin/python3
# -*- coding: utf-8 -*-

import datetime
import json
import os
import sys
import time

from ..api import consts


# Parameters for logs :
list_properties_resources = ["id_n",
                             "name",
                             "interactivityType",
                             "learningResourceType",
                             "significanceLevel",
                             "difficulty",
                             "typicalLearningTime",
                             "learningPlatform",
                             "location",
                             "author",
                             "language",
                             "generative"]

# ========================== TIME FUNCTIONS ==========================


def getDateTime():
    return str(datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d_%H%M%S_%f"))


start_time = 0


def startTimer(textToDisplay):
    global start_time
    print("\t" + textToDisplay, end="")
    start_time = time.time()


def logStopTimer():
    time_to_do = time.time() - start_time
    print(" -->  ", time_to_do, "s")

# ========================== LOG CREATION ==========================


def createRepertory(date, ref_id):
    # creation of log rep
    name_framework_repertory = f'{consts.DATA_PATH}LOG/{ref_id}/'
    name_repertory = f'{name_framework_repertory}{date}/'

    if not os.path.exists(name_framework_repertory):
        os.mkdir(name_framework_repertory)
    os.mkdir(name_repertory)

    return name_repertory


def saveProfile(repertory, date, profile):
    fprofile = open(f'{repertory}profile_{date}.json', "w", encoding="utf-8")
    fprofile.write(json.dumps(profile.profile_data_api,
                   indent=4, ensure_ascii=False))
    fprofile.close()


def saveGraphProfile(repertory, date, profile):
    graphviz = profile.getGraphviz()
    graphviz.render(date, format="png", directory=repertory)


def createLogFile(repertory, date, debug=False):
    if not debug:
        f = open(f'{repertory}trace_algo_{date}.trace', "w", encoding='utf-8')
    else:
        f = sys.__stdout__

    return f


def logToFile(f_log, modules, content):
    # modules are headers before log content [xxx][xxx][xxx]
    date = getDateTime()

    f_log.write(date+modules+" "+content+"\n")


def blankToFile(f_log):
    f_log.write("\n\n")


def formatObjective(obj):
    node = obj.getNode()
    intent = obj.getIntention()
    return "[Obj <"+str((node.getId(), node.getName()))+", "+ intent +">]"

# ========================== Functions FOR LOGS ==========================


def saveFrameworkToLog(f_log, framework):
    global list_properties_resources

    logToFile(f_log, "[Referential][FwId]", str(framework.id))
    logToFile(f_log, "[Referential][Name]", framework.name)
    for id_n, node in framework.getNodes().items():
        if node.getTypeN() != "Resource":
            contentNode = {"id": node.getId(),
                           "name": node.getName(),
                           "type": node.getTypeN()}
            logToFile(f_log, "[Referential][Node]", str(contentNode))
        else:
            contentRes = {"id" if k == "id_n" else k: v for k,
                          v in node.__dict__.items() if k in list_properties_resources}
            logToFile(f_log, "[Referential][Resource]", str(contentRes))

    for id_n, node in framework.getNodes().items():
        for relation, nodeList in node.getLinks().items():
            for node2 in nodeList:
                contentRelation = {"idFrom": node.getId(),
                                   "nameFrom": node.getName(),
                                   "idTo": node2.getId(),
                                   "nameTo": node2.getName(),
                                   "nameRel": relation}
                logToFile(f_log, "[Referential][Relation]",
                          str(contentRelation))
    blankToFile(f_log)


def saveProfileToLog(f_log, profile):
    logToFile(f_log, "[Profile][User]", str(profile.user))
    logToFile(f_log, "[Profile][User][Name]", str(profile.username))
    for id_n, node in profile.getNodes().items():
        if node.getTypeN() not in ["Framework", "Resource"]:
            contentProfileValues = {"node": (id_n, node.getName()),
                                    "values": node.getData()}
            logToFile(f_log, "[Profile][Values]", str(contentProfileValues))
    blankToFile(f_log)


def savePathsToLog(f_log, SELECTED_NODES):
    new_selected = {}
    for obj, selected in SELECTED_NODES.items():
        new_selected[obj] = []
        for i in range(len(selected)):
            # we remove the saved path
            new_selected[obj].append(selected[i][:3])

            if len(SELECTED_NODES[obj][i]) > 3:
                path = SELECTED_NODES[obj][i][3]
                node = SELECTED_NODES[obj][i][0]

                contentPath = {"nodeSelected": [node.getId(), node.getName()],
                               "pathFromObjective": path}
                logToFile(f_log, f"[Selection][KSC]{formatObjective(obj)}[Path]", str(contentPath))

    blankToFile(f_log)
    return new_selected


def logWriter(f, *args):
    var = ""
    for s in args:
        if not isinstance(s, str):
            s = str(s)
        var += s
    var += "\n"
    return f.write(var)
