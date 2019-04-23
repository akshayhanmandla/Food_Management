from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from pymongo import MongoClient
import datetime
from bson.objectid import ObjectId
from FoodManagement.addkitchen.models import Stock
import pprint
import ast
from .forms import CartForm
import json
from .models import Order

mod = Blueprint('cart', __name__, template_folder='templates')

@mod.route('/cart', methods=['GET', 'POST'])
def cart():
    if 'id' in session:
        if session['type'] == 'NGO':
            form = CartForm()
            CartList = ast.literal_eval(session['CartList'])
            Client = MongoClient('localhost:27017')
            Db = Client.FoodManagement
            Customer = Db.Customer

            KitchenList = {}
            AllCustomer = Customer.find({"Type": "Kitchen"})
            for A in AllCustomer:
                KitchenList[A['_id']] = A['Name']

            S = Stock()
            O = Order()

            for customer in Customer.find({"_id": ObjectId(session['id'])}):
                NGOName = customer['Name'] 

            Result = []
            for I in CartList:
                print (I)
                D = S.RetrieveSingle(I)
                for J in D:
                    Result.append(J)

            for I in Result:
                for J in KitchenList:
                    if I['KitchenId'] == str(J):
                        I['KitchenName'] = KitchenList[J]
                        if I['Veg'] == 1:
                            I['Veg'] = 'Veg'
                        else:
                            I['Veg'] = 'Non Veg'
                        I['Quantity'] = I['Quantity']
            
            if request.method == 'POST':
                if form.is_submitted:
                    for Key, Value in request.form.to_dict().items():
                        for J in Result:
                            if J['_id'] == Key:
                                TotalQuantity = J['Quantity'] - int(Value) 
                                J['Quantity'] = TotalQuantity   
                                A = S.Update(J['Name'], J['Quantity'], J['Veg'], J['KitchenId'])  

                    O1 = O.Create(Result, session['id'])
                    flash('Order Placed Successfully') 
                    return redirect('/site/ngo')


                       

            return render_template('cart/index.html', title='Cart', NGOName = NGOName, Results = Result, form = form)
    else:
        return redirect('/site/login')  