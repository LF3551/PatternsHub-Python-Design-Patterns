from flask import Flask, jsonify, request

app = Flask(__name__)

# Имитация базы данных пользователей
users = {}

@app.route('/user/create', methods=['POST'])
def create_user():
    user_data = request.get_json()
    user_id = user_data['id']
    if user_id in users:
        return jsonify({"error": "User already exists"}), 409
    users[user_id] = user_data
    return jsonify(user_data), 201

@app.route('/user/<user_id>', methods=['GET'])
def get_user(user_id):
    if user_id in users:
        return jsonify(users[user_id]), 200
    return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(port=5000)
