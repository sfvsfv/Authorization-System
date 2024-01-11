from flask import Blueprint, request, jsonify
import json
import os

auth_verifier_blueprint = Blueprint('auth_verifier', __name__)
AUTH_FILE = 'data/auth-codes.json'

def read_auth_codes():
    if not os.path.exists(AUTH_FILE):
        return {}
    with open(AUTH_FILE, 'r') as file:
        return json.load(file)

@auth_verifier_blueprint.route('/')
def verify():
    codes = read_auth_codes()
    ip = request.args.get('ip')
    code = codes.get(ip)

    if code:
        return jsonify({'valid': True, 'code': code})
    else:
        return jsonify({'valid': False}), 404