from flask import Flask, request, jsonify, render_template
import requests
from config import HANDY_BASE_URL, MERCHANT_SECRET_KEY
from services import clients, carts

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/create-order', methods=['POST'])
def create_order():
    data = request.json
    client_id = data.get('client_id')
    cart_invoice_number = data.get('cart_invoice_number')
    callback_url = data.get('callback_url')
    response_type = data.get('response_type')

    print("Received data:", data)
    print("Clients:", clients)
    print("Carts:", carts)

    client = next((c for c in clients if c.get('id') == client_id), None)
    cart = next((c for c in carts if c.get('InvoiceNumber') == cart_invoice_number), None)

    print("Found client:", client)
    print("Found cart:", cart)

    if not client or not cart:
        return jsonify({"error": "Client or Cart not found"}), 404

    payment_data = {
        "CallbackUrl": callback_url,
        "ResponseType": response_type,
        "Cart": cart,
        "Client": client
    }

    headers = {
        "merchant-secret-key": MERCHANT_SECRET_KEY,
        "Content-Type": "application/json"
    }

    response = requests.post(f"{HANDY_BASE_URL}/api/payments", json=payment_data, headers=headers)

    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Failed to create order"}), response.status_code


if __name__ == '__main__':
    app.run(port=5000, debug=True)
