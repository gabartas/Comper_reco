import json
import os
import time

import jwt
import pytest

from recommandations import create_app


# --------
# Fixtures
# --------


@pytest.fixture(scope='module')
def test_client():
    # Set the Testing configuration prior to creating the Flask application
    os.environ['CONFIG_TYPE'] = 'config.TestingConfig'
    flask_app = create_app()

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as testing_client:
        # Establish an application context
        with flask_app.app_context():
            yield testing_client  # this is where the testing happens!


@pytest.fixture(scope='function')
def log_in_default_user(test_client):
    test_client.post('/login',
                     data={'email': 'patkennedy79@gmail.com', 'password': 'FlaskIsAwesome'})

    yield  # this is where the testing happens!

    test_client.get('/logout')


@pytest.fixture(scope='function')
def log_in_second_user(test_client):
    test_client.post('login',
                     data={'email': 'patrick@yahoo.com', 'password': 'FlaskIsTheBest987'})

    yield   # this is where the testing happens!

    # Log out the user
    test_client.get('/logout')


@pytest.fixture(scope='module')
def cli_test_client():
    # Set the Testing configuration prior to creating the Flask application
    os.environ['CONFIG_TYPE'] = 'config.TestingConfig'
    flask_app = create_app()

    runner = flask_app.test_cli_runner()

    yield runner  # this is where the testing happens!


@pytest.fixture(scope='module')
def getToken():
    data = {
        "user": "asker:ext_Adam.Hassan",
        "role": "learner",
        "username": "ext_Adam.Hassan",
        "fwid": 83,
        "exp": time.time() + 3600,
        "objectives": [["Ecrire_des_scripts_interactifs", "Revision"]]
    }

    key = ""
    with open('tests/private_testing.key', 'r') as f:
        key = "".join(f.readlines())

    token = jwt.encode(data, key, algorithm="RS256")
    print(token)
    return token


@pytest.fixture(scope='function')
def profile():
    profile_file = ""
    with open('tests/profile.json', 'r', encoding='utf-8') as f:
        profile_file = json.load(f)

    return profile_file
