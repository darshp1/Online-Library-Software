from p1 import db,login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

class User(db.Model,UserMixin):
	id=db.Column(db.Integer,primary_key=True)
	username=db.Column(db.String(20),unique=True,nullable=False)
	email=db.Column(db.String(120),unique=True,nullable=False)
	image_file=db.Column(db.String(20),nullable=False,default='default.jpg')
	password=db.Column(db.String(60),nullable=False)
	phone=db.Column(db.String(10),nullable=False)

	def __repr__(self):
		return f"User('{self.username}','{self.id}','{self.email}','{self.image_file}','{self.phone}')"

class Books(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	book_name=db.Column(db.String(100),nullable=False)
	book_section=db.Column(db.String(100),nullable=False)
	author1=db.Column(db.String(100),nullable=False)
	available=db.Column(db.Integer,nullable=False)


	def __repr__(self):
		return f"Books('{self.book_name}','{self.author1}','{self.available}','{self.book_section}')"

class t1(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	book_name1=db.Column(db.String(100),nullable=False)
	date_taken=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
	user_name1=db.Column(db.String(20),unique=True,nullable=False)
	date_returned=db.Column(db.DateTime)


	def __repr__(self):
		return f"t1('{self.date_taken}','{self.book_name1}','{self.user_name1}')"

#p1=User.query.filter(User.username.like("darsh")).first()
# book1 = Books(book_name='Headfirst',book_section='Java',author1='Darsh',available=58,user_id=p1.id)
#db.session.add(book1)
#db.session.commit()
# book1 = Books(book_name='Java Programming Language',book_section='Java',author1='Ken Arnold, James Gosling, David Holmes',available=60)
# book1 = Books(book_name='Head First Java',book_section='Java',author1='Kathy Sierra, Bert Bates',available=58)
# book1 = Books(book_name='Thinking In Java',book_section='Java',author1='Bruce Eckel',available=58)
# book1 = Books(book_name='The elements of Java style',book_section='Java',author1='Scott Ambler, Alan Vermeulen',available=58)
# book1 = Books(book_name=' Effective Java',book_section='Java',author1='Joshua Bloch',available=58)

#python
# book1 = Books(book_name='Python Crash Course',book_section='python',author1='Eric Matthews',available=58)
# book1 = Books(book_name='Head-First Python',book_section='python',author1='Paul Barry',available=58)
# book1 = Books(book_name='Learn Python the Hard Way',book_section='python',author1='Zed A. Shaw',available=58)
# book1 = Books(book_name='A Byte of Python',book_section='python',author1='C.H. Swaroop',available=58)
# book1 = Books(book_name='Programming Python: Powerful Object-Oriented Programming',book_section='python',author1='Mark Lutz',available=58)

#c
# book1 = Books(book_name='C Programming Absolute Beginner's Guide',book_section='C language',author1='Greg Perry',available=58)
# book1 = Books(book_name='The C Programming Language (2nd Edition)',book_section='C language',author1='Brian W. Kernighan and Dennis M. Ritchie',available=58)
# book1 = Books(book_name='Learn C the Hard Way',book_section='C language',author1='Zed A. Shaw',available=58)
# book1 = Books(book_name='Head First C',book_section='C language',author1='David Griffiths and Dawn Griffiths',available=58)
# book1 = Books(book_name='C Programming: A Modern Approach (2nd Edition)',book_section='C language',author1='K. N. King',available=58)

#c++
# book1 = Books(book_name='C++ Primer (5th Edition)',book_section='C++',author1='B. Lippman, Josée Lajoie, and Barbara E. Moo',available=58)
# book1 = Books(book_name='Effective Modern C++',book_section='C++',author1='Scott Meyers',available=58)
# book1 = Books(book_name='The C++ Programming Language (4th Edition)',book_section='C++',author1='Bjarne Stroustrup',available=58)
# book1 = Books(book_name='Accelerated C++: Practical Programming by Example',book_section='C++',author1='Andrew Koenig and Barbara E. Moo',available=58)
# book1 = Books(book_name='Programming: Principles and Practice Using C++',book_section='C++',author1='Bjarne Stroustrup',available=58)

#c#
# book1 = Books(book_name='C# 5.0 in a Nutshell: The Definitive Reference',book_section='C#',author1='Joseph Albahari, Ben Albahari',available=58)
# book1 = Books(book_name='Head First C#',book_section='C#',author1='Jennifer Greene, Andrew Stellman',available=58)
# book1 = Books(book_name='Pro C# 5.0 and the .NET 4.5 Framework (Expert's Voice in .NET)',book_section='C#',author1='Andrew Troelsen ',available=58)
# book1 = Books(book_name='C# in Depth, 3rd Edition',book_section='C#',author1='Jon Skeet',available=58)
# book1 = Books(book_name='C# 5.0 Unleashed',book_section='C#',author1='Bart De Smet',available=58)