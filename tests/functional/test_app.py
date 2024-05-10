"""
This file (test_app.py) contains the unit tests for the Flask application.
"""
# Get valid token recognized by reco
import json


def test_ping(test_client):
    landing = test_client.get("/api/")
    html = landing.data.decode()

    assert "Service online" in html
    assert landing.status_code == 200


def test_pedagogicStrategyList(test_client):
    landing = test_client.get("/api/pedagogicStrategy/list/")
    # html = landing.data.decode()
    assert landing.status_code == 200


def test_pedagogicStrategyListDetail(test_client):
    landing = test_client.get("/api/pedagogicStrategy/detailledList/")
    # html = landing.data.decode()
    assert landing.status_code == 200


def test_updateFramework(test_client):
    landing = test_client.put("/api/updateFramework/")
    result = landing.data.decode()

    assert "updateFramework done" in result
    assert landing.status_code == 200


def test_generate_recommendation(test_client, getToken):
    headers = {"Authorization": f"Bearer {getToken}"}
    landing = test_client.post("/api/generate/", headers=headers)
    result = landing.data.decode()
    dico = json.loads(result)

    assert "learning_platform" in result
    assert "learning_type" in dico[0].keys()
    assert landing.status_code == 200


def test_generate_recommendation_from_profile(test_client, getToken, profile):
    headers = {"Authorization": f"Bearer {getToken}", "Content-Type": "application/json"}
    landing = test_client.post("/api/generateFromProfile/", headers=headers, data=json.dumps(profile))
    result = landing.data.decode()
    dico = json.loads(result)

    assert "learning_platform" in result
    assert "learning_type" in dico[0].keys()
    assert landing.status_code == 200


def test_getLastLogFile(test_client, getToken):
    headers = {"Authorization": f"Bearer {getToken}"}
    landing = test_client.get("/api/logs/last/", headers=headers)
    assert landing.status_code == 200


def test_logResourceConsultation(test_client, getToken):
    headers = {"Authorization": f"Bearer {getToken}"}
    landing = test_client.put("/api/logResourceConsultation/", headers=headers)
    assert landing.status_code == 200
