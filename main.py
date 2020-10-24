from flask import Flask, json, jsonify
from settings import *

app = Flask(__name__)

def check(id) -> str: 
	with open('id_check_in.json') as ch:
		users_list = json.load(ch)
	id = str(id)
	for user in users_list:
		if user["id"] == id:
			return 'Пользоатель найден'
	return 'Пользователя нет в списке'

@app.route('/id_check_in/', methods=['GET'])
def get_list():
	return jsonify(users_list)

@app.route('/id_check_in/<id>', methods=['GET'])
def get_user(id):
	return check(id)

if __name__ == '__main__':
	app.run(host = REST_HOST, port = REST_PORT)
