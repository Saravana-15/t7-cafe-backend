from flask import Blueprint, jsonify
from config.config import get_db_connection

menu_bp = Blueprint("menu_bp", __name__)


@menu_bp.route("/list", methods=["GET"])
def get_menu():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            query = """
                SELECT mi.id, mi.name AS item_name, mi.price, mi.image_url, mc.name AS category
                FROM menu_items mi
                JOIN menu_categories mc ON mi.category_id = mc.id
                ORDER BY mc.name, mi.name;
            """
            cursor.execute(query)
            rows = cursor.fetchall()

        # Grouping by category
        grouped_menu = {}
        for row in rows:
            category = row["category"]
            item = {
                "id": row["id"],
                "name": row["item_name"],
                "price": float(row["price"]),
                "image_url": row["image_url"]  # 👈 include it
            }
            grouped_menu.setdefault(category, []).append(item)

        return jsonify(grouped_menu)

    finally:
        connection.close()
