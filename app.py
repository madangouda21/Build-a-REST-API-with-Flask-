# app.py

from flask import Flask, jsonify, request
import user_service

app = Flask(__name__)

@app.route('/users', methods=['GET'])
def get_users():
    users = user_service.get_all_users_service()
    return jsonify(users)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = user_service.get_user_by_id_service(user_id)
    if user:
        return jsonify(user)
    return jsonify({'error': 'User not found'}), 404

@app.route('/users', methods=['POST'])
def create_user():
    user_data = request.json
    new_user = user_service.create_user_service(user_data)
    if new_user:
        return jsonify(new_user), 201
    return jsonify({'error': 'Invalid user data'}), 400

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user_data = request.json
    updated_user = user_service.update_user_service(user_id, user_data)
    if updated_user:
        return jsonify(updated_user)
    return jsonify({'error': 'User not found'}), 404

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    deleted_user = user_service.delete_user_service(user_id)
    if deleted_user:
        return jsonify({'message': f'User {user_id} deleted successfully'})
    return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)