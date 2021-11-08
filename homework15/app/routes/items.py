from flask import request
from flask_api import status
from flask_api.exceptions import NotFound
from flask_login import current_user, login_required

from app import app, db
from app.models import Item


@app.route('/items/', methods=['GET', 'POST'])
@login_required
def all_item_requests_handler():
    if request.method == 'GET':
        return [item.to_json() for item in current_user.items]
    else:
        user_input = request.get_json()
        item = Item(
            user_id=current_user.id,
            title=user_input['title'],
            amount=user_input['amount'],
            price=user_input['price'],
        )
        db.session.add(Item)
        db.session.commit()
        return item.to_json(), status.HTTP_201_CREATED


@app.route('/items/<int:item_id>/', methods=['GET', 'PUT', 'DELETE'])
@login_required
def single_pray_request_handler(item_id):
    item: Item = Item.query.get(item_id)
    if item is None or item.user != current_user:
        raise NotFound('Not found pray request')
    if request.method == 'GET':
        response_data = item.to_json()
    elif request.method == 'PUT':
        user_input = request.get_json()
        item.amount = user_input['message']
        item.price = user_input['is_show']
        db.session.commit()
        response_data = item.to_json()
    else:
        db.session.delete(item)
        db.session.commit()
        response_data = {'message': 'Successful deleted pray request'}
    return response_data
