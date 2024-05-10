#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys

import jwt
import requests

from ..logger import loggering
# from api.consts import REP_SP
from ..pedagogicStrategy import ioStrategy, strategyObjects
from .consts import DATA_PATH


REP_SP = DATA_PATH + "PS/"

logger = loggering.getLogger()
sys.path.append("..")


def getAllPubKeys():
    pubfiles = [f for f in os.listdir("./resources/rsaKeys/")
                if os.path.isfile(os.path.join("./resources/rsaKeys/", f)) and ".pub" in f]

    pubKeys = []
    for name in pubfiles:
        f = open("./resources/rsaKeys/" + name, "r")
        pubKeys.append("".join(f.readlines()))
        f.close()

    return pubKeys, pubfiles


def decodeToken(token_jwt):
    is_decoded = False

    pubKeys, pubfiles = getAllPubKeys()

    for pubKey, file in zip(pubKeys, pubfiles):
        try:
            data = jwt.decode(token_jwt, pubKey, algorithms=["RS256"])
        except jwt.exceptions.ExpiredSignatureError as e:
            logger.error(e)
            error = 498
            return {"data": f"Error {error}: {e}", "code": error}
        except jwt.exceptions.DecodeError as e:  # we can't decode it
            logger.debug("Decoding fail using %s. Error: %s", file, e)
            pass
        except jwt.exceptions.InvalidTokenError as e:
            logger.debug(f"Invalid Token {file}. {e}")
            error = 498
            return {"data": f"Error {error}: Invalid token. {e}", "code": error}
        except Exception as e:
            logger.debug("Not expected error with file %s.Error: %s", file, e)
            error = 456
            return {"data": f"Error: {error}. Not Expected error{e}", "code": error}
        else:
            logger.debug("Decode using file %s", file)
            is_decoded = True
            break

    if not is_decoded:
        error = 403
        return {"data": f"Error {error}: No Authorization", "code": error}
    return {"data": data, "code": 200}


def getAllStrategy():
    # we get all SP files created
    SPfiles = [f.split(".json")[0] for f in os.listdir(
        REP_SP) if os.path.isfile(os.path.join(REP_SP, f))]
    SPfiles_filtered = [
        name for name in SPfiles if '@' not in name and name[0] != "n"]

    return SPfiles_filtered


def getAllStrategyDetail():
    SPfiles = getAllStrategy()
    SPdetails = []
    for file in SPfiles:
        SP_obj = ioStrategy.createSPObjectFromFile(
            os.path.join(REP_SP, file + ".json"))
        data = {"id": SP_obj.id,
                "name": SP_obj.name,
                "authors": SP_obj.authors,
                "description": SP_obj.description,
                "version": SP_obj.version,
                "type": SP_obj.type,
                "public_visibility": SP_obj.public_visibility}
        SPdetails.append(data)

    return SPdetails


def requestProfileAPI(arguments, fwid, username):

    req = arguments["profile_ip"] + arguments["profile_path"] + "?frameworkId=" + str(fwid) + "&learnerUsername=" + str(username).replace("-", "").replace(" ", "")
    my_headers = {"x-comper-accepted-host": "https://traffic.irit.fr"}
    profile_request = requests.get(req, headers=my_headers)

    logger.info("%s Parameters :%s | Return error code:  %s ",
                req, my_headers, profile_request.status_code)
    # pprint.pprint(profile_request.json())
    if profile_request.status_code != 200:
        logger.warning(profile_request.text)
        logger.warning("connection impossible (HTTP_%s) to %s",
                       str(profile_request.status_code), req)
        raise EnvironmentError(
            "connection impossible (HTTP_" + str(profile_request.status_code) + ") to " + req)

    profile_data = profile_request.json()

    return profile_data


def parseProfileValues(referential, profile_data):
    profileValues = {}
    # we parse Nodes
    for obj in profile_data["objects"]:
        # print("obj keys :",obj.keys())
        # print("obj name :",obj["name"])
        if obj["name"] not in profileValues.keys():
            profileValues[obj["name"]] = [
                str(obj["mastery"]), str(obj["trust"]), str(obj["cover"])]

    return profileValues


def getStrategyObjectivesParameters(STRATEGIES, nameSP):
    strategy_objects = STRATEGIES[nameSP]["objects"]
    # id_strategy = STRATEGIES[nameSP]["idSPobject"]

    # get SP_obj
    SP_obj = None
    i = 0
    while i < len(strategy_objects) and SP_obj is None:
        id_obj = list(strategy_objects.keys())[i]
        if strategyObjects.PedagogicStrategy.isAPedagogicStrategy(strategy_objects[id_obj]):
            SP_obj = strategy_objects[id_obj]
        i += 1

    return SP_obj.getObjectiveParameters()
