import json
from functools import wraps

from flask import request
from flask_api import exceptions
from flask_login import current_user
from flask_login.config import EXEMPT_METHODS
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


def item_to_regular_user_json(item):
    return {
        'id': item['id'],
        'title': item['title'],
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


def admin_required(func):
    from app import app
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if request.method in EXEMPT_METHODS:
            return func(*args, **kwargs)
        elif app.config.get('LOGIN_DISABLED'):
            return func(*args, **kwargs)
        elif not current_user.is_authenticated or not current_user.is_admin:
            return app.login_manager.unauthorized()
        return func(*args, **kwargs)

    return decorated_view
