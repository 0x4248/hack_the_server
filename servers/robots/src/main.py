# Hack the server
# A group of premade servers that you can hack
# Github://www.github.com/lewisevans2007/hack_the_server
# By: Lewis Evans

FLAG = "BA58365926GZ"

ROBOTS = """User-agent: *
Allow: /
Disallow: /flag"""

from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/robots.txt')
def robots():
    response = app.make_response(ROBOTS)
    response.headers["Content-type"] = "text/plain"
    return response

@app.route('/flag')
def flag():
    response = app.make_response(FLAG)
    response.headers["Content-type"] = "text/plain"
    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5040)