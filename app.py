from flask import Flask,render_template, flash,request,url_for,redirect
from scripts import dbconnect
from content_management import Content
from flask_wtf import Form
from wtforms import BooleanField,validators,StringField,PasswordField


class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=20)])
    email = StringField('Email Address', [validators.Length(min=6, max=50)])
    password = PasswordField('New Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the Terms of Service and Privacy Notice (updated Jan 22, 2015)',
                              [validators.Required()])

BOOK_DETAILS= Content()

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def index():
    try:
        if request.method == "POST":
            attempted_username = request.form['username']
            attempted_password = request.form['password']
            print attempted_password
            print attempted_username

            if attempted_username=="admin" and attempted_password=="password":
                return redirect(url_for('dashboard'))
            else:
                print "invalid credentials"

        return render_template("main.html")

    except Exception as e:
        print e
    return render_template("main.html")

@app.route('/login/', methods=['GET','POST'])
def login_page():
        try:
            if request.method == "POST":
                attempted_username = request.form['username']
                attempted_password = request.form['password']
                print attempted_password
                print attempted_username

                if attempted_username == "admin" and attempted_password == "password":
                    return redirect(url_for('dashboard'))
                else:
                    print "invalid credentials"

            return render_template("login.html")

        except Exception as e:
            print e
        return render_template("login.html")

    #return render_template("login.html")

#@app.route('dash-board/')
@app.route('/dashboard/')
def dashboard():
    #flash("Flash !! test")
    #add login functionality to database
    if(True):
       return render_template("dashboard.html",Book_details=BOOK_DETAILS)
    #else:
        #promt error on login form

@app.route('/signup/', methods=["GET","POST"])
def signup():
    try:
        c, conn = dbconnect.connection()
        print("okay")
        return("okay")
    except Exception as e:
        return(str(e))

@app.errorhandler(404)
def pageNotFound(e):
    return render_template("404.html")

if __name__=='__main__':
      app.run(host='0.0.0.0', port=4141, debug=True, threaded=True)
