from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = os.getenv('KEY')
jwt = JWTManager(app)

accounts = {
    'test@test.com': {
        'balance': 1000,
        'account_number': '12345678'
    }
}

@app.route('/account/balance', methods=['GET'])
@jwt_required()
def get_balance():
    current_user = get_jwt_identity()
    
    if current_user not in accounts:
        return jsonify({'msg': 'Account not found'}), 404
        
    return jsonify({
        'user': current_user,
        'balance': accounts[current_user]['balance'],
        'account_number': accounts[current_user]['account_number']
    }), 200

if __name__ == '__main__':
    app.run(port=5001, debug=True)
