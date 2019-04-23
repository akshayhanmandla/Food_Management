from flask import Blueprint, render_template, request, redirect, url_for, flash, session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
# from dateutil import parser
from datetime import date, timedelta
from json import loads, dumps

mod = Blueprint('index', __name__, template_folder='templates')

@mod.route('/index', methods = ['GET', 'POST'])
def index():
    return render_template('index/index.html')