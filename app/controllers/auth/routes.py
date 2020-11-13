from flask import render_template
from app import app

from .forms import RegisterForm

@app.route('/register', methods=["GET"])
def register_get():
    form = RegisterForm()
    return render_template('auth/register.html', form = form)

@app.route('/register', methods=["POST"])
def register_post():
    form = RegisterForm()
    return render_template('auth/register.html', form = form)