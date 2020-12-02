# views to be created
from flask import render_template, url_for, request, Blueprint, redirect, flash
from flask_login import login_user, logout_user, current_user, login_required
from CompanyBlog import db
from CompanyBlog.models import User, BlogPost
from CompanyBlog.users.forms import Register, LoginForm, Update
from CompanyBlog.users.picture_handler import add_profilepic

users = Blueprint('users', __name__)


# register

@users.route('/register',methods=['GET', 'POST'])
def register():
    form = Register()

    if form.validate_on_submit():
        user = User(email=form.Email.data,
                    username=form.Username.data,
                    password=form.password.data)

        db.session.add(user)
        db.session.commit()
        flash('Thanks for registering')
        return redirect(url_for('users.login'))

    return render_template('register.html', form=form)


# login
@users.route('/login', methods=['GET','POST'])
def login():
    message = ""
    form = LoginForm()
    if form.validate_on_submit():
        try:
            user = User.query.filter_by(email=form.email.data).first()
            if User.check_password(user, password=form.password.data) and user is not None:
                login_user(user)
                message = "Login Success"
                return redirect(url_for('core.index'))
            else:
                message = "wrong password"
        except AttributeError:
            message = "Values entered is not correct"

    return render_template('login.html', form=form, error=message)

# logout
@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('core.index'))


# user account view ( update info )
@users.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = Update()

    if form.validate_on_submit():
        print(form)
        if form.picture.data:
            username = current_user.username
            picture = add_profilepic(form.picture.data, username)
            current_user.profile_image = picture

            current_user.username = form.Username.data
            current_user.email = form.Email.data
            db.session.commit()
            flash('user account updated')
            return redirect(url_for('users.account'))

    elif request.method == "GET":
            form.Username.data = current_user.username
            form.Email.data = current_user.email

    profile_image = url_for('static', filename='profile_pics/'+current_user.profile_image)
    return render_template('account.html', profile_image=profile_image, form=form)


# Login blogpost view
@users.route('/<username>')
def userposts(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    blog_posts = BlogPost.query.filter_by(author=user).order_by(BlogPost.date.desc().paginate(page=page, per_page=3))
    return render_template('user_blog_posts.html', blog_posts=blog_posts, user=user)


