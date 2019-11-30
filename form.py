from wtforms import Form
from wtforms import StringField
from wtforms import IntegerField
from wtforms.validators import DataRequired


class EmailForm(Form):
    name = StringField('name', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])

class LoginForm(Form):
    username = StringField('username', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])

class RegisterForm(Form):
    fistname   = StringField('fistname', validators=[DataRequired()])
    lastname    = StringField('lastname', validators=[DataRequired()])
    mail        = StringField('mail', validators=[DataRequired()])   
    password    = StringField('password', validators=[DataRequired()]) 
    confirmpass = StringField('confirmpass', validators=[DataRequired()]) 