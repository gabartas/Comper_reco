import datetime
import json
import time
import traceback

import flask
from flask import Blueprint
from flask import current_app as app
from flask import request

from .api import apiFunctions, consts, data
from .pedagogicStrategy import errors as pserrors
from .referential import errors as referrors


# -------------
# Configuration
# -------------
api = Blueprint('api', __name__, url_prefix="/api")
referential = None
STRATEGIES = {}
id_defaultSP = None

# ----------------
# Init function Functions
# ----------------


def initStrategies(app):
    global referential, STRATEGIES, id_defaultSP

    app.logger.info(
        "ANR ComPer project personalization engine. Strategies initialization...")
    # =============================================== REFERENTIAL ===============================================
    # Define reverse relation :
    referential = data.primitiveReferential()

    # =============================================== STRATEGIES ================================================
    """ "idSP" : {"objects" : [], "idSPobject": "", "dateLoading": "", "file": ""}"""
    STRATEGIES, id_defaultSP = data.initStrategy(
        STRATEGIES, app.config["STRATEGY_NAME"])

    app.logger.debug(f"STRATEGIE KEYS: {STRATEGIES[id_defaultSP].keys()}")


@api.before_request
def log_addr():
    app.logger.debug("@IP %s | Request %s %s | Headers %s",
                     flask.request.remote_addr,
                     flask.request.method,
                     flask.request.base_url,
                     str(list(flask.request.headers)).replace("),", "),\n\t\t"))


# ********************** PING **********************
@api.route("/", methods=["GET"])
def ping():
    app.logger.info("service online")
    return 'Service online'


# ********************** STRATEGY / FRAMEWORK **********************
@api.route("/pedagogicStrategy/list/", methods=['GET'])
def pedagogicStrategyList():
    return flask.jsonify(apiFunctions.getAllStrategy()), 200, {'Content-Type': 'application/json'}


@api.route("/pedagogicStrategy/detailledList/", methods=['GET'])
def pedagogicStrategyListDetail():
    return flask.jsonify(apiFunctions.getAllStrategyDetail()), 200, {'Content-Type': 'application/json'}


@api.route("/updateFramework/", methods=['PUT'])
def updateFramework():
    global referential
    # delete current referential saved
    referential = data.primitiveReferential()

    app.logger.info("updateFramework")
    return flask.jsonify("updateFramework done"), 200, {'Content-Type': 'application/json'}


# Token decoding
def getTokenDictionary(auth_token: str):
    dic = {"data": "", "code": 200}

    if auth_token is None:
        dic["data"] = "[Token Error] No token found"
        dic["code"] = 400
        app.logger.error(dic["data"])
    else:
        token_jwt = str.replace(auth_token, "Bearer ", "")
        dic = apiFunctions.decodeToken(token_jwt)
    return dic


# ********************** RESOURCES **********************
@api.route("/logResourceConsultation/", methods=['PUT'])
def logResourceConsultation():

    result = getTokenDictionary(request.headers.get("Authorization"))
    if result["code"] != 200:
        return flask.jsonify(result["data"]), result["code"], {'Content-Type': 'application/json'}

    dicConsultation = result["data"]
    # we check the infos
    app.logger.info(f"Clé du token décrypté: {dicConsultation.keys()}")

    if "username" not in dicConsultation.keys():
        app.logger.warning("Error: the Username isn't present")
        # we do not have all infos
        return flask.jsonify("Error: the infos are incorrects"), 498, {'Content-Type': 'application/json'}

    app.logger.info("Log Resource Consultation ", dicConsultation)

    # write information in the logConsultationFile
    data.completeLogConsultation(
        dicConsultation, "logResourceConsultation.json")

    return "OK", 200, {'Content-Type': 'text/plain'}


