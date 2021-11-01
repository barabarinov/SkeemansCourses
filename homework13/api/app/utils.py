import json


from flask_api import exceptions
from werkzeug.security import check_password_hash

from app.models import User
from app.storage import get_users_data


def get_pray_index_or_404(data, pray_id):
    for i in range(len(data)):
        if data[i]["id"] == pray_id:
            return i
    raise exceptions.NotFound("Not found pray request")


def pray_to_json(item):
    return {
        "id": item["id"],
        "message": item["message"],
    }

def get_user_input_json(data):
    return json.loads(data)


def get_user(user_id):
    for user in get_users_data():
        if str(user['id']) == user_id:
            return User(**user)
    return None


def get_user_by_username_and_password(username, password):
    for user in get_users_data():
        if user('username') == username:
            if user('password') == password:
                return User(**user)
            else:
                return None
    return None
