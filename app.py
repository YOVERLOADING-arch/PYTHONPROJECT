import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # For flashing messages

# Function to initialize the database and create the User table if it doesn't exist
def init_db():
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    
    # Enable foreign key support
    cursor.execute('PRAGMA foreign_keys = ON')
    
    # Create User table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS User (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')
    
    # Create User_info table with a foreign key referencing the User table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS User_info (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            dob TEXT NOT NULL,
            address TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES User(id) ON DELETE CASCADE
        )
    ''')
    
    conn.commit()
    conn.close()

# Route for EventHorizon
@app.route('/')
def EventHorizon():
    return render_template('EventHorizon.html')

# Route for Signup Page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM User WHERE username=?", (username,))
        existing_user = cursor.fetchone()
        if existing_user:
            flash('Username already exists', 'error')
            conn.close()
            return redirect(url_for('signup'))

        cursor.execute("INSERT INTO User (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        conn.close()

        flash('Account created successfully! You can now log in.', 'success')
        return redirect(url_for('login'))

    return render_template('signup.html')

# Route for Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM User WHERE username=? AND password=?", (username, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            flash('Login successful!', 'success')
            return redirect(url_for('home'))  # Redirect to home page after login
        else:
            flash('Invalid username or password', 'error')
            return redirect(url_for('login'))

    return render_template('login.html')

# Route for Home Page (Main Front Page)
@app.route('/home')
def home():
    return render_template('home.html')

# Route for User Info Page

@app.route('/user-info', methods=['GET', 'POST'])
def user_info():
    if request.method == 'POST':
        name = request.form['name']
        dob = request.form['dob']
        address = request.form['address']

        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()

        # Insert data into the User_info table, specifying the columns
        cursor.execute("INSERT INTO User_info (user_id, name, dob, address) VALUES ((SELECT id FROM User WHERE username=?), ?, ?, ?)",
                       (name, dob, address))
        conn.commit()
        conn.close()

        flash('Information submitted successfully!', 'success')
        return redirect(url_for('home'))

    return render_template('userinfo.html')

# Event Category Routes
@app.route('/concerts')
def concerts():
    return render_template('concerts.html')

@app.route('/parties')
def parties():
    return render_template('parties.html')

@app.route('/seminars')
def seminars():
    return render_template('seminars.html')

@app.route('/webinars')
def webinars():
    return render_template('webinars.html')

@app.route('/hackathons')
def hackathons():
    return render_template('hackathons.html')

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
