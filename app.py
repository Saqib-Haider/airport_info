from flask import Flask, render_template, request, redirect, url_for, flash
import subprocess
import mysql.connector
import os
from dotenv import load_dotenv
from flask import flash, redirect, url_for

app = Flask(__name__)

# Set a secret key for session management (can be any random string)
app.secret_key = 'your_secret_key'

# MySQL Database Connection Configuration
load_dotenv()
db_username = os.getenv("MYSQL_USERNAME")
db_password = os.getenv("MYSQL_PASSWORD")
db_host = os.getenv("MYSQL_HOST")
db_port = os.getenv("MYSQL_PORT")
db_name = os.getenv("MYSQL_DATABASE")

db_config = {
    'user': db_username,
    'password': db_password,
    'host': db_host,
    'database': db_name
}

# Function to fetch data from MySQL database
def fetch_data_from_db():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM flights")  # Replace with your actual table name
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data if data else []

@app.route('/')
def index():
    data = fetch_data_from_db()
    return render_template('index.html', data=data)

@app.route('/extract', methods=['POST'])


def extract_data():
    try:
        # Get the path to the Python executable in your virtual environment
        python_executable = os.path.join(os.path.dirname(__file__), 'airenv', 'Scripts', 'python.exe')  # Windows
        # For macOS/Linux, it would be: os.path.join(os.path.dirname(__file__), 'airenv', 'bin', 'python')

        # Run the ETL script
        subprocess.run([python_executable, 'etl_script.py'], check=True)
        flash('Data extraction successful!', 'success')
    except subprocess.CalledProcessError as e:
        flash('Failed to extract data.', 'error')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
