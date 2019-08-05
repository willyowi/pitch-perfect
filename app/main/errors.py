from flask import render_template
from . import main
from .. import db

@main.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404

@main.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'),500