from dbutils import MONGO_URI
from dbutils import db_connect
from dbutils import db_insert_user
from dbutils import db_find_all
from form import EmailForm
from form import LoginForm
from form import RegisterForm
from flask import Flask
from flask import request
from flask import render_template
from flask import url_for
from flask import make_response
from flask import redirect
from flask import current_app

# Creacion de instance
app = Flask(__name__)
register = db_connect(MONGO_URI, 'mi_app', 'register')

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    flag = False
    name = None

    if len(form.errors):
        print(form.errors)
    if request.method == 'POST':
        fistname = form.fistname.data
        lastname = form.lastname.data
        mail = form.mail.data
        password = form.password.data
        confirmpass = form.confirmpass.data
        if fistname != '' and lastname != '':
            print(f"Fistname capturado: {fistname}")
            print(f"Lastname capturado: {lastname}")
            print(f"Mail capturado: {mail}")
            print(f"Password capturado: {password}")
            print(f"Confirmpass capturado: {confirmpass}")
            user = {
                "fistname": fistname,
                "lastname": lastname,
                "mail": mail,
                "password": password,
                "confirmpass": confirmpass
            }
            db_insert_user(register, user)
            flag = True
            
    return render_template('register.html', flag=flag, name=name)

@app.route('/maps')
def maps():
    return render_template('maps.html')

@app.route('/index')
def login():
    return render_template('index.html')

@app.route('/forgot')
def forgot():
    return render_template('forgot-password.html')

@app.errorhandler(404)
def no_encontrado(error=None):
    return render_template("404.html", url=request.url)

if __name__ == '__main__':
    app.run(port=5000, debug=True)