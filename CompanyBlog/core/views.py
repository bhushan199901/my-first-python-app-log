# core/views

from flask import render_template, request, Blueprint
from CompanyBlog.models import BlogPost

# Blueprint for for better organisation
core = Blueprint('core', __name__)

@core.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    blog_post = BlogPost.query.order_by(BlogPost.date.desc()).paginate(page=page, per_page=5)

    return render_template('index.html', blog_post=blog_post)

@core.route('/info')
def info():
    return render_template('info.html')

