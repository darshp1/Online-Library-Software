import secrets
import os
from flask import render_template,flash,redirect,url_for,request
from p1 import app,db,bcrypt
from p1.form import RegistrationForm,LoginForm,UpdateAccountForm
from p1.models import User,Books,t1
from flask_login import login_user,current_user,logout_user,login_required
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///p1/site.db',echo=True)
Session = sessionmaker(bind=engine)
session = Session()



@app.route('/')

@app.route('/home')
def home_page():
	return render_template('home.html', title= 'Home Page')

@app.route('/home2')
def home2():
	return render_template('home2.html', title= 'Home Page2')

@app.route('/logout')
def logout():
	logout_user()
	return redirect('home')

def save_picture(form_picture):
	random_hex=secrets.token_hex(8)
	f_,f_ext=os.path.splitext(form_picture.filename)
	picture_fn=random_hex+f_ext
	picture_path=os.path.join(app.root_path,'static/profile_pics',picture_fn)
	form_picture.save(picture_path)
	return picture_fn

@app.route('/about',methods=['GET','POST'])
@login_required 
def about_page():
	form =UpdateAccountForm()
	if form.validate_on_submit():
		if form.picture.data:
			picture_file=save_picture(form.picture.data)
			current_user.image_file=picture_file
		current_user.username=form.username.data
		current_user.email=form.email.data
		db.session.commit()
		flash('Your account has been updated!','success')
		return redirect(url_for('about_page'))
	elif request.method=='GET':
		form.username.data=current_user.username
		form.email.data=current_user.email
	image_file=url_for('static',filename='profile_pics/'+current_user.image_file)
	return render_template('about.html', title='About',image_file=image_file,form=form)


@app.route('/sign_up',methods=['GET','POST'])
def sing_up(): 
	if current_user.is_authenticated:
		return redirect(url_for('home2'))
	form=RegistrationForm()
	if (form.validate_on_submit()):
		hp=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user=User(username=form.username.data,email=form.email.data,password=hp,phone=form.phone.data)
		db.session.add(user)
		db.session.commit()
		flash( f'Your account is created for {form.username.data}!','success') 
		return redirect(url_for('home2'))
	elif (form.validate_on_submit()==False):  
		flash('sorry  error in your data','fail')
		return render_template('sign_up.html', title='Sign Up', form=form)
	return render_template('sign_up.html', title='Sign Up', form=form)

