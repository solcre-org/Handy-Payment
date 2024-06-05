from flask import Flask, request, jsonify

app = Flask(__name__)

products = []
clients = [
    {
        "CommerceName": "Cliente 1",
        "SiteUrl": "https://www.clienteuno.com",
        "id": 1
    }
]
carts = [
    {
        "Currency": 858,
        "InvoiceNumber": 1234,
        "LinkImageUrl": "http://www.imagenproductouno.jpg",
        "Products": [
            {
                "Amount": 10.0,
                "Name": "Product 1",
                "Quantity": 10,
                "TaxedAmount": 22
            }
        ],
        "TaxedAmount": 100.0,
        "TotalAmount": 122.0,
        "TransactionExternalId": "5f37ea13-c9bd-412c-8971-be7448dacae0"
    }
]


# CRUD para productos
@app.route('/products', methods=['POST'])
def create_product():
    product = request.json
    products.append(product)
    return jsonify(product), 201


@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)


@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((p for p in products if p.get('id') == product_id), None)
    if product:
        return jsonify(product)
    return jsonify({'error': 'Product not found'}), 404


@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = next((p for p in products if p.get('id') == product_id), None)
    if product:
        data = request.json
        product.update(data)
        return jsonify(product)
    return jsonify({'error': 'Product not found'}), 404


@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    global products
    products = [p for p in products if p.get('id') != product_id]
    return '', 204


# CRUD para clientes
@app.route('/clients', methods=['POST'])
def create_client():
    client = request.json
    clients.append(client)
    return jsonify(client), 201


@app.route('/clients', methods=['GET'])
def get_clients():
    return jsonify(clients)


@app.route('/clients/<int:client_id>', methods=['GET'])
def get_client(client_id):
    client = next((c for c in clients if c.get('id') == client_id), None)
    if client:
        return jsonify(client)
    return jsonify({'error': 'Client not found'}), 404


@app.route('/clients/<int:client_id>', methods=['PUT'])
def update_client(client_id):
    client = next((c for c in clients if c.get('id') == client_id), None)
    if client:
        data = request.json
        client.update(data)
        return jsonify(client)
    return jsonify({'error': 'Client not found'}), 404


@app.route('/clients/<int:client_id>', methods=['DELETE'])
def delete_client(client_id):
    global clients
    clients = [c for c in clients if c.get('id') != client_id]
    return '', 204


# CRUD para carritos de compras
@app.route('/carts', methods=['POST'])
def create_cart():
    cart = request.json
    carts.append(cart)
    return jsonify(cart), 201


@app.route('/carts', methods=['GET'])
def get_carts():
    return jsonify(carts)


@app.route('/carts/<int:cart_id>', methods=['GET'])
def get_cart(cart_id):
    cart = next((c for c in carts if c.get('InvoiceNumber') == cart_id), None)
    if cart:
        return jsonify(cart)
    return jsonify({'error': 'Cart not found'}), 404


@app.route('/carts/<int:cart_id>', methods=['PUT'])
def update_cart(cart_id):
    cart = next((c for c in carts if c.get('InvoiceNumber') == cart_id), None)
    if cart:
        data = request.json
        cart.update(data)
        return jsonify(cart)
    return jsonify({'error': 'Cart not found'}), 404


@app.route('/carts/<int:cart_id>', methods=['DELETE'])
def delete_cart(cart_id):
    global carts
    carts = [c for c in carts if c.get('InvoiceNumber') != cart_id]
    return '', 204


if __name__ == '__main__':
    app.run(port=5001, debug=True)
