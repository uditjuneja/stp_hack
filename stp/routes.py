import request
from flask import Flask, request, redirect, url_for, render_template, flash
from flask_login import login_user, current_user, logout_user, login_required, \
                        logout_user

from stp import app

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['pass']

        user = User_Byld.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user, remember=True)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('index'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
        return render_template("login.html")

    else:
        return render_template("login.html")

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        # Tests
        key = Key.query.filter_by(key_no=request.form['key']).first()
        if not key and not key.status:
            flash('Error with key.', 'danger')
            return redirect(url_for('register'))
        if User_Byld.query.filter_by(email=request.form['email']).first():
            flash('The email is already registered with an account.', 'danger')
            return redirect(url_for('register'))
        if User_Byld.query.filter_by(username=request.form['username']).first():
            flash('The username is already taken.', 'danger')
            return redirect(url_for('register'))

        hashed_password = bcrypt.generate_password_hash(request.form['pass']).decode('utf-8')
        user = User_Byld(username=request.form['username'],
                    email=request.form['email'],
                    phone_no=request.form['phone_no'],
                    company=request.form['company'],
                    password=hashed_password)
        db.session.add(user)
        key.status=True
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))

    else:
        return render_template("register.html")