# ********************** LOGS **********************
@api.route("/logs/last/", methods=['GET'])
def getLastLogFile():
    app.logger.info("Last log request")

    result = getTokenDictionary(request.headers.get("Authorization"))
    if result["code"] != 200:
        return flask.jsonify(result["data"]), result["code"], {'Content-Type': 'application/json'}

    dic = result["data"]

    # we check the data inside the token
    try:
        username = dic["username"]
        fwid = dic["fwid"]
        # exp = data["exp"]
    except Exception as e:
        app.logger.error("[Error] %s | %s", e, traceback.format_exc())
        return flask.jsonify("Error: " + str(e)), 498, {'Content-Type': 'application/json'}

    recommendations = []
    with open(f'{consts.DATA_PATH}api.json', 'r') as f:
        # Comment:
        recommendations = json.load(f)

    # we create a directory of recommendations indexed by date of recommendations
    # key : (username, framework-id, date-api)
    list_recommendations_repo_user = {}
    for api in recommendations:
        if username in api["user"] and api["fwid"] == fwid:
            list_recommendations_repo_user[datetime.datetime.strptime(
                api["dateReco"], '%Y%m%d_%H%M%S_%f')] = api["dateReco"]

    if len(list_recommendations_repo_user.keys()) == 0:
        app.logger.warning("Error: recommendation not found")
        return flask.jsonify("Error: recommendation not found"), 404, {'Content-Type': 'application/json'}

    # we reconstruct the dictionnary by date most recent first
    reco_ordered = {k: list_recommendations_repo_user[k] for k in list(
        sorted(list_recommendations_repo_user.keys(), reverse=True))}

    dirname = reco_ordered[list(reco_ordered.keys())[0]]

    file_to_send = f"../{consts.DATA_PATH}LOG/{fwid}/{dirname}/trace_algo_{dirname}.trace"
    app.logger.info(file_to_send)
    attachment_name = f'log_{username}_{fwid}_{dirname}.log'
    app.logger.info(
        f"Sending Trace filename {file_to_send} as {attachment_name}")

    return flask.send_file(file_to_send, as_attachment=True, download_name=attachment_name)


