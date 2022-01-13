from flask import Flask,  request, redirect, url_for, session
from flask import render_template
from backend.cfg import config




app = Flask(__name__)
app.config.from_object(config())
mysql = MySQL(app)

class Account:
    def __init__(self, id, username):
        self.id = id
        self.username = username
        self.password = None
        self.email = None
        self.usertype = None
        
    def getId(self):
        return self.id
    
    def getUsername(self):
        return self.username
    
    def getPassword(self):
        return self.password
    
    def getEmail(self):
        return self.email
    
    def getUsertype(self):
        return self.usertype
    
    def setId(self, id):
        self.id = id
    
    def setUsername(self, username):
        self.username = username
    
    def setPassword(self, password):
        self.password = password
    
    def setEmail(self, email):
        self.email = email
    
    def setUsertype(self, usertype):
        self.usertype = usertype
    
