import pytest
import redis
import requests

from page_tracker.app import app

@pytest.fixture(scope="function")
def redis_client(redis_url):
    if redis_url:
        return redis.Redis.from_url(redis_url)
    return redis.Redis()

@pytest.mark.timeout(1.5)
def test_should_update_redis(redis_client, flask_url):
    # Given
    redis_client.set("page_views", 4)

    # When
    response = requests.get(flask_url)

    # Then
    assert response.status_code == 200
    assert response.text == "This page has been seen 5 times."
    assert redis_client.get("page_views") == b"5"
