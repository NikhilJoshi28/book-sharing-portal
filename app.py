import gc, hashlib, content_management
#from MySQLdb import escape_string as

from flask import Flask, render_template, request, url_for, redirect, session
from passlib.hash import sha256_crypt
from wtforms import StringField, validators, PasswordField, Form

from dbconnect import connection
from content_management import Content, searchContent, searchByID

app = Flask(__name__)
app.secret_key = 'beae135cce92ebf432b043c193ccf78eb8a986f8f9febcb7f14f64ba6bc9c387'

class RegistrationForm(Form):
    bitsid = StringField('bitsid', [validators.DataRequired(), validators.Length(min=12, max=15)])
    password = PasswordField('New Password', [validators.DataRequired(),validators.EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password')
    name = StringField('Name', [validators.DataRequired(), validators.Length(min=5,max=50)])
    phoneno = StringField('PhoneNo',[validators.DataRequired(), validators.text_type(int),validators.Length(min=10,max=12)])
    roomno = StringField('RoomNo',[validators.DataRequired(), validators.Length(min=4,max=7)])
    facebook = StringField('FaceLink',[validators.Length(min=10,max=100)])

BOOK_DETAILS= Content()

def sumSessionCounter():
  try:
    session['counter'] += 1
  except KeyError:
    session['counter'] = 1

@app.route('/')
def index():
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
            #password = str(sha256_crypt.encrypt((str(form.password.data))))
            password = str((form.password.data))
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
                c.execute("INSERT INTO users VALUES ( %s, %s)", ((userid),(password)))
                c.execute("INSERT INTO userdetailes VALUES ( %s, %s, %s, %s, %s)",((userid),(username),(phoneno),(roomno),(facebookid)))
                conn.commit()
                print "data added"
                c.close()
                conn.close()
                gc.collect()

                session['logged_in'] = True
                session['userID'] = userid
                print session['userID'] + "this is in register"
                return redirect(url_for('dashboard'))

        else:
            print "555"

        return render_template("register.html", form=form)

    except Exception as e:
        print "****"
        print e

@app.route('/login/', methods=['GET','POST'])
def login():
        try:
            if request.method == "POST":
                attempted_username = request.form['username']
                attempted_password = request.form['password']
                #passEnc = str(sha256_crypt.encrypt((str(attempted_password))))
                passEnc = str(attempted_password)
                print attempted_password
                print attempted_username

                c, conn = connection()
                x = c.execute("SELECT * FROM users WHERE uid= %s", (attempted_username,))
                if int(x>0):
                    c.execute("SELECT password FROM users WHERE uid= %s", (attempted_username,))
                    data = c.fetchall()
                    for row in data:
                        print row[0], passEnc
                        if passEnc == row[0]:
                            session['logged_in'] = True
                            session['userID'] = attempted_username
                            return redirect(url_for('dashboard'))
                    else:
                        print "invalid credentials"
                else:
                    print "user doesnot exist"

            return render_template("main.html")

        except Exception as e:
            print e
        return render_template("main.html")

@app.route('/dashboard/', methods=['GET','POST'])
def dashboard():
    try:
        if request.method == "POST":
            bookname = request.form['bookname']
            author = request.form['author']
            edition = request.form['edition']
            avlstatus = (int)(request.form['avlstatus'])
            userID = str(session['userID'])
            bookID = hashlib.sha1(str(bookname+userID).encode("UTF-8")).hexdigest()[:20]

            c, conn = connection()

            c.execute("INSERT INTO bookdetails VALUES ( %s, %s, %s, %s, %s, %s)",
                      ((bookID), (bookname), (author), (edition), (int)(avlstatus), (userID)))
            conn.commit()
            print "data added"
            print session['userID'] + "this is in addBook, book is added"
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

@app.route('/booksShared/', methods=['POST'])
def booksShared():
    if request.method == "POST":
        BOOK_DETAILS=searchByID(session['userID'])
    return render_template("dashboard.html", Book_details=BOOK_DETAILS)

if __name__=='__main__':
      app.run(host='0.0.0.0', port=4141, debug=True, threaded=True)
