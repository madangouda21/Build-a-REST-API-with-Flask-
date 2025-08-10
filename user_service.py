# user_service.py

import storage

def get_all_users_service():
    return storage.get_all_users()

def get_user_by_id_service(user_id):
    return storage.get_user_by_id(user_id)

def create_user_service(user_data):
    if 'name' not in user_data:
        return None
    return storage.create_user(user_data)

def update_user_service(user_id, updated_data):
    if not storage.get_user_by_id(user_id):
        return None
    return storage.update_user(user_id, updated_data)

def delete_user_service(user_id):
    return storage.delete_user(user_id)