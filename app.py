import gc
#from MySQLdb import escape_string as

from flask import Flask, render_template, request, url_for, redirect, session
from passlib.hash import sha256_crypt
from wtforms import StringField, validators, PasswordField, Form

from dbconnect import connection
from content_management import Content


class RegistrationForm(Form):
    bitsid = StringField('bitsid', [validators.DataRequired(), validators.Length(min=12, max=15)])
    #email = StringField('Email Address', [validators.Length(min=6, max=50)])
    password = PasswordField('New Password', [validators.DataRequired(),validators.EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password')
    name = StringField('Name', [validators.DataRequired(),   validators.Length(min=5,max=50)])
    phoneno = StringField('PhoneNo',[validators.DataRequired(), validators.text_type(int),validators.Length(min=10,max=12)])
    roomno = StringField('RoomNo',[validators.DataRequired(), validators.Length(min=4,max=7)])
    facebook = StringField('FaceLink',[validators.Length(min=10,max=100)])
    #accept_tos = BooleanField('I accept the Terms of Service and Privacy Notice (updated Jan 22, 2015)',
    #                          [validators.DataRequired()])


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


@app.route('/register/', methods=["GET","POST"])
def registration():
    print "###"
    try:
        form = RegistrationForm(request.form)
        print "@@@"
        if request.method == "POST":
            print "&&&&"
            userid = str(form.bitsid.data)
            username = str(form.name.data)
            password = str(sha256_crypt.encrypt((str(form.password.data))))
            phoneno = str(form.phoneno.data)
            roomno = str(form.roomno.data)
            facebookid = str(form.facebook.data)
            c, conn = connection()
            print userid

            x = c.execute("SELECT * FROM users WHERE uid= %s",(userid,))
            print x
            if int(x) > 0:
                print "Username Already taken"
                return render_template('register.html', form=form)
            else:
                c.execute("INSERT INTO users VALUES ( %s, %s, %s)", ((userid),(username),(password)))
                c.execute("INSERT INTO userdetailes VALUES ( %s, %s, %s, %s, %s)",((userid),(username),(phoneno),(roomno),(facebookid)))
                conn.commit()
                print "data added"
                c.close()
                conn.close()
                gc.collect()

                #session['logged_in'] = True
                #session['username'] = username
                return redirect(url_for('dashboard'))

        else:
            print "555"

        return render_template("register.html", form=form)

    except Exception as e:
        print "****"
        print e

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
        c, conn = connection()
        print("okay")
        return("okay")
    except Exception as e:
        return(str(e))

@app.route('/register_confirm/')
def confirmation():
    return render_template("registration_confirm.html")

@app.errorhandler(404)
def pageNotFound(e):
    return render_template("404.html")

if __name__=='__main__':
      app.run(host='0.0.0.0', port=4141, debug=True, threaded=True)
