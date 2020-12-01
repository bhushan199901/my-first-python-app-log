# blog.posts/forms

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class BlogPostForm(FlaskForm):
    title = StringField('TITLE', validators=[DataRequired()])
    text = TextAreaField('Type here ', validators=[DataRequired()])
    submit = SubmitField('Create Blog')
