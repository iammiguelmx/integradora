from dbutils import MONGO_URI
from dbutils import db_connect
from dbutils import db_insert_user
from dbutils import db_insert_vol
from dbutils import db_insert_reporte
from dbutils import db_find_all
from form import EmailForm
from form import LoginForm
from form import RegisterForm
from form import VoluntariadoForm
from form import ReporteForm
from flask import Flask
from flask import request
from flask import render_template

# Creacion de instance
app = Flask(__name__)

# Inserta en la colletion de Usuarios / Registro
users = db_connect(MONGO_URI, 'mi_app', 'users')

# Inserta en colletion de Voluntariado / Voluntariado
voluntariados = db_connect(MONGO_URI, 'mi_app', 'voluntariados')

# Inserta en colletion de Reporte / reporte
reportes = db_connect(MONGO_URI, 'mi_app', 'reporte')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm(request.form)
    login_error = False

    if len(form.errors):
        print(form.errors)
    if request.method == 'POST':
        if form.email.data == 'miguel@gmail.com' and form.password.data == '12':
            return render_template('index.html')
        else:
            login_error = True
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    flag = False
    fistname = None

    if len(form.errors):
        print(form.errors)
    if request.method == 'POST':
        fistname = form.fistname.data
        lastname = form.lastname.data
        mail = form.mail.data
        password = form.password.data
        confirmpass = form.confirmpass.data
        if fistname != '' and lastname != '' and mail != '' and password != '' and confirmpass != '':
            user = {
                "fistname": fistname,
                "lastname": lastname,
                "mail": mail,
                "password": password,
                "confirmpass": confirmpass
            }
            db_insert_user(users, user)
            flag = True
    return render_template('register.html', flag=flag, fistname=fistname)


@app.route('/maps')
def maps():
    return render_template('maps.html')


@app.route('/index')
def login():
    return render_template('index.html')


@app.route('/forgot')
def forgot():
    return render_template('forgot-password.html')


@app.route('/clasificacion')
def clasificacion():
    return render_template('cards.html')


@app.route('/graficas')
def graficas():
    return render_template('/graficas.html')


@app.route('/voluntariado', methods=['GET', 'POST'])
def voluntariado():
    form = VoluntariadoForm(request.form)
    flag = False
    email = None

    if len(form.errors):
        print(form.errors)
    if request.method == 'POST':
        email = form.email.data
        password = form.password.data
        address = form.address.data
        address2 = form.address2.data
        city = form.city.data
        state = form.state.data
        zip = form.zip.data
        check = form.check.data
        if email != '' and password != '' and address != '' and address2 != '' and city != '':
            # print(f"Nombre email: {email}")
            # print(f"password: {password}")
            # print(f"address: {address}")
            # print(f"address2: {address2}")
            # print(f"city: {city}")
            # print(f"state: {state}")
            # print(f"zip: {zip}")
            # print(f"check: {check}")
            voluntariado = {
                "email": email,
                "password": password,
                "address": address,
                "address2": address2,
                "city": city,
                "state": state,
                "zip":  zip,
                "check": check
            }
            db_insert_vol(voluntariados, voluntariado)
            flag = True
    return render_template('voluntariado.html', flag=flag, email=email)


@app.route('/tabla', methods=['GET', 'POST'])
def tabla():
    registered = db_find_all(voluntariados)
    return render_template('/tabla.html', voluntariados=registered)


@app.route('/reporte', methods=['GET', 'POST'])
def reporte():
    form = ReporteForm(request.form)
    flag = False
    name = None

    if len(form.errors):
        print(form.errors)
    if request.method == 'POST':
        name = form.name.data
        email = form.email.data
        phone = form.phone.data
        area = form.area.data
        asunto = form.asunto.data
        mensaje = form.mensaje.data
        check = form.check.data
        if name != '' and email != '' and phone != '' and area != '' and asunto != '':
            #print(f"Name: {name}")
            #print(f"email: {email}")
            #print(f"phone: {phone}")
            #print(f"area: {area}")
            #print(f"mensaje: {mensaje}")
            #print(f"asunto: {asunto}")
            #print(f"ckeck: {check}")
            reporte = {
                "name": name,
                "email": email,
                "phone": phone,
                "area": area,
                "asunto": asunto,
                "mensaje": mensaje,
                "check":  check
            }
            db_insert_reporte(reportes, reporte)
            flag = True
    return render_template('reporte.html', flag=flag, name=name)


@app.errorhandler(404)
def no_encontrado(error=None):
    return render_template("404.html", url=request.url)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
