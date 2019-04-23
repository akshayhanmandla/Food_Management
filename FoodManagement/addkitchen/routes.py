from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from pymongo import MongoClient
import datetime
from .forms import AddKitchenForm
from .models import Stock

mod = Blueprint('addkitchen', __name__, template_folder='templates')

@mod.route('/addkitchen', methods=['GET', 'POST'])
def addkitchen():
    if 'id' in session:
        if session['type'] == 'Kitchen':
            form = AddKitchenForm()

            S = Stock()
            Result = S.Retrieve(session['id'])

            counter = 1
            for I in Result:
                I['id'] = counter
                if I['Veg'] == 1:
                    I['Veg'] = 'Veg'
                else:
                    I['Veg'] = 'Non Veg'
                I['Quantity'] = str(I['Quantity'])
                counter = counter + 1

            if request.method == "POST":
                if form.is_submitted():
                    Name = form.Name.data
                    Quantity = form.Quantity.data
                    V = request.form.get('Veg')
                    if V is None:
                        V = 0
                    else:
                        V = 1
                    print (session['id'])
                    Result1 = S.Create(Name, Quantity, V, session['id'])
                    if Result1 == 0:
                        Result2 = S.Update(Name, Quantity, V, session['id'])       
                        return redirect('site/addkitchen')
                    return redirect('site/addkitchen')

            return render_template('addkitchen/index.html', title='Add Kitchen', form=form, Results=Result)
    else:
        return redirect('/site/login')
