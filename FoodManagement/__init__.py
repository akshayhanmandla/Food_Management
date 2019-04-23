from flask import Flask
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = os.urandom(16)

from FoodManagement.index.routes import mod
from FoodManagement.register.routes import mod
from FoodManagement.login.routes import mod
from FoodManagement.kitchen.routes import mod
from FoodManagement.ngo.routes import mod
from FoodManagement.addkitchen.routes import mod
from FoodManagement.cart.routes import mod
from FoodManagement.order.routes import mod

app.register_blueprint(index.routes.mod, url_prefix='/site')
app.register_blueprint(register.routes.mod, url_prefix='/site')
app.register_blueprint(login.routes.mod, url_prefix='/site')
app.register_blueprint(kitchen.routes.mod, url_prefix='/site')
app.register_blueprint(ngo.routes.mod, url_prefix='/site')
app.register_blueprint(addkitchen.routes.mod, url_prefix='/site')
app.register_blueprint(cart.routes.mod, url_prefix='/site')
app.register_blueprint(order.routes.mod, url_prefix='/site')