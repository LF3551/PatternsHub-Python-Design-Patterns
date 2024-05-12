from flask import Flask, jsonify, request

app = Flask(__name__)

# Имитация базы данных продуктов
products = {}

@app.route('/product/create', methods=['POST'])
def create_product():
    product_data = request.get_json()
    product_id = product_data['id']
    if product_id in products:
        return jsonify({"error": "Product already exists"}), 409
    products[product_id] = product_data
    return jsonify(product_data), 201

@app.route('/product/<product_id>', methods=['GET'])
def get_product(product_id):
    if product_id in products:
        return jsonify(products[product_id]), 200
    return jsonify({"error": "Product not found"}), 404

if __name__ == '__main__':
    app.run(port=5001)
