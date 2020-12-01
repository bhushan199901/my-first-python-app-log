# users/Forms
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from CompanyBlog.models import User


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class Register(FlaskForm):
    Email = StringField('Email', validators=[DataRequired(), Email()])
    Username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password',
                             validators=[DataRequired(), EqualTo('pass_confirm', message='passwords must match')])
    pass_confirm = PasswordField('Confirm Password', validators=[DataRequired()])
    Submit = SubmitField('Register')

    def check_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already exists,Try a new one or Login')

    def check_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('username already exists,Try a new one or Login')


class Update(FlaskForm):
    Email = StringField('Email', validators=[DataRequired(), Email()])
    Username = StringField('Username', validators=[DataRequired()])
    picture = FileField('update Profile Picture ', validators=[FileAllowed(['jpg', 'png'])])
    Submit = SubmitField('Update details')
