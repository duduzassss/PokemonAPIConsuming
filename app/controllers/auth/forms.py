from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, length, EqualTo

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()], render_kw={'autocomplete': 'off'})
    password = PasswordField('Password', validators=[DataRequired(), length(min = 4)])
    
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()], render_kw={'autocomplete': 'off'})
    password = PasswordField('Password', validators=[DataRequired(), length(min = 4)])