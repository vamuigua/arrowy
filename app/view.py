from flask import render_template
import app


@app.route('/')
@app.route('/<user>')
def home(user=None):
    return render_template("user.html", title='Home', user=user)


@app.route('/about')
def about():
    return render_template("about.html", title='About', about=about)


@app.route('/contact')
def contact():
    return render_template("contact.html", title='Contact Us', contact=contact)


@app.route('/register')
def register():
    return render_template("register.html", title='Register', register=register)


@app.route('/data')
def data():
    return render_template("data.html", title='Data', data=data)
