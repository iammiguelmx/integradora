from flask import Flask
from flask import request
from flask import url_for
from flask import make_response
from flask import redirect
from flask import render_template
from flask import current_app
from flask import request
import urllib



FACEBOOK_APP_ID = '110626275752351'
FACEBOOK_APP_SECRET = 'a6d52ed9f11260e72c70b0c5432266f3'

# Creacion de instance
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('login.html')

@app.route('/maps')
def maps():
    return render_template('maps.html')

@app.route('/index')
def login():
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/forgot')
def forgot():
    return render_template('forgot-password.html')

if __name__ == '__main__':
    app.run(port=5000, debug=True)