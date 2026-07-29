import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src', 'fixed'))

from app import app as flask_app


@pytest.fixture
def client():
    flask_app.config['TESTING'] = True

    with flask_app.test_client() as client:
        yield client
