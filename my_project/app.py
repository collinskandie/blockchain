from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import json
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change to a random secret key for production

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_user', methods=['POST'])
def create_user():
    # Get user input from the form
    username = request.form['username']
    email = request.form['email']
    role = request.form['role']

    # Prepare user data
    user_data = {
        'username': username,
        'email': email,
        'role': role
    }

    # Save user data to JSON file
    file_path = './data/data.json'
    if not os.path.exists('data'):
        os.makedirs('data')
    with open(file_path, 'a') as file:
        json.dump(user_data, file)
        file.write('\n')  # Write each user on a new line

    # Flash a success message
    flash('User created successfully', 'success')

    # Redirect to login page
    return redirect(url_for('login'))

# @app.route('/login')
# def login():
#     return render_template('login.html')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']

        # Read user data from JSON file
        file_path = './data/data.json'
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                for line in file:
                    user = json.loads(line)
                    if user['username'] == username:
                        # User found, return details and permissions
                        return jsonify(user)
        
        flash('User not found', 'error')
        return redirect(url_for('login'))

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
