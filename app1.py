from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return '<h1>Bem-vindo à home!</h1>'

@app.route('/sobre/<num>')
def sobre(num):
    return render_template("index.html", numero=num)