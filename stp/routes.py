import request
from flask import Flask, request, redirect, url_for, render_template, flash
from flask_login import login_user, current_user, logout_user, login_required, \
                        logout_user

from stp import app, db, bcrypt
from .models import users, posts, startups

@app.route("/")
def index():
    posts_all = posts.query.all()
    return render_template("index.html", posts=posts_all)

@app.route("/about")
def about():
    return render_template("about/about_stp.html")

# @app.route("/about/cm_message")
# def about_cm():
#     return render_template("about_cm.html")
#
# @app.route("/about/faq")
# def about_faq():
#     return render_template("about_faq.html")
#
# @app.route("/about")
# def about_stp():
#     return render_template("about_stp.html")


<<<<<<< HEAD
@app.route("/form/startup")
@login_required
def form_startup():
    return render_template("forms/startup.html")

@app.route("/form/form", methods=['GET', 'POST'])
=======
@app.route("/form/startup", methods=['GET', 'POST'])
@login_required
def form_startup():
    if not current_user.is_authenticated:
        return redirect(url_for('index'))

    if request.method == 'POST':
        print ("In post", request.form['company'])
        print ()
        print ()
        print ()
        print ()

        if users.query.filter_by(name=request.form['company']).first():
            flash('The name is already taken.', 'danger')
            return redirect(url_for('startup'))

        startup = startups(name=request.form['username'],
                    email=request.form['email'],
                    website=request.form['website'],
                    contact=request.form['contact'],
                    age=request.form['age'],
                    country=request.form['country'],
                    address=request.form['Address'],
                    zipCode=request.form['zipcode'],
                    description=request.form['description'])
        db.session.add(startup)
        db.session.commit()
        flash('Your startup has been registered', 'success')
        return redirect(url_for('index'))

    return render_template("forms/startup.html")


@app.route("/form/investor", methods=['GET', 'POST'])
@login_required
def form_investor():
    if not current_user.is_authenticated:
        return redirect(url_for('index'))

    if request.method == 'POST':

        investor = investors(name=request.form['name'],
                    city=request.form['city'],
                    investment=request.form['investment'],
                    desc=request.form['desc'])

        db.session.add(investor)
        db.session.commit()
        return redirect(url_for('index'))
        return render_template("forms/investor.html")


@app.route("/form/form")
>>>>>>> 0983959db048e9a9f5c195e198f619e43354cc4f
@login_required
def form_post():
    if current_user.user_priority != 1:
        return url_for('index')

    if request.method == 'POST':
        title = request.form['title']
        heading = request.form['heading']
        content = request.form['content']

        if heading == "" or content == "":
            flash('Heading and Content are required!!', 'danger')
            return redirect(url_for('form_post'))

        post = posts(title = title,
                    heading=heading,
                    content=content,


        )
        flash('Heading and Content are required!!', 'danger')
        return redirect(url_for('index'))


    return render_template("forms/post.html")

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

        user = users.query.filter_by(username=username).first()
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
        if users.query.filter_by(email=request.form['email']).first():
            flash('The email is already registered with an account.', 'danger')
            return redirect(url_for('register'))
        if users.query.filter_by(username=request.form['username']).first():
            flash('The username is already taken.', 'danger')
            return redirect(url_for('register'))

        hashed_password = bcrypt.generate_password_hash(request.form['pass']).decode('utf-8')
        user = users(username=request.form['username'],
                    email=request.form['email'],
                    phone_no=request.form['phone_no'],
                    company=request.form['company'],
                    password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))

    else:
        return render_template("register.html")

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))
