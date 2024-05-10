#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time

import flask
import jwt


IP = "127.0.0.1"
PORT = 3002

app = flask.Flask(__name__)


@app.route("/generateToken/", methods=['GET'])
def generateToken():
    """
    """

    data = {
        "user": "asker:ext_Adam.Hassan",
        "role": "learner",
        "username": "ext_Adam.Hassan",
        "fwid": 83,
        "exp": time.time() + 10000, \
        # "objectives": [], \
        "objectives": [["Ecrire_des_scripts_interactifs", "Revision"]]
    }

    f = open("jwtRS256.key")
    key = "".join(f.readlines())

    f.close()

    jwt_encoded = jwt.encode(data, key, algorithm="RS256")

    return jwt_encoded, 200, {'Content-Type': 'text/plain'}


app.run(host=IP, port=PORT, debug=True, use_reloader=True)
