#import requests
from flask import Flask, render_template, request, redirect, flash, session
#from flask.ext.login import LoginManager
#from flask.ext.openid import OpenID
#from config import basedir
import jinja2 #jinja2 is a python based templating language, so we can render the html templates easily.
import os
from pymongo import *

app = Flask(__name__) #creates an flask instances

app.secret_key = 'kbwkfwbhwbhk'
client = MongoClient('mongodb://survistefoo:survi@ds051110.mongolab.com:51110/survi') #establishes connection to mongodb server
db = client.get_default_database()  
users = db.users
#login_manager = LoginManager()
#login_manager.init_app(app)

@app.route('/')
def hello():
	return render_template('home_start.html')

@app.route('/changepassword')
def changepassword():
	users = db.users
	return render_template('changepassword.html', users=users)

@app.route('/changepassword', methods=['POST'])
def changepassword_post():
	if request.method == 'POST':
		user_name = request.form.get('as_username')
		pass_word = request.form.get('as_oldpassword')
		newpassword = request.form.get('as_newpassword')
		confirmpassword = request.form.get('as_confirmpassword')
		if user_name == '':
			flash("Please enter a username.", category='error')
			return render_template('changepassword.html')
		elif pass_word == '':
			flash("Please enter a password.", category='error')
			return render_template('changepassword.html')
		elif newpassword is not confirmpassword:
			flash("Please confirm password.", category='error')
			return render_template('changepassword.html')
		users = db.users
		user_exists = users.find({"username": user_name, "password": pass_word}).count()
		if (user_exists == 1):
			users.update({"username": user_name, "password": pass_word},{"username": user_name, "password": newpassword})
		return redirect('/')
	return render_template('changepassword.html')

@app.route('/createsurvey')
def createsurvey():
	return render_template('createsurvey.html')

@app.route('/edit')
def edit():
	users = db.users
	return render_template('edit.html', users=users)

@app.route('/endingsurveys')
def endingsurveys():
	users = db.users
	return render_template('endingsurveys.html', users=users)

@app.route('/formresponsecheck')
def formload():
	return render_template('formresponsecheck.html')

@app.route('/history')
def history():
	users = db.users
	return render_template('history.html', users=users)

@app.route('/home_login')
def home_login():
	return render_template('home_login.html')

#@app.route("/index")
#def index():
    #msg = Message("Hello",
    #	sender="snowflower411@yahoo.com",
    #	recipients=["stefoo@bergen.org"])
    #msg.body = "Testing"
    #mail.send(msg)

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
	users = db.users
	if request.method == 'POST':
		user_name = request.form.get('username')
		pass_word = request.form.get('password')
		session['username'] = request.form['username']
		user_exists = users.find({"username": user_name, "password": pass_word}).count()
		if (user_exists == 1):
			flash("This user exists.")
			return render_template('home_login.html')
		else:
			flash('Please enter a valid username and password.')
#			print("Please enter a valid username and password.")
	return render_template('login.html')
#	return render_template('get.html', users=users)

@app.route('/logout')
def logout():
	return redirect("/")

@app.route('/monthlylottery')
def monthlylottery():
	users = db.users
	return render_template('monthlylottery.html', users=users)

@app.route('/newaccount')
def newaccount():
	return render_template('createaccount.html')

@app.route('/newaccount', methods=['POST'])
def newaccount_post():
	if request.method == 'POST':
		user_name = request.form.get('username')
		password = request.form.get('password')
		email = request.form.get('email')
		if user_name == '':
			flash("Please enter a username.", category='error')
			return render_template('createaccount.html')
		elif password == '':
			flash("Please enter a password.", category='error')
			return render_template('createaccount.html')
		elif email == '':
			flash("Please enter an email.", category='error')
			return render_template('createaccount.html')
		users = db.users
		user_exists = users.find({'username': user_name}).count()
		if (user_exists >= 1):
			flash("That username already exists.", category='error')
			return render_template('createaccount.html')
		else:
			email_exists = users.find({'email': email}).count()
			if (email_exists >= 1):
				flash("This email is already in use.", category='error')
				return render_template('createaccount.html')
			else:
				users.insert({'username': user_name, 'password': password, 'email': email})
				return redirect('/')
	return render_template('createaccount.html')

@app.route('/newsurveys')
def newsurveys():
	users = db.users
	return render_template('newsurveys.html', users=users)

@app.route('/post', methods=['GET','POST'])
def post():
	if request.method == 'POST':
		return render_template('post.html')
	return render_template('get.html')

@app.route('/search')
def search():
	users = db.users
	return render_template('search.html', users=users)

@app.route('/surveystats')
def surveystats():
	return render_template('surveystats.html')

if __name__ == '__main__': #main method
	port = int(os.environ.get('PORT', 8000)) #connects to local host, which is where we're currently running the website locally.
	app.run(host='0.0.0.0', port=port,debug=True) #just starts running the website.
