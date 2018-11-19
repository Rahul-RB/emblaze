import pytest
import pytest_flask
from emblaze import app
from flask import url_for
from io import BytesIO

class TestApp:

    def test_index(self, client):
        res = client.get(url_for('home'))
        assert res.status_code == 200
    
