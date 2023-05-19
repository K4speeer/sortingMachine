from flask import render_template, Blueprint, url_for

views = Blueprint('views', __name__)

@views.route('/')
@views.route('/home')
def home_page():
    return render_template('index.html')


@views.route('/sign-up')
def signup_page():
    return render_template('sign-up.html')


@views.route('/connect')
def connect():
    return render_template('connect.html')


