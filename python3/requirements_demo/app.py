# Dette er det samme kode som i app.ipynb, forskellen er bare filformatet.

from data import persons
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return jsonify(persons)

if __name__ == "__main__":
    app.run()