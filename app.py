from flask import Flask, render_template, request, redirect, flash
import jinja2 #jinja2 is a python based templating language, so we can render the html templates easily.
import os
from pymongo import *

app = Flask(__name__) #creates an flask instances

app.secret_key = 'kbwkfwbhwbhk'
client = MongoClient('mongodb://survistefoo:survi@ds051110.mongolab.com:51110/survi') #establishes connection to mongodb server
db = client.get_default_database()  
users = db.users

@app.route('/')
def hello():
	#users.insert({'username':'paras2','password':'sucks'})
	return render_template('home_start.html')

@app.route('/search')
def search():
	users = db.users
	return render_template('search.html', users=users)

@app.route('/newsurveys')
def newsurveys():
	users = db.users
	return render_template('newsurveys.html', users=users)

@app.route('/endingsurveys')
def endingsurveys():
	users = db.users
	return render_template('endingsurveys.html', users=users)

@app.route('/monthlylottery')
def monthlylottery():
	users = db.users
	return render_template('monthlylottery.html', users=users)

@app.route('/edit')
def edit():
	users = db.users
	return render_template('edit.html', users=users)

@app.route('/history')
def history():
	users = db.users
	return render_template('history.html', users=users)

@app.route('/surveystats')
def surveystats():
	return render_template('surveystats.html')

@app.route('/accountsettings')
def accountsettings():
	users = db.users
	return render_template('accountsettings.html', users=users)

@app.route('/formresponsecheck')
def formload():
	return render_template('formresponsecheck.html')
	
#@app.route('/accountsettings', methods=['POST'])
#def accountsettings_post():
#	if request.method == 'POST':
#		user_name = request.form.getlist('username[]')
#		password = request.form.getlist('password[]')
#		if user_name == "":
#			print "Error: Please enter a username"
#			return render_template('accountsettings.html')
#		if password == "":
#			print "Error: Please enter a password"
#			return render_template('accountsettings.html')
#		users = db.users
#		user_exists = users.find({'username': user_name})
#		if user_exists == NULL:
#			users.insert({'username': user_name, 'password': password})
#		return redirect('/')
#	return render_template('createaccount.html')

@app.route('/post', methods=['GET','POST'])
def post():
	if request.method == 'POST':
		return render_template('post.html')
	return render_template('get.html')

@app.route('/home_login')
def home_login():
	return render_template('home_login.html')

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
	users = db.users
	if request.method == 'POST':
		user_name = request.form.get('username')
		pass_word = request.form.get('password')
		flash(user_name,,category='error')
		#user_exists = users.find({"username": user_name, "password": pass_word})
#		if (user_exists is not None):
#				flash("user_exists" + user_exists + ".", category='error')
#				return render_template('home_login.html')
#		elif (user_exists == None):
#			return redirect('/')
		#for user in users:
		#	if (user == user_name):
		#		if (pass_word == user.find('password')): #find or get?
		#			return render_template('home_login.html')
		#		elif (pass_word != user.get('password')): #find or get?
		#			flash('Please enter the correct username and password.', category='error')
		#	elif (user != user_name):
		#		flash('Username not found.', category='error')
	return render_template('login.html')
#	return render_template('get.html', users=users)

@app.route('/newaccount')
def newaccount():
	return render_template('createaccount.html')

@app.route('/newaccount', methods=['POST'])
def newaccount_post():
	if request.method == 'POST':
		user_name = request.form.get('username')
		password = request.form.get('password')
		if user_name == '':
			flash("Please enter a username.", category='error')
			return render_template('createaccount.html')
		elif password == '':
			flash("Please enter a password.", category='error')
			return render_template('createaccount.html')
		users = db.users
		user_exists = users.find({'username': user_name})
		if (user_exists is not None):
			flash("That username already exists.", category='error')
			return render_template('createaccount.html')
		else:
			users.insert({'username': user_name, 'password': password})
			return redirect('/')
	return render_template('createaccount.html')

@app.route('/createsurvey')
def createsurvey():
	return render_template('createsurvey.html')

if __name__ == '__main__': #main method
	port = int(os.environ.get('PORT', 8000)) #connects to local host, which is where we're currently running the website locally.
	app.run(host='0.0.0.0', port=port,debug=True) #just starts running the website.
