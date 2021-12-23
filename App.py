import os
from flask import Flask
from flask import render_template
from flask import send_from_directory


app = Flask(__name__)
 
@app.route('/')
def Index():
    return render_template('index.html') 

@app.route('/about')
def about():
    return '<h1>About</h1>'

@app.route('/contact')
def contact():
    return 'Contact'

@app.route('/login')
def login():
    return 'login' 


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)
    
