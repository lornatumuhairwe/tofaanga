from flask import render_template, request,flash, sessions, redirect, url_for
from app import app
from app import models
from app import bucketlistmodel

@app.route('/test') #my test route
def testroute():
	return render_template("inde.html")

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if email in models.users:
            loginuser = models.BucketListApp(email, password)
            if loginuser.login() == 'Logged in':
                print ('Logged in user is')
                print (models.logged_in)
                user_bucketlists = bucketlistmodel.User(models.logged_in[0]).view_user_bucketlist(models.logged_in[0])
                print ('Logged in user has these bucket lists')
                print (user_bucketlists)
                return render_template("bucketlists.html", user_bucketlists=user_bucketlists)
            else:
                flash('Password Incorrect')
                return render_template("login.html")
        else:
            flash('Unknown user')
            return render_template("signup.html")
    return render_template("login.html")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method =='POST':
        name = request.form['name']
        email = request.form['email']
        dob = request.form['dob']
        password = request.form['password']
        cpassword = request.form['cpassword']
        createuser = models.BucketListApp(email, password, name, dob,  cpassword)
        print (createuser.signup())
        return render_template('login.html')
    else:
        return render_template("signup.html")

@app.route('/logout')
def logout():
    models.logged_in[0] = None
    print (models.logged_in)
    return redirect(url_for('login'))#a redirect is best

@app.route('/bucketlists', methods=['GET', 'POST'])
def home():
    user_bucketlists = bucketlistmodel.User(models.logged_in[0]).view_user_bucketlist(models.logged_in[0])
    print ('Logged in user has these  bucketlists')
    print (user_bucketlists)
    return render_template("bucketlists.html", user_bucketlists=user_bucketlists)

@app.route('/addbucketlist', methods=['POST'])
def addBucketlist():
    if request.method =='POST':
        name = request.form['name']
        create_bucket_list = bucketlistmodel.User(models.logged_in[0])
        print (create_bucket_list.create_user_bucketlist(name))
        return redirect(url_for('home'))
        #return render_template("bucketlists.html")

@app.route('/bucketlists/<int:bucketlistID>/delete', methods=['POST', 'GET'])
def deleteBucketlist(bucketlistID):
    if request.method == 'POST':
        name = request.form['name']
        user_bucketlists = bucketlistmodel.User(models.logged_in[0]).delete_bucketlist(bucketlistmodel.current_user_bucketlists[bucketlistID])
        return redirect(url_for('home'))

@app.route('/bucketlists/<int:bucketlistID>', methods=['GET', 'POST'])
def view_items_in_bucketlist(bucketlistID):
    if request.method =='GET':
        user_bucketlists = bucketlistmodel.User(models.logged_in[0]).view_user_bucketlist(models.logged_in[0])
        print ('Logged in user has these  bucketlists')
        print (user_bucketlists)
        bucketlist = bucketlistmodel.current_user_bucketlists[bucketlistID]
        print (bucketlistmodel.User(models.logged_in[0]))
        items = bucketlistmodel.User(models.logged_in[0]).view_items_in_bucketlist(bucketlist)
        if not items:
            return render_template("bucketlists.html", items=items, user_bucketlists=user_bucketlists)
            #return redirect(url_for('home', items = []))
        else:
            print ("items in bucketlist are: ")
            print (items)
            return render_template("bucketlists.html", items = items)
            #return redirect(url_for('home', items = items))
    elif request.method == 'POST':
        bucketlist = bucketlistmodel.current_user_bucketlists[bucketlistID]
        activity = request.form['activity']
        deadline = request.form['deadline']
        status = request.form['status']
        details = [status, deadline]
        print ("details are ")
        print (details)
        print(bucketlistmodel.User(models.logged_in[0]).add_item_to_bucketlist(bucketlist, activity, details))
        return redirect(url_for('home'))
