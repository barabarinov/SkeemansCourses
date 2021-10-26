import json
from flask import Flask, request, Response
from flask_api import status


app = Flask(__name__)


def get_data():
    with open('storage.json', 'r') as f:
        return json.load(f)


def store_data(data):
    with open('storage.json', 'w') as f:
        json.dump(data, f)


@app.route('/items/', methods=['GET'])
def get_items():
    # import ipdb; ipdb.set_trace()
    return Response(
        json.dumps(get_data()),
        mimetype='application/json',
    )


@app.route('/items/<int:item_id>/', methods=['POST'])
def create_item(item_id):
    # import ipdb;
    # ipdb.set_trace()
    data = get_data()
    # print(request.get_json())
    latest_id = max([msg['id'] for msg in data], default=0) + 1
    data.append({
        'id': latest_id,
        'message': request.get_json()['message'],
        'amount': request.get_json()['amount'],
    })
    store_data(data)
    return Response(
        json.dumps({
            'item_id': latest_id,
        }),
        mimetype='application/json',
    )


@app.route('/pet_shop/<int:item_id>/', methods=['GET'])
def get_item(pet_id):
    data = get_data()
    for i in range(len(data)):
        if data[i]['id'] == pet_id:
            return Response(
                json.dumps(data[i]),
                mimetype='application/json',
            )
        break
    else:
        return Response('The pet not found', status=404)


@app.route('/pet_shop/<int:item_id>/', methods=['PUT'])
def update_item(item_id):
    data = get_data()
    for i in range(len(data)):
        pet_shop = data[i]
        if data[i]['id'] == item_id:
            data[i]['message'] = request.get_json()['message']
            data[i]['amount'] = request.get_json()['amount']
            store_data(data)
            break
    else:
        return Response('The item not found', status=404)
    return Response(
        json.dumps(pet_shop),
        status=200,
        mimetype='application/json',
    )


@app.route('/pet_shop/<int:item_id>/', methods=['DELETE'])
def remove_item(item_id):
    data = get_data()
    for i in range(len(data)):
        if data[i]['id'] == item_id:
            del data[i]
            store_data(data)
            return Response(status=204)
    return Response('The item not found!', status=404)


# if __name__ == '__main__':
#     app.run(debug=True)
