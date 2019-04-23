from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from pymongo import MongoClient
import datetime
from bson.objectid import ObjectId
from FoodManagement.addkitchen.models import Stock
import pprint
import ast
import json
from FoodManagement.cart.models import Order
import pprint

mod = Blueprint('order', __name__, template_folder='templates')

@mod.route('/order', methods=['GET', 'POST'])
def order():
    if 'id' in session:
        if session['type'] == 'NGO':
            Client = MongoClient('localhost:27017')
            Db = Client.FoodManagement
            Customer = Db.Customer

            O = Order()
            print (session['id'])
            Result = O.Retrieve(session['id'])
            for I in Result:
                I['CreatedDate'] = I['CreatedDate'].strftime('%m/%d/%Y')
                I['LastModifiedDate'] = I['LastModifiedDate'].strftime('%m/%d/%Y')
            # pprint.pprint(Result)

            for customer in Customer.find({"_id": ObjectId(session['id'])}):
                NGOName = customer['Name']



            return render_template('order/index.html', title='Order', NGOName = NGOName, Results = Result)
    else:
        return redirect('/site/login') 