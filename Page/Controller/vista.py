from flask import Blueprint

bp = Blueprint('vista', __name__, url_prefix='/vista')


@bp.route('/lista')
def index():
    return "Lista de tareas"


@bp.route('/create')
def create():
    return "Tarea"
