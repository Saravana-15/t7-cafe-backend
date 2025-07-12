from flask import Flask
from flask_cors import CORS

from order_service.routes.menu_routes import menu_bp
from order_service.routes.order_routes import order_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(menu_bp, url_prefix="/api/menu")
app.register_blueprint(order_bp, url_prefix="/api/order")

if __name__ == "__main__":
    app.run(port=5001, debug=True)
