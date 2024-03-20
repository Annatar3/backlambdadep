import awsgi
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/')
def index():
    return jsonify(status=200, message='Backend: You are viewing the backend.')

@app.route('/api/request', methods=['GET'])
def send_request():
    # Add any necessary logic here
    return jsonify(status=200, message='200 OK')

def lambda_handler(event, context):
    return awsgi.response(app, event, context)

