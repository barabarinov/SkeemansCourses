import json
from flask import Flask, request, Response

app = Flask(__name__)

def get_data():
    with open('storage_s.py', 'r') as f:
        return json.load(f)


def store_data():
    with open('storage_s.py', 'w') as f:
        return json.dump(f)


@app.route('/pet_shop/', method=['GET'])
def get_a_pets():
    return Response(
        json.dumps(get_data()),
        mimetype='application/json',
    )

@app.route('/pet_shop/', method=['POST'])
def give_the_new_pet(pet):
    data = get_data()
    latest_id = max([msg[id] for msg in data], default=0) + 1
    data.append({
        'id': latest_id,
        'message': request.get_json()['message']
    })
    store_data(data)
    return Response(
        json.dumps({
            'pet_id': latest_id,
        }),
        mimetype='application/json',
    )


@app.route('/pet_shop/<int:pet_id>/', method=['GET'])
def get_a_pet(pet_id):
    data = get_data()
    for i in range(len(data)):
        if data[i]['id'] == pet_id:
            return Response(
                json.dumps(data[i]),
                mimetype='application/json',
            )


@app.route('/pet_shop/<int:pet_id>/', method=['PUT'])
def update_a_pet(pet_id):
    data = get_data()
    for i in range(len(data)):
        pet_shop = data[i]
        if data[i]['id'] == pet_id:
            data[i]['message'] = request.get_json()['message']
            store_data(data)
            break
    else:
        return Response('The pet not found', status=404)
    return Response(
        json.dumps(pet_shop),
        status=200,
        mimetype='application/json',
    )


@app.route('/pet_shop/<int:pet_id>/', method=['DELETE'])
def remove_pet(pet_id):
    data = get_data()
    for i in range(len(data)):
        if data[i]['id'] == pet_id:
            del data[i]
            store_data(data)
            return Response(status=204)
    return Response('The pet not found', status=404)