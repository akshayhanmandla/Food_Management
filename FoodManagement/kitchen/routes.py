from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
from pymongo import MongoClient
from bson.objectid import ObjectId
from FoodManagement.cart.models import Order
import pprint

mod = Blueprint('kitchen', __name__, template_folder='templates')

@mod.route('/kitchen', methods=['GET', 'POST'])
def kitchen():
    if 'id' in session:
        if session['type'] == 'Kitchen': 
            O = Order()

            Client = MongoClient('localhost:27017')
            Db = Client.FoodManagement
            Customer = Db.Customer
            for customer in Customer.find({"_id": ObjectId(session['id'])}):
                KitchenName = customer['Name']

            Result = O.RetrieveForKitchen(session['id'])
            for I in Result:
                I['CreatedDate'] = I['CreatedDate'].strftime('%m/%d/%Y')
                I['LastModifiedDate'] = I['LastModifiedDate'].strftime('%m/%d/%Y')
                for ngo in Customer.find({"_id": ObjectId(I["NGOId"])}):
                    I['NGOName'] = ngo['Name']
                    I['Email'] = ngo['Email']
                for J in I['Orders']:
                    if J['KitchenId'] not in session['id']:
                        I['Orders'].remove(J)              
            pprint.pprint(Result)

            return render_template('kitchen/index.html', title='Kitchen', KitchenName = KitchenName, Results=Result)
    else:
        return redirect('/site/login')