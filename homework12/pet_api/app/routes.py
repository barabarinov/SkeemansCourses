from flask import request
from flask_api import status
from flask_login import logout_user, login_user, current_user
from werkzeug.security import generate_password_hash


from app import app
from app.models import User
from app.storage import get_data, store_data, get_users_data, store_users_data
from app.utils import get_item_index_or_404, item_to_json, get_user_input_json
from app.utils import get_user_by_username_and_password, admin_required, item_to_regular_user_json


@app.route('/login/', methods=['POST'])
def login():
    info = request.get_json()
    username = info['username']
    password = info['password']
    admin = get_user_by_username_and_password(username, password)
    if admin is not None:
        login_user(admin)
        return admin.to_json()
    else:
        return {"reason": "Username or password are incorrect"}, status.HTTP_401_UNAUTHORIZED


@app.route('/logout/', methods=['POST'])
def logout():
    logout_user()
    return {"message": "Logout success!"}


@app.route('/register/', methods=['POST'])
def register():
    users_data = get_users_data()
    request_data = request.get_json()
    user_data_to_save = {
        'id': max([msg['id'] for msg in users_data], default=0) + 1,
        'username': request_data['username'],
        'password': generate_password_hash(request_data['password']),
        'first_name': request_data['first_name'],
        'last_name': request_data['last_name'],
        'age': request_data['age'],
    }
    users_data.append(user_data_to_save)
    store_users_data(users_data)
    user = User(**user_data_to_save)
    logout_user()
    return user.to_json(), status.HTTP_201_CREATED


@app.route('/items/', methods=['GET'])
def get_all_items_requests_handler():
    data = get_data()
    if current_user.is_anonymous:
        return [item_to_regular_user_json(item) for item in data]
    else:
        return [item_to_json(item) for item in data]


@app.route('/items/<int:item_id>/', methods=['GET'])
def get_single_item_request_handler(item_id):
    data = get_data()
    item_index = get_item_index_or_404(data, item_id)
    item_request = data[item_index]
    if current_user.is_anonymous:
        return item_to_regular_user_json(item_request)
    else:
        return item_to_json(item_request)


@app.route('/items/', methods=['POST'])
@admin_required
def post_all_items_requests_handler():
    data = get_data()
    user_data = get_user_input_json(request.get_data())
    item_request = {
        'id': max([msg['id'] for msg in data], default=0) + 1,
        'title': user_data['title'],
        'amount': user_data['amount'],
        'price': user_data['price'],
    }
    data.append(item_request)
    store_data(data)
    return item_to_json(item_request), status.HTTP_201_CREATED


# Endpoints
@app.route('/items/<int:item_id>/', methods=['PUT', 'DELETE'])
@admin_required
def delete_single_item_request_handler(item_id):
    data = get_data()
    item_index = get_item_index_or_404(data, item_id)
    item_request = data[item_index]
    if request.method == 'PUT':
        user_data = get_user_input_json(request.get_data())
        item_request['title'] = user_data['title']
        item_request['amount'] = user_data['amount']
        item_request['price'] = user_data['price']
        store_data(data)
        return item_to_json(item_request)
    else:
        del data[item_index]
        store_data(data)
        return None, status.HTTP_204_NO_CONTENT


@app.route('/items/buy/<int:item_id>/', methods=['POST'])
@admin_required
def buy_one_item(item_id):
    data = get_data()
    item_index = get_item_index_or_404(data, item_id)
    if data[item_index]['amount'] <= 0:
        return {'message': 'Out of stock!'}, status.HTTP_400_BAD_REQUEST
    data[item_index]['amount'] -= 1
    store_data(data)
    return item_to_json(data[item_index])


@app.route('/items/calculate/', methods=['GET'])
@admin_required
def sum_of_prices():
    data = get_data()
    result = 0
    for item in data:
        if item['amount'] > 0:
            result += item['amount'] * item['price']
    return {'message': f'Sum of all prices of items = {result}'}
