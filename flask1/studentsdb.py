import sqlite3
from data_dict import random_users
import requests

def create():
    with sqlite3.connect('members.db') as conn:
        cur = conn.cursor()
        cur.execute ('''CREATE TABLE IF NOT EXISTS members (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    birth_date TEXT NOT NULL,
    gender TEXT NOT NULL,
    email TEXT NOT NULL,
    phonenumber TEXT,
    address TEXT,
    nationality TEXT,
    active INTEGER,
    github_username TEXT)''')
        
        cur.executemany('''
            INSERT INTO members (first_name, last_name, birth_date, gender, email, phonenumber, address, nationality, active, github_username)
            VALUES(:first_name,:last_name,:birth_date,:gender,:email,:phonenumber,:address,:nationality,:active,:github_username)
        ''', random_users)

def fetch_github_repos(username, is_me=False):
    url = f'https://api.github.com/users/{username}/repos'
    headers = {}
    if is_me:
        headers['Authorization'] = 'Your_Github_Token'

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        repos = response.json()
        return [{'name': repo['name'], 'url': repo['html_url']} for repo in repos]
    elif response.status_code == 401:  # Unauthorized access
        return {'error': 'Unauthorized - Check your GitHub credentials'}
    elif response.status_code == 404:  # User not found
        return {'error': 'GitHub user not found'}
    return {'error': 'Failed to fetch GitHub repos'}

def read():

    members = []

    with sqlite3.connect('members.db') as conn:
        cur = conn.cursor()
        cur.execute('SELECT * FROM members')

        for i in cur:
            members.append({
                'id': i[0],
                'first_name': i[1],
                'last_name': i[2],
                'birth_date': i[3],
                'gender': i[4],
                'email': i[5],
                'phonenumber': i[6],
                'address': i[7],
                'nationality': i[8],
                'active': i[9],
                'github_username': i[10],
            })

    return members