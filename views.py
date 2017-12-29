from main import app
from flask import render_template, request, url_for, redirect, flash
from models import User, Politics, Technology, General, Entertainment, Sport 
from formhandler import LoginForm, RegisterForm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from sqlalchemy.exc import IntegrityError
from main import db
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from datetime import datetime
from flask_mail import Mail, Message
from flask_sqlalchemy import SQLAlchemy 

mail = Mail(app)
s = URLSafeTimedSerializer('My_Biggest_Secret')




login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



@app.route('/')
def index():
	post = General.query.order_by(General.date_posted.desc()).first()

	#return post[0].post_title
	#return post.post_title

	
	return render_template('index.html',post=post)


@app.route('/Political-Upadates')
def politics():
	return render_template('politics.html')


@app.route('/Sports-Updates')
def Sport():
	return render_template('sport.html')

@app.route('/Technology-Updates')
def Technology():
	return render_template('tech.html')


@app.route('/Entertainment-Updates')
def Entertainment():
	return render_template('entertainment.html')


@app.route('/registration', methods=['GET', 'POST'])
def registration():
	form = RegisterForm()

	if form.validate_on_submit():
		try:
			hashed_password = generate_password_hash(form.password.data, method='sha256')
			new_user = User(first_name=form.first_name.data, last_name=form.last_name.data, phone_number=form.phone.data,email=form.email.data,User_Address=form.address.data,Country=form.country.data,Referal_email=form.referal_email.data,password=hashed_password)
			db.session.add(new_user)
			db.session.commit()
			email = form.email.data
			token = s.dumps(email, salt='email-confirm')
			msg = Message('Confirm Email', sender='Admin@natterworld.com', recipients=[email])
			link = url_for('confirm_email', token=token, _external=True)
			msg.body = 'Your link is {}'.format(link)
			mail.send(msg)
		except IntegrityError:
			return "Someone as already sign up with that email"

		return '<h1>New user has been created! check your email address </h1>' 

	return render_template('registration.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user:
			if check_password_hash(user.password, form.password.data):
				login_user(user, remember=form.remember.data)
				return redirect(url_for('dashboard'))

			return '<h1>Invalid username or password</h1>'
	return render_template('login.html', form=form)

@app.route('/dashboard')
@login_required
def dashboard():

	#timeshow = datetime.now()
	#timeshow = (str(timeshow))
	#return current_user.email + timeshow
	#query.filter_by(current_user.email)
	#user = User.query.filter_by(current_user.email).first()
	#current_login = User(current_login_at = datetime.now())
	
	#db.session.add(current_login)
	#db.session.commit()
	
	mail=current_user.email
	fname = current_user.first_name
	lname =  current_user.last_name
	userbalance = current_user.user_balance
	content_posted = current_user.post_counter
	posthandler = current_user.daily_post
	
	
	if posthandler == 10:
		email = current_user.email
		my_user = db.session.query(User).filter_by(email=email).first()
		if my_user is None:
			pass
		my_user.withdraw="yes"
		db.session.add(my_user) #this doesn't create a new user, it updates the existing
		db.session.commit()
		post_availability = "Not Available"
		return render_template('dashboard.html',mail=mail, fname=fname, lname=lname, userbalance=userbalance, content_posted=content_posted, post_availability=post_availability)
	email = current_user.email
	my_user = db.session.query(User).filter_by(email=email).first()
	if my_user is None:
		pass
	my_user.withdraw="no"
	db.session.add(my_user) #this doesn't create a new user, it updates the existing
	db.session.commit()
	post_availability = "Available"
		#return render_template('dashboard.html',mail=mail, fname=fname, lname=lname, userbalance=userbalance, content_posted=content_posted, post_availability=post_availability)

	return render_template('dashboard.html',mail=mail, fname=fname, lname=lname, userbalance=userbalance, content_posted=content_posted, post_availability=post_availability)



@app.route('/confirm_email/<token>')

def confirm_email(token):
    try:
        email = s.loads(token, salt='email-confirm', max_age=3600)
    except SignatureExpired:
        return '<h1>The token is expired!</h1>'

   
    #db.session.commit()
    return render_template('authetication.html')
    #flash('Your Account is Confirmed')
    #return redirect(url_for('dashboard'))
@app.route('/authetication', methods=['GET', 'POST'])
def authetication():
	if request.method == 'POST':
		email = request.form['email']
		my_user = db.session.query(User).filter_by(email=email).first()
		if my_user is None:
			pass
		db.session.add(my_user)
		my_user.confirmed_at=datetime.now()
		db.session.add(my_user) #this doesn't create a new user, it updates the existing
		db.session.commit() # saved.
		return "your account is verified"
	return render_template('authetication.html')

@app.route('/profile')
@login_required
def profile():
	mail=current_user.email
	fname = current_user.first_name
	lname =  current_user.last_name
	userbalance = current_user.user_balance
	content_posted = current_user.post_counter
	posthandler = current_user.daily_post
	address = current_user.User_Address
	phone_number = current_user.phone_number


	mail=current_user.email
	fname = current_user.first_name
	lname =  current_user.last_name
	userbalance = current_user.user_balance
	content_posted = current_user.post_counter
	posthandler = current_user.daily_post
	
	
	if posthandler == 10:
		email = current_user.email
		my_user = db.session.query(User).filter_by(email=email).first()
		if my_user is None:
			pass
		my_user.withdraw="yes"
		db.session.add(my_user) #this doesn't create a new user, it updates the existing
		db.session.commit()
		post_availability = "Not Available"
		return render_template('my-profile.html' ,mail=mail, fname=fname, lname=lname, userbalance=userbalance, content_posted=content_posted, address=address, phone_number=phone_number, post_availability=post_availability )
	email = current_user.email
	my_user = db.session.query(User).filter_by(email=email).first()
	if my_user is None:
		pass
	my_user.withdraw="no"
	db.session.add(my_user) #this doesn't create a new user, it updates the existing
	db.session.commit()
	post_availability = "Available"

	



	return render_template('my-profile.html' ,mail=mail, fname=fname, lname=lname, userbalance=userbalance,post_availability=post_availability, content_posted=content_posted, address=address, phone_number=phone_number)



@app.route('/cashout')
@login_required
def cashout():
	if current_user.post_counter == 10 and current_user.withdraw == 'yes':
		return 'you can withdraw your money'
	current_user.post_counter < 10 and current_user.withdraw == 'no'
	return 'you are not eligable'





######################################Posting News And Monitoring Code#####################################
@app.route('/post')
@login_required
def posts():

	mail=current_user.email
	fname = current_user.first_name
	lname =  current_user.last_name
	userbalance = current_user.user_balance
	content_posted = current_user.post_counter
	posthandler = current_user.daily_post

	if posthandler == 10:
		email = current_user.email
		my_user = db.session.query(User).filter_by(email=email).first()
		if my_user is None:
			pass
		my_user.withdraw="yes"
		db.session.add(my_user) #this doesn't create a new user, it updates the existing
		db.session.commit()
		post_availability = "Not Available"
		return render_template('postcontent.html',mail=mail, fname=fname, lname=lname, userbalance=userbalance, content_posted=content_posted, post_availability=post_availability)
	email = current_user.email
	my_user = db.session.query(User).filter_by(email=email).first()
	if my_user is None:
		pass
	my_user.withdraw="no"
	db.session.add(my_user) #this doesn't create a new user, it updates the existing
	db.session.commit()
	post_availability = "Available"
	return render_template('postcontent.html',content_posted=content_posted,posthandler=posthandler,userbalance=userbalance,post_availability=post_availability)




@app.route('/addpost', methods=['POST'])
def addpost():
	posttype = request.form['posttype']
	post_title = request.form['posttitle']
	posted_by = request.form['postedby']
	location = request.form['postlocation']
	#file_attach = request.files['']
	content = request.form['content']

	email = current_user.email
	my_user = db.session.query(User).filter_by(email=email).first()
	if posttype == 'politics' and my_user.post_counter < 10 and my_user.daily_post < 10 and my_user.daily_post < 1000 :
		post = Politics(post_type=posttype,post_title=post_title, posted_by=posted_by, location=location, content=content, date_posted=datetime.now())
		db.session.add(post)
		email = current_user.email
		my_user = db.session.query(User).filter_by(email=email).first()
		if my_user is None:
			pass

		
		#counting =  my_user.post_counter + 1
		#counting =str(counting)
		my_user.post_counter += 1
		my_user.daily_post += 1
		my_user.user_balance += 100 
		#my_user.post_counter=counts 
		db.session.add(my_user) #t
		db.session.commit()
		return "Posted" + posted_by
	
	#my_user.withdraw = "yes"
	#db.session.add(my_user) #t
	#db.session.commit()
	#return 'You no more eligiable please wait for the next 24hours and withdraw yor money'

			
		
	
		
	email = current_user.email
	my_user = db.session.query(User).filter_by(email=email).first()	
	if posttype == 'general' and my_user.post_counter < 10 and my_user.daily_post < 10 and my_user.daily_post < 1000  :
		post = General(post_type=posttype,post_title=post_title, posted_by=posted_by, location=location, content=content, date_posted=datetime.now())
		db.session.add(post)
		db.session.commit()

		email = current_user.email
		my_user = db.session.query(User).filter_by(email=email).first()
		if my_user is None:
			pass

		
		#counting =  my_user.post_counter + 1
		#counting =str(counting)
		my_user.post_counter += 1
		my_user.daily_post += 1
		my_user.user_balance += 100 
		#my_user.post_counter=counts 
		db.session.add(my_user) #t
		db.session.commit()
		return "Posted" + posted_by

	email = current_user.email
	my_user = db.session.query(User).filter_by(email=email).first()
	if posttype == 'entertainment' and my_user.post_counter < 10 and my_user.daily_post < 10 and my_user.daily_post < 1000 :
		post = Entertainment(post_type=posttype,post_title=post_title, posted_by=posted_by, location=location, content=content, date_posted=datetime.now())
		db.session.add(post)
		email = current_user.email
		my_user = db.session.query(User).filter_by(email=email).first()
		if my_user is None:
			pass

		
		#counting =  my_user.post_counter + 1
		#counting =str(counting)
		my_user.post_counter += 1
		my_user.daily_post += 1
		my_user.user_balance += 100 
		#my_user.post_counter=counts 
		db.session.add(my_user) #t
		db.session.commit()
		return "Posted" + posted_by
		
	email = current_user.email
	my_user = db.session.query(User).filter_by(email=email).first()	
	if posttype == 'sport' and my_user.post_counter < 10 and my_user.daily_post < 10 and my_user.daily_post < 1000  :
		post = Sport(post_type=posttype,post_title=post_title, posted_by=posted_by, location=location, content=content, date_posted=datetime.now())
		db.session.add(post)
		db.session.commit()
		return "Posted" + posted_by


	email = current_user.email
	my_user = db.session.query(User).filter_by(email=email).first()	
	if posttype == 'tech' and my_user.post_counter < 10 and my_user.daily_post < 10 and my_user.daily_post < 1000 :
		post = Technology(post_type=posttype,post_title=post_title, posted_by=posted_by, location=location, content=content, date_posted=datetime.now())
		db.session.add(post)
		db.session.commit()

		email = current_user.email
		my_user = db.session.query(User).filter_by(email=email).first()
		if my_user is None:
			pass

		
		#counting =  my_user.post_counter + 1
		#counting =str(counting)
		my_user.post_counter += 1
		my_user.daily_post += 1
		my_user.user_balance += 100 
		#my_user.post_counter=counts 
		db.session.add(my_user) #t
		db.session.commit()
		flash("Thank You Content Posted")
		return redirect(url_for('dashboard'))
	else:
		return'post type is not selected or not available'


@app.route('/sport/<int:post_id>')
def post(post_id):
    post = Sport.query.filter_by(id=post_id).one()

    return render_template('post.html', post=post)

@app.route('/entertainment/<int:post_id>')
def EntPost(post_id):
    post = Entertainment.query.filter_by(id=post_id).one()

    return render_template('post.html', post=post)


@app.route('/create')
@app.before_first_request
def before_first_request():
	# db.drop_all()
	db.configure_mappers()
	db.create_all()
	return "database created"

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))	