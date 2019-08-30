import request
from flask import Flask, request, redirect, url_for, render_template, flash
from flask_login import login_user, current_user, logout_user, login_required, \
                        logout_user

from stp import app

@app.route("/")
def index():
    return render_template("index.html")
