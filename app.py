from flask import Flask, render_template, url_for, request, redirect, Response, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from werkzeug.security import generate_password_hash, check_password_hash
import io
import random
import sqlite3 as sql
import database

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_ERI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = "random string"
db = SQLAlchemy(app)

# 157.230.63.172 
@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        stock_info = request.form['content']
    return render_template('index.html')


@app.route("/stocks", methods=['POST', 'GET'])
def stocks():
    if request.method == 'POST':
        stock_info = request.form['content']
    return render_template('stocks.html')


@app.route("/contact", methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        stock_info = request.form['content']
    return render_template('contact.html')

@app.route("/about", methods=['POST', 'GET'])
def about():
    if request.method == 'POST':
        stock_info = request.form['content']
    return render_template('about.html')


@app.route("/login", methods=['POST', 'GET'])
def login():
    return render_template('login.html')
    #if request.method == 'POST':
    #stock_info = request.form['content']

@app.route('/loginAttempt', methods=['POST', 'GET'])
def loginAttempt():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        '''
        #Check if user is in database by select *
        try:
            con = sql.connect("database.db")
            con.row_factory = sql.Row
    
            cur = con.cursor()
            cur.execute("select * from users")

            rows = cur.fetchall()
            data = 0
            for row in rows:
                if username in row:
                    data = 1

            if data == 1:
                print("User found")
            else:
                print("User not found")
        except:
            print("Something went wrong with method 1")
        finally:
            print("Finished with method 1")'''

        #Check if user is in database
        try:
            con = sql.connect("database.db")
            con.row_factory = sql.Row
    
            cur = con.cursor()
            cur.execute('SELECT * FROM users WHERE username=?', (username,))
            row = cur.fetchone()

            data = 0
            if row is not None:
                if username in row:
                    data = 1
            
            #User found in the database
            if data == 1:
                print("User found")

            else:
                print("User not found")

        except:
            print("Something went wrong finding the user in the database")
        finally:
            print("Finished finding user in database")
        msg = "login successful"
        return render_template("result.html", msg = msg)
    else:
        msg = "idk"
        return render_template("result.html", msg = msg)

@app.route("/signup", methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        stock_info = request.form['content']
    return render_template('sign-up.html')

@app.route("/signupAttempt", methods=['POST', 'GET'])
def signupAttempt():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['id'] or not request.form['email'] or not request.form['password'] or not request.form['password2']:
            flash('All fields are required for signing up', 'error')
            return render_template('sign-up.html')
        
        try:
            name = request.form['name']
            username = request.form['id']
            email = request.form['email']
            password = request.form['password']
            password2 = request.form['password2']

            #Check if passwords match
            if password != password2:
                flash('Passwords do not match', 'error')
                msg="Passwords do not match"
                return render_template('sign-up.html')

            #Check if username already exists
            if usernameExists(username):
                flash('Username already exists', 'error')
                msg="Username already exists"
                return render_template('sign-up.html')

            #Check if email already exists
            if emailExists(email):
                flash('Username already exists', 'error')
                msg="Email already exists"
                return render_template('sign-up.html')
            
            insertUser(name, username, email, password)
            msg = "Signup successful"
        except:
            msg = "Something went wrong"
            con.rollback()

        finally:
            return render_template("result.html", msg = msg)
            con.close()

@app.route("/index2", methods=['POST', 'GET'])
def index2():
    if request.method == 'POST':
        stock_info = request.form['content']
    return render_template('index2.html')

@app.route('/list')
def list():
    con = sql.connect("database.db")
    con.row_factory = sql.Row
    
    cur = con.cursor()
    cur.execute("select * from users")
    
    rows = cur.fetchall(); 
    return render_template("list.html",rows = rows)

@app.route("/mypage", methods=['POST', 'GET'])
def mypage():
    if request.method == 'POST':
        stock_info = request.form['content']
    return render_template('mypage.html')


@app.route('/plot.png')
def plot_png():
    getvar = "postwas"
    fig = create_figure("Stock", 5)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

def create_figure(Stock, Time):
    #lr = LinearRegression()
    #lr.predict(Stock, Time)
    fig = Figure()
    axis = fig.add_subplot(1,1,1)
    xs = range(6)
    ys = [random.randint(1,50) for x in xs]
    axis.plot(xs, ys)
    return fig

def usernameExists(username):
    #Check if username is already in database
    try:
        con = sql.connect("database.db")
        con.row_factory = sql.Row

        cur = con.cursor()
        cur.execute('SELECT * FROM users WHERE username=?', (username,))
        row = cur.fetchone()

        data = 0
        if row is not None:
            if username in row:
                data = 1
        
        #User found in the database
        if data == 1:
            return True
        #User not found in the database
        else:
            return False

    except:
        print("Something went wrong when attempting to find the user in the database")
    finally:
        print("Finished finding user in database")

def emailExists(email):
    #Check if email is already in database
    try:
        con = sql.connect("database.db")
        con.row_factory = sql.Row

        cur = con.cursor()
        cur.execute('SELECT * FROM users WHERE email=?', (email,))
        row = cur.fetchone()

        data = 0
        if row is not None:
            if email in row:
                data = 1
        
        #Email found in the database
        if data == 1:
            return True
        #Email not found in the database
        else:
            return False

    except:
        print("Something went wrong when attempting to find the email in the database")
    finally:
        print("Finished finding email in database")

def insertUser(name, username, email, password):
#Insert new user into table
    try:
        with sql.connect("database.db") as con:
            cur = con.cursor()

            #hash password using sha256
            hashedPassword = generate_password_hash(password, method='sha256')

            #insert user into table
            cur.execute("INSERT INTO users (name, username, email, password) VALUES (?, ?, ?, ?)", (name, username, email, hashedPassword))
            con.commit()
    except:
        print("Something went wrong attempting to insert user into database")
    finally:
        print("Successfully inserted user into database")


if __name__ == "__main__":
    app.run(debug=True)
