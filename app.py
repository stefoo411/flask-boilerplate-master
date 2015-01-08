from flask import Flask, render_template, request, redirect
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
	print " hello "
	users.insert({'username':'paras2','password':'sucks'})
	return render_template('home.html')

@app.route('/create')
def create():
	users = db.users
	return render_template('createaccount.html', users=users)

@app.route('/surveystats')
def surveystats():
	return render_template('surveystats.html')

@app.route('/change')
def chance():
	return redirect('/')

@app.route('/post', methods=['GET','POST'])
def post():
	if request.method == 'POST':
		return render_template('post.html')
	return render_template('get.html')

@app.route('/login', methods=['GET','POST'])
def login():
	users = db.users
	users = users.find({})
	return render_template('get.html',users=users)

@app.route('/newaccount', methods=['GET', 'POST'])
def newaccount():
	if request.method == 'POST':
		user_name = request.form.get('username')
		if user_name is None:
				return render_template('createaccount.html', error="Cannot leave username blank")

		users.insert({'name':user_name.strip()})
		return redirect('/methodname')
	return render_template("createaccount.html")

if __name__ == '__main__': #main method
	port = int(os.environ.get('PORT', 8000)) #connects to local host, which is where we're currently running the website locally.
	app.run(host='0.0.0.0', port=port,debug=True) #just starts running the website.
