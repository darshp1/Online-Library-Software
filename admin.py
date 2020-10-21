from flask import render_template,flash,redirect,url_for,request
from p1 import app,db,bcrypt
from p1.form import RegistrationForm,LoginForm,UpdateAccountForm
from p1.models import User,Books,t1
from flask_login import login_user,current_user,logout_user,login_required

@app.route('/')
def admin():
	return render_template('admin.html', title= 'Admin Page')