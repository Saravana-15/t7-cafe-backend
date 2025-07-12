from flask import Blueprint, jsonify
# from config.config import get_db_connection

menu_bp = Blueprint("menu_bp", __name__)


@menu_bp.route("/list", methods=["GET"])
def get_menu():

    '''connection = get_db_connection()
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
            connection.close()'''

    menu_items = {
        "Ice Creams": [
            {
                "id": 13,
                "image_url": "/static/images/blackcurrant.jpg",
                "name": "Blackcurrant",
                "price": 50.0
            },
            {
                "id": 6,
                "image_url": "/static/images/chocholate.jpg",
                "name": "Chocolate",
                "price": 50.0
            },
            {
                "id": 12,
                "image_url": "/static/images/mango.jpg",
                "name": "Mango",
                "price": 50.0
            },
            {
                "id": 7,
                "image_url": "/static/images/strawberry.jpg",
                "name": "Strawberry",
                "price": 50.0
            },
            {
                "id": 5,
                "image_url": "/static/images/vanilla.jpg",
                "name": "Vanilla",
                "price": 40.0
            }
        ],
        "Puffs": [
            {
                "id": 4,
                "image_url": "/static/images/chicken-roll.jpg",
                "name": "Chicken Roll",
                "price": 22.0
            },
            {
                "id": 2,
                "image_url": "/static/images/egg-puff.jpg",
                "name": "Egg Puff",
                "price": 18.0
            },
            {
                "id": 1,
                "image_url": "/static/images/veg-puff.jpg",
                "name": "Veg Puff",
                "price": 15.0
            },
            {
                "id": 3,
                "image_url": "/static/images/veg-roll.jpg",
                "name": "Veg Roll",
                "price": 18.0
            }
        ],
        "Sandwiches": [
            {
                "id": 9,
                "image_url": "/static/images/cheese-sandwich.jpg",
                "name": "Cheese Sandwich",
                "price": 50.0
            },
            {
                "id": 11,
                "image_url": "/static/images/egg-sandwich.jpg",
                "name": "Egg Sandwich",
                "price": 50.0
            },
            {
                "id": 10,
                "image_url": "/static/images/paneer-sandwich.jpg",
                "name": "Paneer Sandwich",
                "price": 50.0
            },
            {
                "id": 8,
                "image_url": "/static/images/veg-sandwich.jpg",
                "name": "Veg Sandwich",
                "price": 40.0
            }
        ]
    }

    return jsonify(menu_items)
