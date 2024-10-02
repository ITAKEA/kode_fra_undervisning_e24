from flask import Flask, jsonify, request
from data_dict_simple import simple
import sqlite3
from data_dict import random_users
from studentsdb import read, fetch_github_repos



app = Flask(__name__)

@app.route('/members')
def read_all():
    members = read()
    for member in members:
        github_username = member.get('github_username')
        if github_username:
            if github_username == 'ViktorBach':
                member['github_repos'] = fetch_github_repos(github_username, is_me=True)
            else:
                member['github_repos'] = fetch_github_repos(github_username, is_me=False)
    return jsonify(read())


@app.route('/members/', methods=['POST'])
def creator():
    data = request.get_json()
    read().append(data)
    
    return jsonify(message='Created'), 201

@app.route('/members/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    with sqlite3.connect('members.db') as conn:
        cur = conn.cursor()
        cur.execute('DELETE FROM members WHERE id = ?', (member_id,))
        conn.commit()
    return jsonify(message=f'Member {member_id} deleted'), 200

@app.route('/members/<int:member_id>', methods=['PUT'])
def update_member(member_id):
    data = request.get_json()
    with sqlite3.connect('members.db') as conn:
        cur = conn.cursor()
        cur.execute('''
            UPDATE members SET first_name=?, last_name=?, birth_date=?, gender=?, email=?, phonenumber=?, address=?, nationality=?, active=?, github_username=?
            WHERE id=?
        ''', (
            data['first_name'], data['last_name'], data['birth_date'], 
            data['gender'], data['email'], data.get('phonenumber'),
            data.get('address'), data.get('nationality'), 
            data.get('active', 1), data.get('github_username'), member_id
        ))
        conn.commit()
    return jsonify(message=f'Member {member_id} updated'), 200

@app.route('/members/<int:member_id>', methods=['PATCH'])
def partial_update_member(member_id):
    data = request.get_json()

    query = 'UPDATE members SET '
    query_params = []
    for key, value in data.items():
        if key != 'id':  # Ensure we don't try to update the 'id'
            query += f'{key} = ?, '
            query_params.append(value)

    # Remove the trailing comma and space from the query
    query = query.rstrip(', ')
    query += ' WHERE id = ?'
    query_params.append(member_id)

    # Perform the update in the database
    with sqlite3.connect('members.db') as conn:
        cur = conn.cursor()
        cur.execute(query, query_params)
        conn.commit()

    return jsonify(message=f'Member {member_id} partially updated'), 200

app.run(app.run(host="0.0.0.0"), debug=True, port=5001)