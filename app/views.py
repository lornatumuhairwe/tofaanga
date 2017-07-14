from flask import render_template, request,flash, sessions, redirect, url_for
from app import app
from app import models
from app import bucketlistmodel

@app.route('/', methods=['GET', 'POST'])
def login():
    """method implementing login"""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if email in models.users:
            loginuser = models.BucketListApp(email, password)
            if loginuser.login() == 'Logged in':
                #models.logged_in[0] is the identifier of the logged in user
                user_bucketlists = bucketlistmodel.User(models.logged_in[0]).view_user_bucketlist(models.logged_in[0])
                # user_bucketlists returns the bucketlists of the logged in user
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
    """method implementing signup"""
    if request.method =='POST':
        name = request.form['name']
        email = request.form['email']
        dob = request.form['dob']
        password = request.form['password']
        cpassword = request.form['cpassword']
        createuser = models.BucketListApp(email, password, name, dob,  cpassword)
        createuser.signup() #creates users with above credentials
        return render_template('login.html')
    else:
        return render_template("signup.html")

@app.route('/logout')
def logout():
    """method implementing logout"""
    models.logged_in[0] = None # replaces logged in user with None
    return redirect(url_for('login'))

@app.route('/bucketlists', methods=['GET', 'POST'])
def home():
    if models.logged_in[0]:
        user_bucketlists = bucketlistmodel.User(models.logged_in[0]).view_user_bucketlist(models.logged_in[0])
        # user_bucketlists returns the bucketlist of the logged in user
        return render_template("bucketlists.html", user_bucketlists=user_bucketlists)
    else:
        return redirect(url_for('login'))

@app.route('/addbucketlist', methods=['POST'])
def addBucketlist():
    """method implementing add bucketlist feature"""
    if models.logged_in[0]:
        if request.method =='POST':
            name = request.form['name']
            create_bucket_list = bucketlistmodel.User(models.logged_in[0])
            create_bucket_list.create_user_bucketlist(name)
            return redirect(url_for('home'))
    else:
        return redirect(url_for('login'))

@app.route('/bucketlists/<int:bucketlistID>/delete', methods=['POST', 'GET'])
def deleteBucketlist(bucketlistID):
    """method implementing delete bucketlist feature"""
    if models.logged_in[0]:
        if request.method == 'POST':
            name = request.form['name']
            user_bucketlists = bucketlistmodel.User(models.logged_in[0]).delete_bucketlist(bucketlistmodel.current_user_bucketlists[bucketlistID])
            return redirect(url_for('home'))
    else:
        return redirect(url_for('login'))


@app.route('/bucketlists/<int:bucketlistID>/update', methods=['POST', 'GET'])
def updateBucketlist(bucketlistID):
    """method implementing delete bucketlist feature"""
    if models.logged_in[0]:
        if request.method == 'POST':
            new_name = request.form['new_name']
            user_bucketlists = bucketlistmodel.User(models.logged_in[0]).update_bucketlist(bucketlistmodel.current_user_bucketlists[bucketlistID], new_name)
            return redirect(url_for('home'))
        elif request.method == 'GET':
            return render_template('editbucketlist.html')
    else:
        return redirect(url_for('login'))


@app.route('/bucketlists/<int:bucketlistID>', methods=['GET', 'POST'])
def view_items_in_bucketlist(bucketlistID):
    """method implementing  feature"""
    if models.logged_in[0]:
        if request.method =='GET':
            user_bucketlists = bucketlistmodel.User(models.logged_in[0]).view_user_bucketlist(models.logged_in[0])
            bucketlist = bucketlistmodel.current_user_bucketlists[bucketlistID]
            items = bucketlistmodel.User(models.logged_in[0]).view_items_in_bucketlist(bucketlist)
            if not items:
                return render_template("bucketlists.html", items=items, user_bucketlists=user_bucketlists)
                # return redirect(url_for('home', items = []))
            else:
                return render_template("bucketlists.html", items=items, user_bucketlists=user_bucketlists)
        elif request.method == 'POST':
            bucketlist = bucketlistmodel.current_user_bucketlists[bucketlistID]
            activity = request.form['activity']
            deadline = request.form['deadline']
            status = request.form['status']
            details = [status, deadline]
            bucketlistmodel.User(models.logged_in[0]).add_item_to_bucketlist(bucketlist, activity, details)
            #adds activity/items to specified bucketlist of current user
            return redirect(url_for('home'))
    else:
        return redirect(url_for('login'))
