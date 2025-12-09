import os
import sqlite3
import pytest
from user_editing import app

DB_PATH = 'people.db'

@pytest.fixture(scope="module", autouse=True)
def setup_db():
    # Ensure DB exists before tests
    assert os.path.exists(DB_PATH), "people.db not found. Run createDB.py and insert_recs.py first."
    yield

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

def test_revise_access_existing_user(client):
    resp = client.get('/revise?username=George_Washington')
    assert resp.status_code == 200
    data = resp.get_json()
    assert "user" in data
    assert data["user"]["username"] == "George_Washington"

def test_revise_access_non_existing_user(client):
    resp = client.get('/revise?username=Not_A_User')
    assert resp.status_code == 404
    data = resp.get_json()
    assert "error" in data

def test_revise_update_auth_existing_user(client):
    resp = client.get('/revise?username=John_Adams&auth=2')
    assert resp.status_code == 200
    data = resp.get_json()
    assert data["message"] == "Authorization updated"
    assert data["user"]["username"] == "John_Adams"
    assert data["user"]["auth"] == 2

def test_revise_update_auth_non_existing_user(client):
    resp = client.get('/revise?username=Fake_User&auth=3')
    assert resp.status_code == 404
    data = resp.get_json()
    assert "error" in data
