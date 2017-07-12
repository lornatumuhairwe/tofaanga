from flask import render_template
from app import app

@app.route('/test') #my test route
def testroute():
	return render_template("inde.html")

@app.route('/')
def login():
	return render_template("login.html")

@app.route('/signup')
def signup():
	return render_template("signup.html")

@app.route('/home')
def home():
	return render_template("bucketlists.html")
