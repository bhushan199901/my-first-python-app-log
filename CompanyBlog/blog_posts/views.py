# blogposts/views.py
from flask import render_template, url_for, request, redirect, Blueprint, flash, abort
from flask_login import current_user, login_required

from CompanyBlog.models import db
from CompanyBlog.models import BlogPost
from CompanyBlog.blog_posts.forms import BlogPostForm

blog_posts = Blueprint('blog_posts', __name__)


# create a blog post
@blog_posts.route('/create', methods=['GET','POST'])
@login_required
def create_post():
    form = BlogPostForm()

    if form.validate_on_submit():
        blog_post = BlogPost(title=form.title.data, text=form.text.data, user_id=current_user.id)
        db.session.add(blog_post)
        db.session.commit()
        print('blog created')
        return redirect(url_for('core.index'))

    return render_template('create_post.html', form=form)

#view blogpost


@blog_posts.route('/<int:blog_post_id>')
def blog(blog_post_id):
    blog_find = BlogPost.query.get_or_404(blog_post_id)
    return render_template('blog.html', title=blog_find.title,
                                        date=blog_find.date,
                                        post=blog_find)


# update blogpost
@blog_posts.route('/<int:blog_post_id>/update', methods=['GET','POST'])
@login_required
def blog_update(blog_post_id):
    b_update = BlogPost.query.get_or_404(blog_post_id)

    if b_update.author != current_user:
        abort(403)

    form = BlogPostForm()

    if form.validate_on_submit():
        b_update.title = form.title.data
        b_update.text = form.text.data
        db.session.commit()
        print('blog updated')
        return redirect(url_for('blog_posts.blog', blog_post_id=blog_post_id))

    elif request.method == 'GET':
        form.title.data = b_update.title
        form.text.data = b_update.text

    return render_template('create_post.html', form=form, title='Updating')


# Delete a blog post
@blog_posts.route('/<int:blog_post_id>/delete', methods=['GET', 'POST'])
@login_required
def deleteb(blog_post_id):
    d_post = BlogPost.query.get_or_404(blog_post_id)
    if d_post.author != current_user:
        abort(403)
    db.session.delete(d_post)
    db.session.commit()
    print('post deleted')
    return redirect(url_for('core.index'))




