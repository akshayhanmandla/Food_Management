from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
from FoodManagement.login.forms import LoginForm
from pymongo import MongoClient
from bson import ObjectId

mod = Blueprint('login', __name__, template_folder='templates')

@mod.route('/login', methods=['GET', 'POST'])
def login():
    if 'id' in session:
        if session['type'] == 'Kitchen':
            return redirect('/site/kitchen') 
        elif session['type'] == 'NGO':
            return redirect('/site/ngo') 
    else:
        ##Mongodb
        client = MongoClient('localhost', 27017)
        Db = client.FoodManagement
        Customer = Db.Customer

        form = LoginForm()

        if request.method == 'POST':
            if form.validate():
                Email = form.Email.data
                Password = form.Password.data   
                customer = Customer.find({"Email": Email})
                # print (customer)
                for I in customer:
                    if I['Email'] is None or not check_password_hash(I['Password'], Password):
                        flash('Invalid username or password')
                        return redirect('/site/login')
                    session['id'] = str(I['_id'])
                    session['type'] = I['Type']
                    if session['type'] == 'Kitchen':
                        return redirect('/site/kitchen') 
                    elif session['type'] == 'NGO':  
                        return redirect('/site/ngo') 
                    
    return render_template('login/page-login.html', title='Login', form=form)

@mod.route("/logout")
def logout():
    session.pop('id', None)
    session.pop('type', None)
    return redirect('/site/login')  