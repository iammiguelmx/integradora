from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/maps')
def maps():
    return render_template('maps.html')

if __name__ == '__main__':
    # Add obtain information
    app.run(port=5000, debug=True)