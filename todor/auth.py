from zipfile import error

from flask import (Blueprint, render_template, flash, request, url_for, redirect, session, g, )
from werkzeug.security import generate_password_hash, check_password_hash
from . import models
from .models import User
from todor import db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User(username, generate_password_hash(password))
        error = None

        user_name  = User.query.filter_by(username = username).first()
        if user_name == None:
            db.session.add(user)
            db.session.commit()
            return  redirect(url_for('auth.login'))
        else:
            error = f"El usuario {username} ya existe!"

            flash(error)

    return render_template('auth/registrar.html')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        error = None
        # Validar datos de usuario
        user = User.query.filter_by(username = username).first()
        if user is None:
            error = 'El nombre de usuario es incorrecto'
        elif not check_password_hash(user.password, password):
            error = 'La contraseña es incorrecta'

        # iniciar sesion
        if error is None:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('todo.index'))

        flash(error)
    return render_template('auth/login.html')


@bp.before_request
def load_logged_in_user():
    user_id = session.get('user_id')
    print(f"el usuario es: {user_id}  okkkk")
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get_or_404(user_id)

