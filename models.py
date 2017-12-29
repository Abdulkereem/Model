from flask_sqlalchemy  import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from main import db



class User(db.Model, UserMixin):
	__name__ = "User"
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(255))
	last_name = db.Column(db.String(255))
	phone_number = db.Column(db.String(255))
	email = db.Column(db.String(255), unique=True)
	User_Address = db.Column(db.String(255))
	Country = db.Column(db.String(255))
	Referal_email = db.Column(db.String(255))
	password = db.Column(db.String(255))
	active = db.Column(db.Boolean())
	confirmed_at = db.Column(db.DateTime())
	last_login_at =  db.Column(db.String(255))
	current_login_at = db.Column(db.String(255))
	last_login_ip = db.Column(db.String(255))
	current_login_ip = db.Column(db.String(255))
	login_count = db.Column(db.String(255))
	post_counter= db.Column(db.Integer, default=0)
	user_balance = db.Column(db.Integer, default=0)
	daily_post = db.Column(db.Integer, default=0)
	withdraw=db.Column(db.String(255))


class General(db.Model):
	__name__ = "General"
	id = db.Column(db.Integer, primary_key=True)
	post_type = db.Column(db.String(20))
	post_title = db.Column(db.String(50))
	posted_by = db.Column(db.String(50))
	location = db.Column(db.String(20))
	content = db.Column(db.Text)
	#attach_image= db.Column(db.LargeBinary)
	date_posted = db.Column(db.DateTime)
	display_name = db.Column(db.String(255))
	post_viewer = db.Column(db.Integer, default=0)
	def __init__(self,post_type,post_title,posted_by,location,content,date_posted,display_name,post_viewer):
		self.post_type = post_type
		self.post_title = post_title
		self.posted_by = posted_by
		self.location = locatation
		self.content = content 
		self.date_posted = date_posted
		self.display_name = display_name
		self.post_viewer = post_viewer


    



class Politics(db.Model):
	__name__ = "Politics"
	id = db.Column(db.Integer, primary_key=True)
	post_type = db.Column(db.String(20))
	post_title = db.Column(db.String(50))
	posted_by = db.Column(db.String(50))
	location = db.Column(db.String(20))
	#attach_image= db.Column(db.LargeBinary)
	content = db.Column(db.Text)
	date_posted = db.Column(db.DateTime)
	display_name = db.Column(db.String(255))
	post_viewer = db.Column(db.Integer, default=0)
	def __init__(self,post_type,post_title,posted_by,location,content,date_posted,display_name,post_viewer):
		self.post_type = post_type
		self.post_title = post_title
		self.posted_by = posted_by
		self.location = locatation
		self.content = content 
		self.date_posted = date_posted
		self.display_name = display_name
		self.post_viewer = post_viewer

class Entertainment(db.Model):
	__name__ = "Entertainment"
	id = db.Column(db.Integer, primary_key=True)
	post_type = db.Column(db.String(20))
	post_title = db.Column(db.String(50))
	posted_by = db.Column(db.String(50))
	location = db.Column(db.String(20))
	#attach_image= db.Column(db.LargeBinary)
	content = db.Column(db.Text)
	date_posted = db.Column(db.DateTime)
	display_name = db.Column(db.String(255))
	post_viewer = db.Column(db.Integer, default=0)
	def __init__(self,post_type,post_title,posted_by,location,content,date_posted,display_name,post_viewer):
		self.post_type = post_type
		self.post_title = post_title
		self.posted_by = posted_by
		self.location = locatation
		self.content = content 
		self.date_posted = date_posted
		self.display_name = display_name
		self.post_viewer = post_viewer

class Sport(db.Model):
	__name__ = 'Sport'
	id = db.Column(db.Integer, primary_key=True)
	post_type = db.Column(db.String(20))
	post_title = db.Column(db.String(50))
	posted_by = db.Column(db.String(50))
	location = db.Column(db.String(20))
	#attach_image= db.Column(db.LargeBinary)
	content = db.Column(db.Text)
	date_posted = db.Column(db.DateTime)
	display_name = db.Column(db.String(255))
	post_viewer = db.Column(db.Integer, default=0)
	def __init__(self,post_type,post_title,posted_by,location,content,date_posted,display_name,post_viewer):
		self.post_type = post_type
		self.post_title = post_title
		self.posted_by = posted_by
		self.location = locatation
		self.content = content 
		self.date_posted = date_posted
		self.display_name = display_name
		self.post_viewer = post_viewer

class Technology(db.Model):
	__name__ = 'Technology'
	id = db.Column(db.Integer, primary_key=True)
	post_type = db.Column(db.String(20))
	post_title = db.Column(db.String(50))
	posted_by = db.Column(db.String(50))
	location = db.Column(db.String(20))
	#attach_image= db.Column(db.LargeBinary)
	content = db.Column(db.Text)
	date_posted = db.Column(db.DateTime)
	display_name = db.Column(db.String(255))
	post_viewer = db.Column(db.Integer, default=0)
	def __init__(self,post_type,post_title,posted_by,location,content,date_posted,display_name,post_viewer):
		self.post_type = post_type
		self.post_title = post_title
		self.posted_by = posted_by
		self.location = locatation
		self.content = content 
		self.date_posted = date_posted
		self.display_name = display_name
		self.post_viewer = post_viewer