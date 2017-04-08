from flask import Flask,render_template
import app
app = Flask(__name__)

@app.route('/')
def hello_world():
    db.hello();
    return render_template("main.html")

@app.route('/login')
def login():
    #add login functionality to database
    if(True):
        return render_template("dashboard.html")
    #else:
        #promt error on login form

@app.route('/signup')
def signup():
    print("Signing up")
    #signup function


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4001, debug=True, threaded=True)
