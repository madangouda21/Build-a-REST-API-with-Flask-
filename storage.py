# storage.py

users_data = {}
next_user_id = 1

def get_all_users():
    return list(users_data.values())

def get_user_by_id(user_id):
    return users_data.get(user_id)

def create_user(user_data):
    global next_user_id
    user_id = next_user_id
    user_data['id'] = user_id
    users_data[user_id] = user_data
    next_user_id += 1
    return user_data

def update_user(user_id, updated_data):
    if user_id in users_data:
        users_data[user_id].update(updated_data)
        users_data[user_id]['id'] = user_id  # Ensure ID is not changed
        return users_data[user_id]
    return None

def delete_user(user_id):
    return users_data.pop(user_id, None)