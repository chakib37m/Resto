from flask import Flask, render_template, redirect, request, session
from cs50 import SQL
from flask_session import Session
from hashlib import sha256
from cryptography.fernet import Fernet

app = Flask(__name__)

db = SQL("sqlite:///resto.db")

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)



key = Fernet.generate_key()
fernet = Fernet(key)



menu = db.execute("SELECT * FROM MENU")


@app.route("/", methods=['GET', 'POST'])
def index():
    try:
        name = db.execute('SELECT name FROM customers WHERE id = ?', session[id])[0][name]
    except:
        name = ''
    return render_template("index.html", menu=menu, name=name)

@app.route("/signup", methods=["POST"])
def singup():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    db.execute('INSERT INTO customers(name, email, password) VALUES(?, ?, ?)', name, email, password)
    return redirect('/login', code=307)
@app.route("/login", methods=["POST"])
def login():
    email = request.get.form("email")
    password = request.get.form("password")
    id = db.execute('SELECT id FROM customers WHERE email=? and password=?', email, password)
    session[id] = id
    return redirect('/')
@app.route("/cart", methods=["POST"])
def cart():
    return id

@app.route("/order", methods=["POST"])
def order():
    return id