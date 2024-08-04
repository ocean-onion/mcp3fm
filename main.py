from flask import Blueprint, render_template, request
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
@login_required
def home():
    return render_template('home.html', title='Home')
