import sys
from os.path import abspath
from os.path import dirname as d
from os.path import join

import pytest
from config import Config

root_dir = join(d(d(abspath(__file__))), 'src')
sys.path.append(root_dir)


@pytest.fixture()
def app():
    from main import create_app
    app = create_app(Config)
    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
