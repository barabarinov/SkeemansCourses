from flask import request
from flask_api import status


from app import app
from app.storage import get_data, store_data
from app.utils import get_pray_index_or_404, pray_to_json, get_user_input_json


@app.route('/pray-requests/', methods=['GET', 'POST'])
def all_pray_requests_handler():
    data = get_data()
    if request.method == 'GET':
        return [pray_to_json(item) for item in data]
    else:
        user_data = get_user_input_json(request.get_data())
        pray_request = {
            'id': max([msg['id'] for msg in data], default=0) + 1,
            'message': user_data['message']
        }
        data.append(pray_request)
        store_data(data)
        return pray_to_json(pray_request), status.HTTP_201_CREATED

#Endpoints
@app.route('/pray-requests/<int:pray_id>/', methods=['GET', 'PUT', 'DELETE'])
def single_pray_request_handler(pray_id):
    data = get_data()
    pray_index = get_pray_index_or_404(data, pray_id)
    pray_request = data[pray_index]
    if request.method == 'GET':
        return pray_to_json(pray_request)
    elif request.method == 'PUT':
        user_data = get_user_input_json(request.get_data())
        pray_request['message'] = user_data['message']
        store_data(data)
        return pray_to_json(pray_request)
    else:
        del data[pray_index]
        store_data(data)
        return None, status.HTTP_204_NO_CONTENT
