from flask_wtf import FlaskForm
from wtforms import StringField, validators, SelectMultipleField, SubmitField, TextAreaField


class CreateArticleForm(FlaskForm):
    title = StringField("Title", [validators.DataRequired()])
    body = TextAreaField('Body', [validators.DataRequired()])
    submit = SubmitField('Publish')
    tags = SelectMultipleField('Tags', coerce=int)
