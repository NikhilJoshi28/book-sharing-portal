from flask import Flask,render_template,request,flash,redirect,url_for,session
from passlib.hash import sha256_crypt
from MySQLdb import escape_string as thwart
import gc, requests

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

@app.route('/signUp/', methods=["GET","POST"])
def signUp():
    try:

        if request.method == "POST":
            uid = request.form['uid']
            password = sha256_crypt.encrypt((str(request.form['password'])))
            c, conn = dbconnect.connection()

            x = c.execute("SELECT * FROM credentials WHERE uid = (%s)",
                          (thwart(uid)))

            if int(x) > 0:
                flash("That username is already taken, please choose another")
                return render_template('main.html')

            else:
                name = request.form['name']
                phno = request.form['phno']
                roomno = request.form['roomno']
                fbid = request.form['fbid']
                c.execute("INSERT INTO credentials (uid, password) VALUES (%s, %s)",
                          (thwart(uid), thwart(password)))
                c.execute("INSERT INTO users (uid, name, phno, roomno, fbid) VALUES (%s, %s, %s, %s, %s)",
                          (thwart(uid), thwart(name), thwart(phno), thwart(roomno), thwart(fbid)))

                conn.commit()
                flash("Thanks for registering!")
                c.close()
                conn.close()
                gc.collect()

                session['logged_in'] = True
                session['uid'] = uid

                return redirect(url_for('dashboard'))

    except Exception as e:
        return (str(e))

@app.errorhandler(404)
def pageNotFound(e):
    return render_template("404.html")

if __name__=='__main__':
      app.run(host='0.0.0.0', port=4141, debug=True, threaded=True)
