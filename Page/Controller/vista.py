from flask import Blueprint, render_template, request, redirect, url_for, g
from Page.Controller.auth_vista import login_required

bp = Blueprint('tareas_vista', __name__, url_prefix='/tareas_vista')


@bp.route('/lista')
@login_required
def index():
    from Page.Models.modelo import User, Tareas
    from Page import db
    tareas = Tareas.query.all()

    return render_template('tareas/index.html', tareas=tareas)


@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create_tarea():
    from Page.Models.modelo import User, Tareas
    from Page import db
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        state = False
        tarea = Tareas(title, desc, state, g.user.id)

        db.session.add(tarea)
        db.session.commit()
        return redirect(url_for('tareas_vista.index'))

    return render_template('tareas/create.html')


def get_tareas(id):
    from Page.Models.modelo import Tareas
    tarea = Tareas.query.get_or_404(id)
    return tarea


@bp.route('/edit/<int:id>', methods=('GET', 'POST'))
@login_required
def edit_tarea(id):
    from Page.Models.modelo import Tareas
    from Page import db
    tarea = Tareas.query.get_or_404(id)

    if request.method == 'POST':
        tarea.title = request.form['title']
        tarea.desc = request.form['desc']
        tarea.state = True if request.form.get('state') == 'on' else False

        db.session.commit()

        return redirect(url_for('tareas_vista.index'))

    return render_template('tareas/update.html', tarea=tarea)


@bp.route('/delete/<int:id>', methods=('GET', 'POST'))
@login_required
def delete_tarea(id):
    from Page.Models.modelo import Tareas
    from Page import db

    tarea = Tareas.query.get_or_404(id)

    if request.method == 'POST':
        tarea.is_active = 0
        db.session.commit()
        return redirect(url_for('tareas_vista.index'))

    return render_template('tareas/delete.html', tarea=tarea)
