from flask import Flask,render_template,request,flash,redirect,url_for,session
from flask_wtf import Form
from wtforms import BooleanField,StringField,PasswordField,validators
from passlib.hash import sha256_crypt
from MySQLdb import escape_string as thwart
import gc

from scripts import dbconnect
from content_management import Content

BOOK_DETAILS= Content()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("main.html")

@app.route('/login/')
def login_page():
    return render_template("login.html")

#@app.route('dash-board/')
@app.route('/dashboard/')
def dashboard():
    #add login functionality to database
    if(True):
       return render_template("dashboard.html",Book_details=BOOK_DETAILS)
    #else:
        #promt error on login form

@app.route('/signup/', methods=["GET","POST"])
def signup():
    try:

        if request.method == "POST" and form.validate():
            username = form.username.data
            email = form.email.data
            password = sha256_crypt.encrypt((str(form.password.data)))
            c, conn = dbconnect.connection()

            x = c.execute("SELECT * FROM users WHERE username = (%s)",
                          (thwart(username)))

            if int(x) > 0:
                flash("That username is already taken, please choose another")
                return render_template('main.html', form=form)

            else:
                c.execute("INSERT INTO credentials (uid, password, email, tracking) VALUES (%s, %s, %s, %s)",
                          (thwart(username), thwart(password), thwart(email),
                           thwart("/introduction-to-python-programming/")))

                conn.commit()
                flash("Thanks for registering!")
                c.close()
                conn.close()
                gc.collect()

                session['logged_in'] = True
                session['username'] = username

                return redirect(url_for('dashboard'))

    except Exception as e:
        return (str(e))

@app.errorhandler(404)
def pageNotFound(e):
    return render_template("404.html")

if __name__=='__main__':
      app.run(host='0.0.0.0', port=4141, debug=True, threaded=True)
