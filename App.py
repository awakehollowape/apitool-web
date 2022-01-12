import os
from flask import Flask, flash, request, redirect, url_for, session
from flask import render_template
import backend.auth as auth



app = Flask(__name__)

app.secret_key = '15441109'


# <------------------ MAIN --------------->#
    
@app.route('/')
def Index():
    if 'loggedin' in session:
        return redirect(url_for('profile'))
    return render_template('index/index.html') 

# <------------------ AUTH --------------->#

app.add_url_rule('/login', view_func=auth.login, methods=['GET', 'POST'])

app.add_url_rule('/register', view_func=auth.register, methods=['GET', 'POST'])

app.add_url_rule('/logout', view_func=auth.logout, methods=['GET', 'POST'])


# <------------------ DASHBOARD --------------->#

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard/dashboard.html')

@app.route('/profile')
def profile():
    return render_template('profile.html', username=session['username'],id=session['id'])

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080,debug=True)