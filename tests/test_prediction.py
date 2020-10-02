import math
from unittest.mock import MagicMock, patch

import pytest
from fastapi.testclient import TestClient

from src.app import api


@pytest.fixture
def client():
    return TestClient(api)


@pytest.fixture
def input_data():
    return {'item_id': 1, 'user_id': 1}


def test_ping(client):
    response = client.get('/ping')
    assert response.status_code == 200
    assert response.json() == 'hello'


def test_predict(client, input_data):
    with patch('src.prediction.ModelService.predict', MagicMock(return_value=0.0)):
        response = client.post('/invocations', json=input_data)
        assert response.status_code == 200
        assert math.isclose(response.json().get('result'), 0.0)
