import pytest
import redis

from page_tracker.app import app 

def pytest_addoption(parser):
    parser.addoption("--flask-url", required=True)
    parser.addoption("--redis-url", required=True)

@pytest.fixture(scope="session")
def flask_url(request):
    return request.config.getoption("--flask-url")

@pytest.fixture(scope="session")
def redis_url(request):
    return request.config.getoption("--redis-url")

# ... (other fixtures)