# ********************** RECOMMENDATIONS **********************
# ********** TO DELETE ***********************
@api.route("/generate/", methods=['POST'])
@api.route("/generate/<nameSP>/", methods=['POST'])
def generate_recommendation(nameSP=""):
    global my_arguments, referential, id_defaultSP, STRATEGIES

    # ============================== SP ==============================
    # gestion de la SP
    if nameSP == "":
        nameSP = id_defaultSP
    app.logger.info("Generate recommendations with strategy named %s", nameSP)

    # we reload SP if needed
    try:
        STRATEGIES = data.loadStrategy(STRATEGIES, nameSP)
    except Exception as e:
        app.logger.error("[Error] %s | %s", e, traceback.format_exc())
        return flask.jsonify("Error: " + str(e)), 410, {'Content-Type': 'application/json'}
    # ================================================================

    result = getTokenDictionary(request.headers.get("Authorization"))
    if result["code"] != 200:
        return flask.jsonify(result["data"]), result["code"], {'Content-Type': 'application/json'}
    datas = result["data"]

    # we check the data inside the token
    try:
        user = datas["user"]
        # role = data["role"]
        username = datas["username"]
        fwid = datas["fwid"]
        # exp = data["exp"]
    except Exception as e:
        app.logger.error("[Error] %s | %s", e, traceback.format_exc())
        return flask.jsonify("Error: " + str(e)), 498, {'Content-Type': 'application/json'}

    try:
        if (datas["objectives"][-1][0] == "sendTraces"):
            objectives = datas["objectives"][:-1]
            sendTraces = True
        else:
            objectives = datas["objectives"]
            sendTraces = False
    except Exception as e:
        app.logger.error("[Error] %s | %s", e, traceback.format_exc())
        objectives = []

    if objectives == []:
        return flask.jsonify([]), 200, {'Content-Type': 'application/json', 'X-Date': ""}

    app.logger.info("Generating for %s", datas)

    start_time = time.time()
    # we check if the current referential is the one we have to use
    try:
        arguments = {}
        arguments["profile_ip"] = app.config["PROFILE_URL"]
        arguments["profile_path"] = app.config["PROFILE_PATH"]

        profile_data = apiFunctions.requestProfileAPI(arguments, fwid, username)
        app.logger.info("PROFILE RECUPERE")

        if referential.name != "Framework-" + str(fwid):
            referential = data.reloadReferential(fwid, profile_data)

        # we create the profile object
        profile_values = apiFunctions.parseProfileValues(
            referential, profile_data)
        profile = data.loadProfile(referential, profile_values)

        profile.user = user
        profile.username = username
        profile.profile_data_api = profile_data.copy()

    except EnvironmentError as e:
        app.logger.error("[Error] %s | %s", e, traceback.format_exc())
        return flask.jsonify("ProfileError: " + str(e)), 504, {'Content-Type': 'application/json'}
    except (pserrors.PropertyObjectError, referrors.NodeObjectError, referrors.NodeProfileObjectError, referrors.ObjectiveError, referrors.NotAReferential) as e:
        app.logger.error("[Error] %s | %s", e, traceback.format_exc())
        return flask.jsonify("ProfileError: " + str(e)), 400, {'Content-Type': 'application/json'}
    except Exception as e:
        app.logger.error("[Error] %s | %s", e, traceback.format_exc())
        return flask.jsonify("ProfileError: " + str(e)), 520, {'Content-Type': 'application/json'}

    try:
        SPObjectivesParam = apiFunctions.getStrategyObjectivesParameters(
            STRATEGIES, nameSP)
        objectives = (data.loadObjectives(
            profile, SPObjectivesParam, objectives))
        app.logger.info("Objectives %s", objectives)
    except (referrors.ObjectiveError) as e:
        app.logger.error("[Error] %s | %s", e, traceback.format_exc())
        return flask.jsonify("ObjectiveError: " + str(e)), 400, {'Content-Type': 'application/json'}

    try:
        loadingdata = time.time() - start_time
        app.logger.info("Time loading : %s s", loadingdata)

        start_time = time.time()
        recommendations, directory = data.getRecommendation(
            referential, profile, objectives, STRATEGIES[nameSP]["objects"], STRATEGIES[nameSP]["idSPobject"])

        recodata = time.time() - start_time
        app.logger.info("Time api : %s s", recodata)
    except (pserrors.PropertyObjectError, referrors.NodeObjectError, referrors.NodeProfileObjectError, referrors.ObjectiveError, referrors.NotAReferential) as e:
        app.logger.error("[Error] %s | %s", e, traceback.format_exc())
        return flask.jsonify("RecommendationError: " + str(e)), 400, {'Content-Type': 'application/json'}
    except Exception as e:
        app.logger.error("[Error] %s | %s", e, traceback.format_exc())
        return flask.jsonify("RecommendationError: " + str(e)), 520, {'Content-Type': 'application/json'}

    # Store information in api.json file to trace it
    recommendations_data = {"user": user,
                            "fwid": fwid,
                            "dateReco": directory.split("/")[-2],
                            "api": recommendations,
                            "nb": len(recommendations)}
    data.completeLogConsultation(recommendations_data, "api.json")

    app.logger.info("Total res : %s", len(recommendations))
    if (sendTraces):
        app.logger.info("TRACES REQUESTED")
        traceFile = open(f"{directory}trace_algo_{directory.split('/')[-2]}.trace", encoding='utf-8')
        traces = traceFile.read()
        traceFile.close()
        dict = {"recommandation": recommendations, "traces": traces}
        return flask.jsonify(dict), 200, {'Content-Type': 'application/json', 'X-Date': directory.split("/")[-2]}
    else:
        return flask.jsonify(recommendations), 200, {'Content-Type': 'application/json', 'X-Date': directory.split("/")[-2]}


