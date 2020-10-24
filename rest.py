from flask import Flask, json, jsonify
from host import *
app = Flask(__name__)
def check(id) -> str:
    with open('user_id.json') as f:
        user_id = json.load(f)
    id = str(id)
    for user in user_id:
        if user["id"] == id:
            return 'True'

    return 'False'


@app.route('/user_id/', methods=['GET'])
def get_list():
    return jsonify(user_id)


@app.route('/user_id/<id>', methods=['GET'])
def get_user(id):
    return check(id)


if __name__ == '__main__':
    app.run(host=REST_HOST, port=REST_PORT)
# http://localhost/user_id/