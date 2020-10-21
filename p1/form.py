from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed
from flask_login import current_user
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError
from p1.models import User,Books,t1


class RegistrationForm(FlaskForm):
	username=StringField('Username',validators=[DataRequired(),
		Length(min=3,max=20)])
	email=StringField('Email',validators=[DataRequired(),
		Email()])
	password=PasswordField('Password',validators=[DataRequired()])
	confirm_password=PasswordField('Confirm_password',
						validators=[DataRequired(),EqualTo('password')])
	phone=StringField('Phone',validators=[DataRequired(),
		Length(min=10,max=10)])
	submit=SubmitField('Sign up')

	def validate_username(self,username):
		user1=User.query.filter_by(username=username.data).first()
		if user1:
			raise ValidationError('This username is taken please choose another one')	

	def validate_email(self,email):
		user=User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError('This Email is registered, You can login directly')		

class LoginForm(FlaskForm):
	email=StringField('Email',validators=[DataRequired(),
		Email()])
	password=PasswordField('Password',validators=[DataRequired()])
	remember=BooleanField('Remember me')
	submit=SubmitField('Login')
	

class UpdateAccountForm(FlaskForm):
	username=StringField('Username',validators=[DataRequired(),
		Length(min=3,max=20)])
	email=StringField('Email',validators=[DataRequired(),
		Email()])
	picture=FileField('Update your Profile Picture from here',validators=[FileAllowed(['jpg','png'])])
	submit=SubmitField('Update')

	def validate_username(self,username):
		if username.data!=current_user.username:
			user1=User.query.filter_by(username=username.data).first()
			if user1:
				raise ValidationError('This username is taken please choose another one')	

	def validate_email(self,email):
		if email.data!=current_user.email:
			user=User.query.filter_by(email=email.data).first()
			if user:
				raise ValidationError('This Email is registered, You can login directly')	

class SelectBook(FlaskForm):
	book_name=StringField('Bookname',validators=[Length(min=0,max=200)])

class admin_pass(FlaskForm):
	d="d1"
	admin_password=PasswordField('Password',validators=[DataRequired(),EqualTo('d')])
	username=StringField('Username',validators=[DataRequired(),
		Length(min=3,max=20)])
	def validate_username(self,username):
		if username.data!=current_user.username:
			user1=User.query.filter_by(username=username.data).first()
			if user1:
				user1=user1
			else:
				raise ValidationError('This user doesnt exists')	