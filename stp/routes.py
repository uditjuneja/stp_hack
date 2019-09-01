import request
from flask import Flask, request, redirect, url_for, render_template, flash
from flask_login import login_user, current_user, logout_user, login_required, \
                        logout_user
from werkzeug import secure_filename
from stp import app, db, bcrypt
from .models import users, posts, startups, investors, incubators, analysis

@app.route("/")
def index():
    posts_all = posts.query.all()
    return render_template("index.html", posts=posts_all)

#####################################################################
#  About
#####################################################################
@app.route("/about")
def about():
    return render_template("about/about_stp.html")

@app.route("/about/cm")
def about_cm():
    return render_template("about/cm.html")

@app.route("/response_map")
def response_map():
    return render_template("map.html")


#####################################################################
#  Explore
#####################################################################
@app.route("/explore")
def explore():
    startups_all = startups.query.all()
    return render_template("explore/startups.html", startups=startups_all )

@app.route("/explore/investor")
def explore_investor():
    investors_all = investors.query.all()
    return render_template("explore/investors.html", investors=investors_all)

@app.route("/explore/incubator")
def explore_incubator():
    incubators_all = incubators.query.all()
    return render_template("explore/incubators.html", incubators=incubators_all)

@app.route("/explore/mentor")
def explore_mentor():
    mentors_all = mentors.query.all()
    return render_template("explore/mentors.html", mentors=mentors_all)


#####################################################################
#  Events
#####################################################################
@app.route("/events")
def events():
    return render_template("events/hackathons.html")


#####################################################################
#  Forms
#####################################################################
@app.route("/form/startup", methods=['GET', 'POST'])
@login_required
def form_startup():
    if not current_user.is_authenticated:
        return redirect(url_for('index'))

    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return 'file uploaded successfully'

        if startups.query.filter_by(company=request.form['company']).first():
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
                    description=request.form['description'],
                    image_file=f.filename)
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
        if investors.query.filter_by(name=request.form['name']).first():
            flash('The name is already taken.', 'danger')
            return redirect(url_for('form_investor'))

        investor =investors(name=request.form['name'],
                            city=request.form['city'],
                            investment=request.form['investment'],
                            desc=request.form['desc'])
        db.session.add(investor)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template("forms/investor.html")

@app.route("/form/incubator", methods=['GET', 'POST'])
@login_required
def form_incubator():
    if not current_user.is_authenticated:
        return redirect(url_for('index'))
    if request.method == 'POST':
        incubator = incubators(name=request.form['name'],
                    location=request.form['location'],
                    seats=request.form['seats'],
                    startup_incubated=request.form['startup_incubated'],
                    funding=request.form['funding'])
        db.session.add(incubator)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template("forms/incubator.html")

@app.route("/form/form")
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
                    content=content)
        flash('Heading and Content are required!!', 'danger')
        return redirect(url_for('index'))
    return render_template("forms/post.html")


#####################################################################
#  Dash
#####################################################################
@app.route("/dash")
def dash():
    item = analysis.query.first()
    return render_template("dash/main.html", item=item)

@app.route("/dash/2")
def dash_rank_2():
    item = analysis.query.filter_by(id=1).first()
    return render_template("dash/main.html", item=item)

@app.route("/dash/1")
def dash_rank_1():
    item = analysis.query.filter_by(id=2).first()
    return render_template("dash/main.html", item=item)

@app.route("/dash/3")
def dash_rank_3():
    item = analysis.query.filter_by(id=3).first()
    return render_template("dash/main.html", item=item)

@app.route("/dash/4")
def dash_rank_4():
    item = analysis.query.filter_by(id=4).first()
    return render_template("dash/main.html", item=item)

#####################################################################
#  User
#####################################################################
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
