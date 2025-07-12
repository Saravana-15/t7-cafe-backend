from flask import Blueprint, request, jsonify
# from config.config import get_db_connection
from ..utils.whatsapp import send_whatsapp_message  # optional

order_bp = Blueprint("order_bp", __name__)


@order_bp.route('/place_order', methods=['POST'])
def save_order():
    data = request.get_json()
    print('data', data)

    try:
        items = data['items']
        total = data['total_amount']
        name = data.get('customer_name', 'N/A')
        number = data.get('customer_number', 'N/A')
        location = data.get('customer_location', 'N/A')

        msg = (
            f"🧾 *New Order Received!*\n\n"
            f"👤 Name: {name}\n"
            f"📱 Number: {number}\n"
            f"📍 Location: {location}\n\n"
            f"🛒 *Order Items:*\n"
        )

        for i in items:
            msg += f"• {i['name']} × {i['qty']} = ₹{i['total']}\n"

        msg += f"\n💰 Total: ₹{total}"

        send_whatsapp_message(msg)

        return jsonify({"status": "success", "message": "Order saved and WhatsApp sent."})
    except Exception as e:
        print("Order error:", e)
        return jsonify({"status": "error", "message": str(e)}), 500
