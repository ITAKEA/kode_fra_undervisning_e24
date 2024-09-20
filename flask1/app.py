from flask import Flask, jsonify, request
from data_dict_simple import simple
from students import read
from data_dict import random_users

app = Flask(__name__)

# routes  CRUD operationer  GET, POST, PUT, PATCH, DELETE

@app.route('/students')
def read_all():
    return jsonify(random_users)

@app.route('/students', methods=['POST'])
def create():
    data = request.get_json()
    simple.append(data)
    return jsonify()

app.run(debug=True)