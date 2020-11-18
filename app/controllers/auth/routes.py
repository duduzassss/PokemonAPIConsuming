from flask import render_template, request, redirect, flash, url_for
from flask_login import login_user, login_required, logout_user
from app import app, db, lm

from app.models.models import User

from .forms import RegisterForm, LoginForm


@lm.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()


@app.route('/register', methods=['GET','POST'])
def register_post():
    form = RegisterForm()
    print(form.validate_on_submit())
    print(form.password.data)
    if form.validate_on_submit():
        try:  
            user = User( username = form.username.data,
                         password = form.password.data ) 
            db.session.add(user)
            db.session.commit()
            flash('Successfully registered', 'success')
            return redirect('/')
            
        except:
            flash('User is already registered', 'danger')
            return redirect('/')
        
        
    return render_template('auth/register.html', form = form)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        u = User.query.filter_by(username = form.username.data).first()
        if u and u.password == form.password.data:
            login_user(u)
            flash('Logged in successfully.', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid login.','danger')
            return redirect(url_for('login'))
    return render_template('auth/login.html', form = form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out.', 'warning')
    return redirect(url_for('index'))
    