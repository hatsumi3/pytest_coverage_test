import pytest

from app import app

@pytest.fixture()
def client():
    app.config['TESTING'] = True
    test_client = app.test_client() 
    yield test_client
    test_client.delete()

def test_index(client):
    got = client.get("/")
    assert got.status_code == 200
    assert got.data == b'hello, world'

def test_notfound(client):
    got = client.get("/404")
    assert got.status_code == 404

