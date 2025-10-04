from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    """
    A simple Flask route that increments a Redis counter and returns a message
    displaying the number of times the page has been viewed.

    Returns:
        A string with the number of page views.
    """
    redis.incr('hits')
    counter = str(redis.get('hits'),'utf-8')
    return "This webpage has been viewed "+counter+" time(s)"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
