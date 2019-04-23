from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from pymongo import MongoClient
import datetime
from bson.objectid import ObjectId
from FoodManagement.addkitchen.models import Stock
from .forms import NGOForm

mod = Blueprint('ngo', __name__, template_folder='templates')

@mod.route('/ngo', methods=['GET', 'POST'])
def ngo():
    if 'id' in session:
        if session['type'] == 'NGO':
            form = NGOForm()
            Client = MongoClient('localhost:27017')
            Db = Client.FoodManagement
            Customer = Db.Customer

            for customer in Customer.find({"_id": ObjectId(session['id'])}):
                NGOName = customer['Name']  

            S = Stock()
            Result = S.Retrieve()      

            KitchenList = {}
            AllCustomer = Customer.find({"Type": "Kitchen"})
            for A in AllCustomer:
                KitchenList[A['_id']] = A['Name']
            # print (KitchenList)
            for I in Result:
                for J in KitchenList:
                    if I['KitchenId'] == str(J):
                        I['KitchenName'] = KitchenList[J]
                        if I['Veg'] == 1:
                            I['Veg'] = 'Veg'
                        else:
                            I['Veg'] = 'Non Veg'
                        I['Quantity'] = I['Quantity']    
            # print (Result)

            CartList = []
            if request.method == 'POST':
                if form.is_submitted:
                    for I in request.form:
                        if I != "csrf_token" and I != "Buy": 
                            CartList.append(I)
                    session['CartList'] = str(CartList)
                    print (session['CartList'])
                    return redirect('/site/cart') 

            return render_template('ngo/index.html', title='NGO', NGOName = NGOName, Results = Result, form = form)
    else:
        return redirect('/site/login')

          