@api.route("/generateFromProfile/", methods=['POST'])
@api.route("/generateFromProfile/<nameSP>/", methods=['POST'])
def generate_recommendation_from_profile(nameSP=""):
    global referential, id_defaultSP, STRATEGIES

    # ============================== SP ==============================
    # gestion de la SP
    if nameSP == "":
        nameSP = id_defaultSP
    app.logger.info(f"Generate recommendations with strategy named {nameSP}")

    # we reload SP if needed
    try:
        STRATEGIES = data.loadStrategy(STRATEGIES, nameSP)
    except Exception as e:
        app.logger.error(f"[Error] {e} | {traceback.format_exc()}")
        return flask.jsonify(f"Error: {e}"), 410, {'Content-Type': 'application/json'}
    # ================================================================

    result = getTokenDictionary(request.headers.get("Authorization"))
    if result["code"] != 200:
        return flask.jsonify(result["data"]), result["code"], {'Content-Type': 'application/json'}
    datas = result["data"]

    # we check the data inside the token
    try:
        user = datas["user"]
        # role = data["role"]
        username = datas["username"]
        fwid = datas["fwid"]
        # exp = data["exp"]
    except Exception as e:
        app.logger.error(f"[Error] {e} | {traceback.format_exc()}")
        return flask.jsonify(f"Error: {e}"), 498, {'Content-Type': 'application/json'}

    try:
        if (datas["objectives"][-1][0] == "sendTraces"):
            objectives = datas["objectives"][:-1]
            sendTraces = True
        else:
            objectives = datas["objectives"]
            sendTraces = False
    except Exception as e:
        app.logger.error(f"[Error]{e} | {traceback.format_exc()}")
        objectives = []

    if objectives == []:
        return flask.jsonify([]), 200, {'Content-Type': 'application/json', 'X-Date': ""}

    app.logger.info(f"Generating for {datas}")

    start_time = time.time()
    # we check if the current referential is the one we have to use
    try:
        profile_data = request.get_json()
        # print("-----------------------------------KEYS!---------------------------------------:",profile_data.keys())
        # print(profile_data["objects"][0].keys())
        if referential.name != f"Framework-{fwid}":
            referential = data.reloadReferential(fwid, profile_data)

        # we create the profile object
        profile_values = apiFunctions.parseProfileValues(
            referential, profile_data)
        profile = data.loadProfile(referential, profile_values)

        profile.user = user
        profile.username = username
        profile.profile_data_api = profile_data.copy()

    except EnvironmentError as e:
        app.logger.error(f"[ProfileError] {e} | {traceback.format_exc()}")
        return flask.jsonify(f"ProfileError: {e}"), 504, {'Content-Type': 'application/json'}

    except (pserrors.PropertyObjectError, referrors.NodeObjectError, referrors.NodeProfileObjectError, referrors.ObjectiveError, referrors.NotAReferential) as e:
        app.logger.error(f"[ProfileError] {e} | {traceback.format_exc()}")
        return flask.jsonify(f"ProfileError: {e}"), 400, {'Content-Type': 'application/json'}

    except Exception as e:
        app.logger.error(f"[ProfileError] {e} | {traceback.format_exc()}")
        return flask.jsonify(f"ProfileError: {e}"), 520, {'Content-Type': 'application/json'}

    try:
        SPObjectivesParam = apiFunctions.getStrategyObjectivesParameters(
            STRATEGIES, nameSP)
        objectives = (data.loadObjectives(
            profile, SPObjectivesParam, objectives))
        app.logger.info(f"Objectives {objectives}")

    except (referrors.ObjectiveError) as e:
        app.logger.error(f"[ObjectiveError] {e} | {traceback.format_exc()}")
        return flask.jsonify(f"ObjectiveError: {e}"), 400, {'Content-Type': 'application/json'}

    try:
        loadingdata = time.time() - start_time
        app.logger.info(f"Time loading : {loadingdata} s")

        start_time = time.time()
        recommendations, directory = data.getRecommendation(
            referential, profile, objectives, STRATEGIES[nameSP]["objects"], STRATEGIES[nameSP]["idSPobject"])

        recodata = time.time() - start_time
        app.logger.info(f"Time api : {recodata} s")

    except (pserrors.PropertyObjectError, referrors.NodeObjectError, referrors.NodeProfileObjectError, referrors.ObjectiveError, referrors.NotAReferential) as e:
        app.logger.error(
            f"[RecommendationError] {e} | {traceback.format_exc()}")
        return flask.jsonify("[RecommendationError]: " + str(e)), 400, {'Content-Type': 'application/json'}

    except Exception as e:
        app.logger.error(
            f"[RecommendationError] {e} | {traceback.format_exc()}")
        return flask.jsonify("[RecommendationError]: " + str(e)), 520, {'Content-Type': 'application/json'}

    # Store information in api.json file to trace it
    recommendations_data = {"user": user,
                            "fwid": fwid,
                            "dateReco": directory.split("/")[-2],
                            "api": recommendations,
                            "nb": len(recommendations)}
    data.completeLogConsultation(recommendations_data, "api.json")

    app.logger.info(f"Total res : {len(recommendations)}")
    if (sendTraces):
        app.logger.info("TRACES REQUESTED")
        traceFile = open(
            f"{directory}trace_algo_{directory.split('/')[-2]}.trace", encoding='utf-8')
        traces = traceFile.read()
        traceFile.close()
        dict = {"recommandation": recommendations, "traces": traces}
        return flask.jsonify(dict), 200, {'Content-Type': 'application/json', 'X-Date': directory.split("/")[-2]}
    else:
        return flask.jsonify(recommendations), 200, {'Content-Type': 'application/json', 'X-Date': directory.split("/")[-2]}
