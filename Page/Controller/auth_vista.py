from flask import Blueprint,render_template

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register')
def register():
    return render_template('auth_template/register.html')


@bp.route('/login')
def login():
    return render_template('auth_template/login.html')
