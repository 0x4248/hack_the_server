# Hack the server
# A group of premade servers that you can hack
# Github://www.github.com/0x4248/hack_the_server
# By: 0x4248

FLAG = "FG49573957KB"

from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/410034980239843109384029837428374329019809874320489374')
def flag():
    response = app.make_response(FLAG)
    response.headers["Content-type"] = "text/plain"
    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5040)