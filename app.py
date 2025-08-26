from flask import Flask, render_template, request
app= Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form.get('username')
        print(username)
        return f"<h1>Username: {username} foi recebido!</h1>"
    else:
        return render_template('index.html')