from flask import Flask
from redis import Redis, RedisError
from redis import ConnectionError

app = Flask(__name__)
redis_client = Redis()  # Global redis client
import unittest.mock

from redis import ConnectionError

# ...

@unittest.mock.patch("page_tracker.app.redis")
def test_should_handle_redis_connection_error(mock_redis, http_client):
    # Given
    mock_redis.return_value.incr.side_effect = ConnectionError

    # When
    response = http_client.get("/")

    # Then
    assert response.status_code == 500
    assert response.text == "Sorry, something went wrong \N{thinking face}"

@app.get("/")
def index():
    try:
        page_views = redis_client.incr("page_views")
    except RedisError:
        app.logger.exception("Redis error")
        return "Sorry, something went wrong \N{thinking face}", 500
    else:
        return f"This page has been seen {page_views} times."


# Two blank lines here
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
