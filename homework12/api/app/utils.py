import json

from flask_api import exceptions


def get_pray_index_or_404(data, pray_id):
    for i in range(len(data)):
        if data[i]['id'] == pray_id:
            return i
    raise exceptions.NotFound('Not found pray request!')


def pray_to_json(item):
    return {
        'id': item['id'],
        'message': item['message'],
    }


def get_user_input_json(data):
    return json.loads(data)