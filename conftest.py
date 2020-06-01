import pytest
import requests
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

class MockResponse:
    @staticmethod
    def json():
        return {
            "results": [
                {'formatted': '66003845687 Pereira, Colombia',
                 'geometry': {'lat': 51.9526599, 'lng': 7.632473}}
            ]
        }

@pytest.fixture
def mock_response(monkeypatch):
    """requests.get() mocked to return a static response"""

    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)