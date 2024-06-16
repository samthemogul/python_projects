from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)

DATABASE = 'guestbook.db'

# For tests
app.secret_key = 'secret'

def get_db():
    conn = sqlite3.connect(DATABASE)
    return conn

@app.route('/', methods=['GET', 'POST'])
def index():
    
    
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Backend Validation
        if not name or not email or not message:
            flash('Please fill out all fields.', 'error')
        else:
            db = get_db()
            cursor = db.cursor()
            cursor.execute('INSERT INTO guests (name, email, message) VALUES (?, ?, ?)', (name, email, message))
            db.commit()  
            flash('Entry added successfully!', 'success') 

        return redirect(url_for('index'))
    
    if request.method == 'GET':
        db = get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM guests')
        entries = cursor.fetchall()
        return render_template('index.html', entries=entries)

    return render_template('index.html')