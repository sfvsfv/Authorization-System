from flask import Blueprint, request, jsonify
import json
import os

auth_manager_blueprint = Blueprint('auth_manager', __name__)
AUTH_FILE = 'auth-codes.json'

# 辅助函数：读取授权码
def read_auth_codes():
    if not os.path.exists(AUTH_FILE):
        return {}
    with open(AUTH_FILE, 'r') as file:
        return json.load(file)

# 辅助函数：写入授权码
def write_auth_codes(codes):
    with open(AUTH_FILE, 'w') as file:
        json.dump(codes, file, indent=2)

@auth_manager_blueprint.route('/auth-code', methods=['POST', 'DELETE'])
def manage_auth_code():
    codes = read_auth_codes()
    ip = request.json.get('ip')
    code = request.json.get('code')

    if request.method == 'POST':
        codes[ip] = code
        write_auth_codes(codes)
        return jsonify({'message': f'Auth code for IP {ip} updated.'}), 200

    if request.method == 'DELETE':
        del codes[ip]
        write_auth_codes(codes)
        return jsonify({'message': f'Auth code for IP {ip} deleted.'}), 200
