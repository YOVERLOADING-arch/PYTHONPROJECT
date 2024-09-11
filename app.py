import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # For flashing messages

# Function to initialize the database and create the User table if it doesn't exist
def init_db():
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS User (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Route for Signup Page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Get form data
        username = request.form['username']
        password = request.form['password']

        # Connect to the database
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()

        # Check if the user already exists
        cursor.execute("SELECT * FROM User WHERE username=?", (username,))
        existing_user = cursor.fetchone()
        if existing_user:
            flash('Username already exists', 'error')
            conn.close()
            return redirect(url_for('signup'))

        # Insert new user into the database
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
        # Get form data
        username = request.form['username']
        password = request.form['password']

        # Connect to the database
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()

        # Check if the user exists and the password is correct
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

# Route for Home Page
@app.route('/home')
def home():
    return 'Welcome to the home page!'

if __name__ == "__main__":
    # Initialize the database
    init_db()
    app.run(debug=True)
