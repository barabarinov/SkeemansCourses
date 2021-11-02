import json

from flask_api import exceptions
from werkzeug.security import check_password_hash

from app.models import User
from app.storage import get_users_data


def get_item_index_or_404(data, item_id):
    for i in range(len(data)):
        if data[i]['id'] == item_id:
            return i
    raise exceptions.NotFound('Item not found!')


def item_to_json(item):
    return {
        'id': item['id'],
        'title': item['title'],
        'amount': item['amount'],
        'price': item['price'],
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
        if user['username'] == username:
            if check_password_hash(user['password'], password):
                return User(**user)
            else:
                return None
    return None
