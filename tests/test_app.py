from flask import Flask

import os

import pytest

from handlers.routes import configure_routes
from database.database import init_app, init_db

@pytest.fixture
def app():
    app = Flask(__name__, 
        instance_relative_config=True, 
        template_folder="../templates")
    app.config.from_mapping(
        DATABASE=os.path.join(app.instance_path, "shoppinglist.sqlite")
    )
    app.config.from_mapping(
        TESTING=True
    )
    
    init_app(app)
    configure_routes(app)
    # FIXME: copied schema.sql into ./tests/ so that also the testing app finds it. 
    # Replace this with proper app config
    with app.app_context():
        init_db()

    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_homepage_displays(client):
    """When calling the default route the homepage should return."""

    res = client.get("/")
    assert res.status_code == 200
    assert b'Currently the list contains the following:' in res.data

def test_add_item(client):
    """When adding an item it should be in the list afterwards."""

    res = client.post('/addentry', data={"value": "Bananas"})
    assert res.status_code == 302

    res = client.get("/")
    assert res.status_code == 200
    assert b'Bananas' in res.data
