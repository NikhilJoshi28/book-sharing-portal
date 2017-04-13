import gc, hashlib
#from MySQLdb import escape_string as

from flask import Flask, render_template, request, url_for, redirect, session
from passlib.hash import sha256_crypt
from wtforms import StringField, validators, PasswordField, Form

from dbconnect import connection
from content_management import Content, searchContent

app = Flask(__name__)

class RegistrationForm(Form):
    bitsid = StringField('bitsid', [validators.DataRequired(), validators.Length(min=12, max=15)])
    password = PasswordField('New Password', [validators.DataRequired(),validators.EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password')
    name = StringField('Name', [validators.DataRequired(),   validators.Length(min=5,max=50)])
    phoneno = StringField('PhoneNo',[validators.DataRequired(), validators.text_type(int),validators.Length(min=10,max=12)])
    roomno = StringField('RoomNo',[validators.DataRequired(), validators.Length(min=4,max=7)])
    facebook = StringField('FaceLink',[validators.Length(min=10,max=100)])

BOOK_DETAILS= Content()

@app.route('/', methods=["GET","POST"])
def index():
    try:
        if request.method == "POST":
            attempted_username = request.form['username']
            attempted_password = request.form['password']

            print attempted_password
            print attempted_username

            c ,conn = connection()
            getpassword = str(c.execute("SELECT password FROM users WHERE uid= %s",(attempted_username,)))
            print getpassword

            c.close()
            conn.close()

            if (attempted_username=="admin" and attempted_password=="password") or (sha256_crypt.verify(attempted_password,getpassword)):
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

@app.route('/dashboard/', methods=['GET','POST'])
def dashboard():
    try:
        if request.method == "POST":
            bookname = request.form['bookname']
            author = request.form['author']
            edition = request.form['edition']
            avlstatus = (int)(request.form['avlstatus'])
            bookID = hashlib.sha1(bookname.encode("UTF-8")).hexdigest()[:20]

            c, conn = connection()

            c.execute("INSERT INTO bookdetails VALUES ( %s, %s, %s, %s, %s)",
                      ((bookID), (bookname), (author), (edition), (int)(avlstatus)))
            conn.commit()
            print "data added"
            c.close()
            conn.close()
            gc.collect()

        return render_template("dashboard.html", Book_details=BOOK_DETAILS)

    except Exception as e:
        print e
    return render_template("dashboard.html", Book_details=BOOK_DETAILS)

@app.route('/register_confirm/')
def confirmation():
    return render_template("registration_confirm.html")

@app.errorhandler(404)
def pageNotFound(e):
    return render_template("404.html")

@app.route('/search/', methods=['POST'])
def search():
    if request.method == "POST":
        query = request.form['search']
        print query
        BOOK_DETAILS=searchContent(query)
    return render_template("dashboard.html", Book_details=BOOK_DETAILS)
if __name__=='__main__':
      app.run(host='0.0.0.0', port=4141, debug=True, threaded=True)
