from flask import Blueprint, request, jsonify
from config.config import get_db_connection
from ..utils.whatsapp import send_whatsapp_message  # optional

order_bp = Blueprint("order_bp", __name__)


@order_bp.route('/place_order', methods=['POST'])
def save_order():
    data = request.get_json()
    print('data', data)
    items = data.get('items', [])
    total_amount = data.get('total_amount', 0.0)

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        for item in items:
            cursor.execute("""
                INSERT INTO order_details (item_name, qty, price, total)
                VALUES (%s, %s, %s, %s)
            """, (item['name'], item['qty'], item['price'], item['total']))

        conn.commit()
        cursor.close()
        conn.close()

        # Send WhatsApp message
        data = request.json
        items = data['items']
        total = data['total_amount']
        number = data.get('customer_number', 'N/A')
        location = data.get('customer_location', 'N/A')

        msg = f"📦 New Order from {number}\n📍 Location: {location}\n\n"
        for i in items:
            msg += f"{i['name']} x {i['qty']} = ₹{i['total']}\n"
        msg += f"\nTotal: ₹{total}"

        send_whatsapp_message(msg)

        return jsonify({"status": "success", "message": "Order saved and WhatsApp sent."})
    except Exception as e:
        print("Order error:", e)
        return jsonify({"status": "error", "message": str(e)}), 500
