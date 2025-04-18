from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from dotenv import load_dotenv # import fra .env fil
import os
import requests
import datetime

# Load environment variables
load_dotenv()

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = os.getenv('KEY')
app.config['JWT_HEADER_TYPE'] = 'token'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = False

jwt = JWTManager(app)

# database
users = {
    'test@test.com': {
        'password': 'password123',
        'role': 'user'
    }
}

@app.route('/login', methods=['POST'])
def login():
    email = request.json.get('email', None)
    password = request.json.get('password', None)

    if not email or not password:
        return jsonify({'msg': 'Missing email or password'}), 400

    user = users.get(email, None)
    if not user or user['password'] != password:
        return jsonify({'msg': 'Incorrect email or password'}), 401

    # Opret token
    token = create_access_token(identity=email)

    return jsonify({
        'access_token': token,
    }), 200

@app.route('/protected', methods=['GET'])
@jwt_required() # alle protecd route
def protected():
    current_user = get_jwt_identity()
    return jsonify({
        'logged_in_as': current_user,
        'msg': 'Du har adgang til denne resourse'
    }), 200

@app.route('/account/info', methods=['GET'])
@jwt_required()
def get_account_info():
    # Get the JWT token from the current request
    token = request.headers.get('Authorization')
    
    # Forward the request to the account service
    response = requests.get(
        'http://localhost:5001/account/balance',
        headers={'Authorization': token}
    )
    
    return jsonify(response.json()), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
