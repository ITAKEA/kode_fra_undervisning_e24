from flask import Flask
import sqlite3
from dotenv import load_dotenv
import os

# Load environment variabler fra .env fil
load_dotenv()

# Opret en Flask app
app = Flask(__name__)

# db_path = os.getenv("DB_PATH", "db.db")

with sqlite3.connect('db.db') as conn:
    pass

@app.route('/')
def index():
    return 'Hello'

app.run(host='0.0.0.0')