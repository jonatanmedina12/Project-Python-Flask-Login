from flask import Blueprint, render_template, request, url_for, redirect, flash, session, g
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

bp = Blueprint('auth', __name__, url_prefix='/auth')


def login_exist(view):
    @wraps(view)
    def wrapped_view(**kwargs):
        if g.get('user') is not None:
            return redirect(url_for('tareas_vista.index'))

        return view(**kwargs)

    return wrapped_view


@bp.route('/register', methods=['GET', 'POST'])
@login_exist
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
            flash(f'EL USUARIO YA EXISTE!: {username}')

    return render_template('auth_template/register.html')


@bp.route('/login', methods=['GET', 'POST'])
@login_exist
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        from Page.Models.modelo import User
        from Page import db

        user_name = User.query.filter_by(username=username).first()
        error = None
        if user_name is None:
            error = "error"
            flash(f'el usuario no existe: {username}')
        elif not check_password_hash(user_name.password, password):
            error = "error"
            flash(f'Contraseña incorrecta')
        if error is None:
            session.clear()
            session['user_id'] = user_name.id
            return redirect(url_for('tareas_vista.index'))

    return render_template('auth_template/login.html')


@bp.before_app_request
def load_logger_in_user():
    from Page.Models.modelo import User

    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get_or_404(user_id)


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


def login_required(view):
    @wraps(view)
    def wrapped_view(**kwargs):
        if g.get('user') is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)

    return wrapped_view
