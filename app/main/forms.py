from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField, StringField, SelectField
from wtforms.validators import Required


class UpdateProfile(FlaskForm):
    bio=TextAreaField('Add or update your bio', validators=[Required()])
    submit=SubmitField('Submit')

class AddBlog(FlaskForm):
    title=StringField('Title', validators=[Required()])
    content= TextAreaField('Content', validators=[Required()])
    submit=SubmitField('Add a blog')

class CommentForm(FlaskForm):
    comment=TextAreaField("Comment on this blog", validators=[Required()])
    submit=SubmitField('Submit comment')


    