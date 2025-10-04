from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
	"""
    A simple Flask route that returns a 'Hello World!' string.

    Returns:
        A string 'Hello World!'.
    """
	return "Hello World!"

@app.route('/cache-me')
def cache():
	"""
    A simple Flask route that returns a string that can be cached by Nginx.

    Returns:
        A string 'nginx will cache this response'.
    """
	return "nginx will cache this response"

@app.route('/info')
def info():
	"""
    A Flask route that returns information about the request headers.

    Returns:
        A JSON response containing the client's IP address, the proxy's IP address,
        the host, and the user agent.
    """
	resp = {
		'connecting_ip': request.headers['X-Real-IP'],
		'proxy_ip': request.headers['X-Forwarded-For'],
		'host': request.headers['Host'],
		'user-agent': request.headers['User-Agent']
	}

	return jsonify(resp)

@app.route('/flask-health-check')
def flask_health_check():
	"""
    A simple health check endpoint for the Flask application.

    Returns:
        A string 'success'.
    """
	return "success"
