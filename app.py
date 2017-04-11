from flask import Flask,render_template
from scripts import db
from content_management import Content

BOOK_DETAILS= Content()

app = Flask(__name__)

@app.route('/')
def hello_world():
    db.hello();
    return render_template("main.html")

#@app.route('dash-board/')
@app.route('/dashboard/')
def dashboard():
    #return ("hello dashboard")
    #add login functionality to database
    if(True):
       return render_template("dashboard.html",Book_details=BOOK_DETAILS)
    #else:
        #promt error on login form

@app.route('/signup')
def signup():
    print("Signing up")
    #signup function


if __name__=='__main__':
      app.run(host='0.0.0.0', port=4141, debug=True, threaded=True)
