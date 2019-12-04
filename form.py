from wtforms import Form
from wtforms import StringField
from wtforms import IntegerField
from wtforms.validators import DataRequired


class EmailForm(Form):
    name = StringField('name', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])


class LoginForm(Form):
    email = StringField('email', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])


class RegisterForm(Form):
    fistname = StringField('fistname', validators=[DataRequired()])
    lastname = StringField('lastname', validators=[DataRequired()])
    mail = StringField('mail', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])
    confirmpass = StringField('confirmpass', validators=[DataRequired()])


class VoluntariadoForm(Form):
    email = StringField('email', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])
    address = StringField('address', validators=[DataRequired()])
    address2 = StringField('address2', validators=[DataRequired()])
    city = StringField('city', validators=[DataRequired()])
    state = StringField('state', validators=[DataRequired()])
    zip = StringField('zip', validators=[DataRequired()])
    check = StringField('check', validators=[DataRequired()])

class ReporteForm(Form):
    name = StringField('name', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    phone = StringField('phone', validators=[DataRequired()])
    area = StringField('area', validators=[DataRequired()])
    asunto = StringField('asunto', validators=[DataRequired()])
    mensaje = StringField('mensaje', validators=[DataRequired()])
    check = StringField('check', validators=[DataRequired()])
