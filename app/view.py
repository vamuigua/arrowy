from flask import render_template, flash, redirect
from app import app

@app.route('/')
@app.route('/<user>')
def home(user=None):
    return render_template("user.html",user = user)

@app.route('/about')
def about():
    return render_template("about.html",about = about)

@app.route('/contact')
def contact():
    return render_template("contact.html",contact = contact)

@app.route('/register')
def register():
    return render_template("register.html",register = register)

@app.route('/data')
def data():
    return render_template("data.html",data = data)