from flask import Flask, jsonify, request
from data_dict_simple import simple

app = Flask(__name__)

# routes  CRUD operationer  GET, POST, PUT, PATCH, DELETE

@app.route('/students')
def read_all():
    return jsonify(simple)

@app.route('/students', methods=['POST'])
def create():
    data = request.get_json()
    simple.append(data)
    return jsonify(simple)

app.run(debug=True)