# Hack the server
# A group of pre made servers that you can break
# Github://www.github.com/lewisevans2007/hack_the_server
# By: Lewis Evans

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