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
          "Quick Bites": [
            {"id": 1, "name": "Veg Puff", "price": 15, "image_url": "/static/images/veg-puff.jpg"},
            {"id": 2, "name": "Egg Puff", "price": 18, "image_url": "/static/images/egg-puff.jpg"},
            {"id": 3, "name": "Chicken Roll", "price": 22, "image_url": "/static/images/chicken-roll.jpg"},
            {"id": 4, "name": "French Fries", "price": 45, "image_url": "/static/images/french-fries.jpg"},
            {"id": 5, "name": "Smily Fries (5pcs)", "price": 45, "image_url": "/static/images/smiley-fries.jpg"},
            {"id": 6, "name": "Cheese Ball (5pcs)", "price": 50, "image_url": "/static/images/cheese-ball.jpg"},
            {"id": 7, "name": "Veg Nugget (5pcs)", "price": 45, "image_url": "/static/images/veg-nuggets.jpg"},
            {"id": 8, "name": "Chicken Nugget (5pcs)", "price": 55, "image_url": "/static/images/chicken-nuggets.jpg"},
            {"id": 9, "name": "Veg Momo (5pcs)", "price": 45, "image_url": "/static/images/veg-momo.jpg"},
            {"id": 10, "name": "Chicken Momo (5pcs)", "price": 55, "image_url": "/static/images/chicken-momo.jpg"},
            {"id": 11, "name": "Veg Cheese Sandwich", "price": 40, "image_url": "/static/images/cheese-sandwich.jpg"},
            {"id": 12, "name": "Paneer Sandwich", "price": 50, "image_url": "/static/images/paneer-sandwich.jpg"},
            {"id": 13, "name": "Corn Sandwich", "price": 50, "image_url": "/static/images/corn-sandwich.jpg"},
            {"id": 14, "name": "Bread Omelette", "price": 40, "image_url": "/static/images/bread-omelette.jpg"},
            {"id": 15, "name": "Cheese Bread Omelette", "price": 50, "image_url": "/static/images/cheese-bread-omelette.jpg"},
            {"id": 16, "name": "Veg Burger", "price": 60, "image_url": "/static/images/veg-burger.jpg"},
            {"id": 17, "name": "Chicken Burger", "price": 80, "image_url": "/static/images/chicken-burger.jpg"}
          ],
          "Ice Creams": [
            {"id": 18, "name": "Brownie with Ice Cream", "price": 70, "image_url": "/static/images/brownie-icecream.jpg"},
            {"id": 19, "name": "Vanilla", "price": 40, "image_url": "/static/images/vanilla.jpg"},
            {"id": 20, "name": "Strawberry", "price": 40, "image_url": "/static/images/strawberry.jpg"},
            {"id": 21, "name": "Butterscotch", "price": 40, "image_url": "/static/images/butterscotch.jpg"},
            {"id": 22, "name": "Chocolate", "price": 50, "image_url": "/static/images/chocolate.jpg"},
            {"id": 23, "name": "Mango", "price": 50, "image_url": "/static/images/mango.jpg"},
            {"id": 24, "name": "Black Currant", "price": 50, "image_url": "/static/images/blackcurrant.jpg"},
            {"id": 25, "name": "Kulfi", "price": 40, "image_url": "/static/images/kulfi.jpg"}
            {"id": 32, "name": "Strawberry-Vanilla mixed", "price": 40, "image_url": "/static/images/strawberry.jpg"},          ],
          "Desserts": [
            {"id": 26, "name": "Brownie", "price": 45, "image_url": "/static/images/brownie.jpg"},
            {"id": 27, "name": "White Brownie", "price": 50, "image_url": "/static/images/white-brownie.jpg"},
            {"id": 28, "name": "Mutta Mittai", "price": 45, "image_url": "/static/images/mutta-mittai.jpg"}
          ],
          "Cool Drinks": [
            {"id": 29, "name": "Rose Milk", "price": 35, "image_url": "/static/images/rose-milk.jpg"},
            {"id": 30, "name": "Badam Milk", "price": 35, "image_url": "/static/images/badam-milk.jpg"},
            {"id": 31, "name": "Cold Coffee", "price": 40, "image_url": "/static/images/cold-coffee.jpg"}
          ]
        }

    menu_itemss = {
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
        ],
        "Drinks": [
            {
                'image_url': ''
            }
        ]
    }

    return jsonify(menu_items)
