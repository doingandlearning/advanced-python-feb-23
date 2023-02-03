import os

import sqlalchemy as sa
from flask import (current_app, flash, redirect, render_template, request,
                   url_for)
from flask_login import current_user, login_required, login_user, logout_user

from project import db
from project.models import User

from . import users_blueprint
from .forms import LoginForm, RegisterForm


# ------
# Routes
# ------

@users_blueprint.route('/profile')
@login_required
def profile():
    return render_template('users/profile.html')


@users_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    # If the User is already logged in, don't allow them to try to register
    if current_user.is_authenticated:
        flash('Already registered!  Redirecting to your User Profile page...')
        return redirect(url_for('users.profile'))

    form = RegisterForm()
    if request.method == 'POST' and form.validate_on_submit():
        new_user = User(form.email.data, form.password.data)

        current_app.logger.info(f"DEBUG001... DATABASE_URL environment variable: {os.getenv('DATABASE_URL')}")
        current_app.logger.info(f"DEBUG002... CONFIG_TYPE environment variable: {os.getenv('CONFIG_TYPE')}")
        current_app.logger.info(f"DEBUG003... SQLALCHEMY_DATABASE_URI: {current_app.config['SQLALCHEMY_DATABASE_URI']}")
        current_app.logger.info(f"DEBUG004... LOG_TO_STDOUT environment variable: {os.getenv('LOG_TO_STDOUT')}")

        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        flash('Thanks for registering, {}!'.format(new_user.email))
        return redirect(url_for('users.profile'))
    return render_template('users/register.html', form=form)


@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    # If the User is already logged in, don't allow them to try to log in again
    if current_user.is_authenticated:
        flash('Already logged in!  Redirecting to your User Profile page...')
        return redirect(url_for('users.profile'))

    form = LoginForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            if user and user.is_password_correct(form.password.data):
                db.session.add(user)
                db.session.commit()
                login_user(user, remember=form.remember_me.data)
                flash('Thanks for logging in, {}!'.format(current_user.email))
                return redirect(url_for('users.profile'))

        flash('ERROR! Incorrect login credentials.')
    return render_template('users/login.html', form=form)


@users_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Goodbye!')
    return redirect(url_for('recipes.index'))


@users_blueprint.route('/status')
def status():
    # Check if the database needs to be initialized
    engine = sa.create_engine(current_app.config['SQLALCHEMY_DATABASE_URI'])
    inspector = sa.inspect(engine)

    return render_template(
        'users/status.html',
        database_url=os.getenv('DATABASE_URL'),
        config_type=os.getenv('CONFIG_TYPE'),
        sqlalchemy_database_uri=current_app.config['SQLALCHEMY_DATABASE_URI'],
        log_to_stdout=os.getenv('LOG_TO_STDOUT'),
        database_initialized=inspector.has_table("users")
    )