@app.route("/login",methods=['GET','POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('home2'))
	form=LoginForm()
	if (form.validate_on_submit()):
		user=User.query.filter_by(email=form.email.data).first()
		if user and bcrypt.check_password_hash(user.password,form.password.data):
			login_user(user,remember=form.remember.data)
			next_page=request.args.get('next')
			return redirect(next_page) if next_page else redirect(url_for('home2'))
		else:
			flash('Login uncsuccessful, Please check your email and password','danger')
		return render_template('login.html', title='Login', form=form)
	return render_template('login.html', title='Login Page',form=form)

@app.route('/Search_Book',methods=['GET','POST'])
@login_required 
def Search_Book():
	bname="d"
	if request.method == "POST":
		bname=request.form.get("jd",None)
		s_book=request.form.get("searchbooks",None)

		if s_book:
			return render_template("searchbook.html", s_book = s_book)
	try:
		colours= session.query(Books).filter(Books.book_name.like("%"+bname+"%")).limit(5).all()
		if bname:		
							#Books.query.filter(Books.book_name.like("%Ja%")).limit(5).all()
			return render_template("searchbook.html", colours=colours)
		colours1=[]
		for i in colours:
			colours1.append(i.book_name)
		if colours1:
			return render_template("searchbook.html", colours1=colours1)
	except:
		engine = create_engine('sqlite:///p1/site.db',echo=True)
		Session = sessionmaker(bind=engine)
		session = Session()
		colours= session.query(Books).filter(Books.book_name.like("%"+bname+"%")).limit(5).all()
		if bname:
			return render_template("searchbook.html", colours=colours)
		
	return render_template('searchbook.html', title='Search Books')




hioewfhwfw



import secrets
import os
from flask import render_template,flash,redirect,url_for,request
from p1 import app,db,bcrypt
from p1.form import RegistrationForm,LoginForm,UpdateAccountForm
from p1.models import User,Books,t1
from flask_login import login_user,current_user,logout_user,login_required
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import requests,sys,webbrowser
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///p1/site.db',echo=True)
Session = sessionmaker(bind=engine)
session = Session()



@app.route('/')

@app.route('/home')
def home_page():
	return render_template('home.html', title= 'Home Page')

@app.route('/home2')
def home2():
	return render_template('home2.html', title= 'Home Page2')

@app.route('/logout')
def logout():
	logout_user()
	return redirect('home')

def save_picture(form_picture):
	random_hex=secrets.token_hex(8)
	f_,f_ext=os.path.splitext(form_picture.filename)
	picture_fn=random_hex+f_ext
	picture_path=os.path.join(app.root_path,'static/profile_pics',picture_fn)
	form_picture.save(picture_path)
	return picture_fn

@app.route('/about',methods=['GET','POST'])
@login_required 
def about_page():
	form =UpdateAccountForm()
	if form.validate_on_submit():
		if form.picture.data:
			picture_file=save_picture(form.picture.data)
			current_user.image_file=picture_file
		current_user.username=form.username.data
		current_user.email=form.email.data
		db.session.commit()
		flash('Your account has been updated!','success')
		return redirect(url_for('about_page'))
	elif request.method=='GET':
		form.username.data=current_user.username
		form.email.data=current_user.email
	image_file=url_for('static',filename='profile_pics/'+current_user.image_file)
	return render_template('about.html', title='About',image_file=image_file,form=form)


@app.route('/sign_up',methods=['GET','POST'])
def sing_up(): 
	if current_user.is_authenticated:
		return redirect(url_for('home2'))
	form=RegistrationForm()
	if (form.validate_on_submit()):
		hp=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user=User(username=form.username.data,email=form.email.data,password=hp,phone=form.phone.data)
		db.session.add(user)
		db.session.commit()
		flash( f'Your account is created for {form.username.data}!','success') 
		return redirect(url_for('home2'))
	elif (form.validate_on_submit()==False):  
		flash('sorry  error in your data','fail')
		return render_template('sign_up.html', title='Sign Up', form=form)
	return render_template('sign_up.html', title='Sign Up', form=form)

@app.route("/login",methods=['GET','POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('home2'))
	form=LoginForm()
	if (form.validate_on_submit()):
		user=User.query.filter_by(email=form.email.data).first()
		if user and bcrypt.check_password_hash(user.password,form.password.data):
			login_user(user,remember=form.remember.data)
			next_page=request.args.get('next')
			return redirect(next_page) if next_page else redirect(url_for('home2'))
		else:
			flash('Login uncsuccessful, Please check your email and password','danger')
		return render_template('login.html', title='Login', form=form)
	return render_template('login.html', title='Login Page',form=form)

@app.route('/Search_Book',methods=['GET','POST'])
@login_required 
def Search_Book():
	
	if request.method == "POST":
		bname=request.form.get("jd",None)
		s_book=request.form.get("searchbooks",None)

		if s_book:
			return render_template("searchbook.html", s_book = s_book)
	try:
		colours= session.query(Books).filter(Books.book_name.like("%"+bname+"%")).limit(5).all()
		if bname:
			ua = UserAgent()
			query=bname
			google_url = "https://www.google.com/search?q=" + query + " GoodReads"
			response = requests.get(google_url, {"User-Agent": ua.random})
			soup = BeautifulSoup(response.text, "html.parser")

			result_div = soup.find_all('div', attrs = {'class': 'ZINbbc'})
			file = open('d7.txt', 'a')
			links = []
			titles = []
			descriptions = []
			for r in result_div:
			    # Checks if each element is present, else, raise exception
			    try:
			        link = r.find('a', href = True)
			        title = r.find('div', attrs={'class':'vvjwJb'}).get_text()
			        description = r.find('div', attrs={'class':'s3v9rd'}).get_text()
			        
			        # Check to make sure everything is present before appending
			        if link != '' and title != '' and description != '': 
			            links.append(link['href'])
			            titles.append(title)
			       
			            return render_template("searchbook.html", title=title)
			            descriptions.append(description)
			            
			            return render_template("searchbook.html", description=description)

			    except:
        			continue
				
			return render_template("searchbook.html", colours=colours)	
							#Books.query.filter(Books.book_name.like("%Ja%")).limit(5).all()
			
		colours1=[]
		for i in colours:
			colours1.append(i.book_name)
		if colours1:
			return render_template("searchbook.html", colours1=colours1)
	except:
		engine = create_engine('sqlite:///p1/site.db',echo=True)
		Session = sessionmaker(bind=engine)
		session = Session()
		colours= session.query(Books).filter(Books.book_name.like("%"+bname+"%")).limit(5).all()
		if bname:
			ua = UserAgent()
			query=bname
			google_url = "https://www.google.com/search?q=" + query + " GoodReads"
			response = requests.get(google_url, {"User-Agent": ua.random})
			soup = BeautifulSoup(response.text, "html.parser")

			result_div = soup.find_all('div', attrs = {'class': 'ZINbbc'})
			file = open('d7.txt', 'a')
			links = []
			titles = []
			descriptions = []
			for r in result_div:
			    # Checks if each element is present, else, raise exception
			    try:
			        link = r.find('a', href = True)
			        title = r.find('div', attrs={'class':'vvjwJb'}).get_text()
			        if title:
			        	return render_template("searchbook.html", title="jd")
			        description = r.find('div', attrs={'class':'s3v9rd'}).get_text()
			        
			        # Check to make sure everything is present before appending
			        if link != '' and title != '' and description != '': 
			            links.append(link['href'])
			            titles.append(title)
			            
			            descriptions.append(description)
			            return render_template("searchbook.html", description="dp")
			    except:
        			continue

			return render_template("searchbook.html", colours=colours)

		colours1=[]
		for i in colours:
			colours1.append(i.book_name)
		if colours1:
			return render_template("searchbook.html", colours1=colours1)
	return render_template('searchbook.html', title='Search Books')

