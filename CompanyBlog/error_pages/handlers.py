# handlers.py/error_pages
from flask import render_template
from flask import Blueprint

err_pages = Blueprint('err_pages', __name__)


@err_pages.app_errorhandler(404)
def error_404(error):
    return render_template('error_pages/404.html'), 404


@err_pages.app_errorhandler(403)
def error_403(error):
    return render_template('error_pages/403.html'), 403

