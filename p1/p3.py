from p1 import db
from p1.models import Books,User
d=User.query.all()
for i in d:
	print(i.username)