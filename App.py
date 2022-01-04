import os
from flask import Flask, flash
from flask import render_template
from flask_mysqldb import MySQL


app = Flask(__name__)
app.config["MYSQL_HOST"] = "databases.000webhost.com"
app.config["MYSQL_USER"] = "id18157936_apitool"
app.config["MYSQL_PASSWORD"] = "8$v<(WUBOEfc}^r9"
app.config["MYSQL_DB"] = "id18157936_test"

mysql = MySQL(app)

 
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
    return render_template('login.html') 


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080,debug=True)
    

