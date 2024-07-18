from flask import Blueprint, render_template, request, url_for, redirect, flash
from werkzeug.security import generate_password_hash, check_password_hash

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        from Page.Models.modelo import User
        from Page import db

        user = User(username=username, password=generate_password_hash(password))

        user_name = User.query.filter_by(username=username).first()
        if user_name is None:
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.login'))
        else:
            flash(f'Username already exists{username}')

    return render_template('auth_template/register.html')


@bp.route('/login')
def login():
    return render_template('auth_template/login.html')
