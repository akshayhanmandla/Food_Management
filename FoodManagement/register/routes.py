from flask import Blueprint, render_template, request, redirect, url_for, flash, session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date, timedelta
from json import loads, dumps
from FoodManagement.register.forms import RegisterForm
from .utils import Customer

mod = Blueprint('register', __name__, template_folder='templates')

@mod.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegisterForm()
    
    if request.method == 'POST':
        if form.validate_on_submit():
            Name = form.Username.data
            Email = form.Email.data
            PhoneNumber = None
            # print (form.PhoneNumber.data)
            Password = form.Password.data
            Type = form.Type.data

            C = Customer()
            Result = C.Create(Name, Email, PhoneNumber, Password, Type)
            print (Result)
            if Result == 1:
                flash('Successful Registration')
                return redirect('/site/index')
            elif Result != 1:
                flash('Unsuccessful Registration')
    return render_template('register/page-register.html', title='Register', form=form)