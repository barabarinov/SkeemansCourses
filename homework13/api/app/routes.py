from flask import request
from flask_api import status
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash


from app import app
from app.models import User
from app.storage import get_data, store_data, get_users_data, store_users_data
from app.utils import get_pray_index_or_404, pray_to_json, get_user_input_json, get_user_by_username_and_password


@app.route('/login/', methods=['POST'])
def login():
    info = request.get_json()
    username = info['username']
    password = info['password']
    user = get_user_by_username_and_password(username, password)
    if user is not None:
        login_user(user)
        return user.to_json()
    else:
        return {"reason":"Username or password are incorrect"}, status.HTTP_401_UNAUTHORIZED


@app.route('/logout', methods=['POST'])
def logout():
    logout_user()
    return {"message":"logout success"}


@app.route('/register/', methods=['POST'])
def register():
    users_data = get_users_data()
    request_data = request.get_json()
    user_data_to_save = {
        "id": max([msg['id'] for msg in users_data], default=0) + 1
        "username": request_data['username'],
        "password": generate_password_hash(request_data['password']),
        "first_name": request_data['first_name'],
        "last_name": request_data['last_name'],
        "age": request_data['age'],
    }
    users_data.append(user_data_to_save)
    store_users_data(users_data)
    user = User(**user_data_to_save)
    logout_user(user)
    return user.to_json(), status.HTTP_201_CREATED


@app.route('/user-info/', methods=['GET'])
def user_info():
    if current_user.is_authenticated:
        return current_user.to_json()
    else:
        return {"message": "user not logged in"}, status.HTTP_401_UNAUTHORIZED


@app.route('/users/', methods=['GET'])
def get_users():
    return [User(**user_data).to_json() for user_data in get_users_data()]


@app.route('/pray-requests/', methods=['GET', 'POST'])
@login_required
def all_pray_requests_handler():
    data = get_data()
    if request.method == 'GET':
        return [pray_to_json(item) for item in data if item['user_id'] == current_user.id]
    else:
        user_data = get_user_input_json(request.get_data())
        pray_request = {
            "id": max([msg['id'] for msg in data], default=0) + 1
            "user_id": current_user.id,
            "message": user_data['message'],
        }
        data.append(pray_request)
        store_data(data)
        return pray_to_json(pray_request), status.HTTP_201_CREATED


@app.route('/pray-requests/<int:pray_id>/', methods['GET', 'PUT', 'DELETE'])
@login_required
def single_pray_request_handler(pray_id):
    data = get_data()
    pray_index = get_pray_index_or_404(data, pray_id)
    pray_request = data[pray_index]
    if pray_request['user_id'] != current_user.id:
        raise NotFound('Not found pray request')
    if request.method == 'GET':
        return  pray_to_json(pray_request)
    elif request.method == 'PUT':
        user_data = get_user_input_json(request.get_data())
        pray_request["message"] = user_data["message"]
        store_data(data)
        return  pray_to_json(pray_request)
    else:
        del data[pray_index]
        store_data(data)
        return None, status.HTTP_204_NO_CONTENT
