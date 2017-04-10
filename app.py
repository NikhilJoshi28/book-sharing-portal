from flask import Flask,render_template
from scripts import dbconnect
app = Flask(__name__)

@app.route('/')
def index():
    dbconnect.hello();
    return render_template("main.html")

@app.route('/login/')
def login_page():
    return render_template("login.html")

#@app.route('dash-board/')
@app.route('/dashboard/')
def dashboard():
    #add login functionality to database
    if(True):
       return render_template("dashboard.html")
    #else:
        #promt error on login form

@app.route('/signup')
def signup():
    print("Signing up")
    #signup function


if __name__=='__main__':
      app.run(host='0.0.0.0', port=4141, debug=True, threaded=True)
