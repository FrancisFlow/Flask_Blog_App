from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField, StringField, SelectField
from wtforms.validators import Required


class UpdateProfile(FlaskForm):
    bio=TextAreaField('Add or update your bio', validators=[Required()])
    submit=SubmitField('Submit')