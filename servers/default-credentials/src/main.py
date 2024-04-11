# Hack the server
# A group of premade servers that you can hack
# Github://www.github.com/0x4248/hack_the_server
# By: 0x4248

FLAG = "XG48563957GN"

from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = "secret_key"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username == "admin" and password == "password":
        session['username'] = username
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('index'))

@app.route('/admin')
def admin():
    if session['username'] == "admin":
        response = app.response_class(
            response=FLAG,
            status=200,
            mimetype='text/plain'
        )
        return response
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5040)