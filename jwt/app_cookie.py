from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, set_access_cookies, unset_jwt_cookies, jwt_required, get_jwt_identity
from dotenv import load_dotenv
import os
from datetime import timedelta

load_dotenv()

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = os.getenv('KEY')
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_COOKIE_SAMESITE'] = 'Lax' 

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

    # Create access token
    access_token = create_access_token(identity=email)

    response = jsonify({
        'msg': 'Login OK',
        'user': email
    })
    
    # cookie
    set_access_cookies(response, access_token)
    
    return response, 200

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify({
        'logged_in_as': current_user,
        'msg': 'You have access to this resource'
    }), 200

@app.route('/logout', methods=['POST'])
def logout():
    response = jsonify({'msg': 'Successfully logged out'})
    unset_jwt_cookies(response)
    return response, 200

if __name__ == '__main__':
    app.run(debug=True)
