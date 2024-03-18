# Importing required modules
from flask import Flask, render_template, request, redirect, session, jsonify
import json
import random

# Creating a Flask app
app = Flask(__name__)

# Create a secret key for sessions
app.secret_key = "df86c319adcd8242593ce55f3d5cb8b2"

# Function to load user data from external JSON file
def load_users():
    try: 
        with open('users.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"users": [], "next_id": 1}

# Function to load case data from external JSON file
def load_cases():
    try: 
        with open('cases.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"cases": []}

# Function to save user data to external JSON file
def save_users(users_data):
    with open('users.json', 'w') as file:
        json.dump(users_data, file, indent=4)

# Function to generate a unique user ID
def generate_user_id(users_data):
    user_id = users_data["next_id"]
    users_data["next_id"] += 1
    return user_id

# Function to check if username is unique
def is_username_unique(username, users_data):
    return not any(user['username'] ==  username for user in users_data['users'])

# Home page routing
@app.route("/")
def hello_world():
    # Check if user is logged in and redirect to dashboard if so
    if 'logged_in' in session and session['logged_in']:
        return redirect("/dashboard")
    else:
        return render_template('home.html')

# Authentication routing
@app.route("/authenticate", methods=["POST", "GET"])
def authenticate():
    # If user is already logged in, redirect to dashboard
    if 'logged_in' in session and session['logged_in']:
        return redirect('/dashboard')
    else:
        if request.method == 'POST':
            if 'login_username' in request.form and 'login_password' in request.form:
                username = request.form['login_username']
                password = request.form['login_password']
                if username and password:
                    users_data = load_users()
                    user = next((user for user in users_data['users'] if user['username'] == username), None)
                    if user and user['password'] == password:
                        session['logged_in'] = True
                        return redirect("/dashboard")
                    else:
                        error = "Incorrect credentials"
                else:
                    error = "Missing username or password"
            elif 'signup_username' in request.form and 'signup_password' in request.form:
                name = request.form['signup_username']
                password = request.form['signup_password']
                if name and password:
                    users_data = load_users()
                    if is_username_unique(name, users_data):
                        user_id = generate_user_id(users_data)
                        new_user = {"id": user_id, "username": name, "password": password}
                        users_data['users'].append(new_user)
                        save_users(users_data)
                        return redirect("/login")
                    else:
                        error = "Username already exists"
                else:
                    error = "Missing username or password"
            return render_template('authenticate.html', error=error)
        else:
            return render_template('authenticate.html', error=None)

# Dashboard routing
@app.route("/dashboard")
def dashboard():
    if 'logged_in' in session and session['logged_in']:
        return redirect("/dashboard/cases")
    else:
        return redirect("/authenticate")

# Dashboard cases routing
@app.route("/dashboard/cases")
def dashboard_cases():
    if 'logged_in' in session and session['logged_in']:
        data = load_cases()
        random_case = random.choice(data["cases"])
        return render_template("cases.html", description=random_case)
    else:
        return redirect("/authenticate")

# Dashboard clues routing
@app.route("/dashboard/clues")
def dashboard_clues():
    if 'logged_in' in session and session['logged_in']:
        return render_template("clues.html")
    else:
        return redirect("/authenticate")

# Dashboard suspects routing
@app.route("/dashboard/suspect")
def dashboard_suspects():
    if 'logged_in' in session and session['logged_in']:
        return render_template("suspect.html")
    else:
        return redirect("/authenticate")

# Dashboard timeline routing
@app.route("/dashboard/timeline")
def dashboard_timeline():
    if 'logged_in' in session and session['logged_in']:
        return render_template("timeline.html")
    else:
        return redirect("/authenticate")

# Logout routing
@app.route("/logout", methods=["POST"])
def logout():
    session.pop('logged_in', None)
    return redirect("/authenticate")

# Route to add a new clue
@app.route('/add_clue', methods=['POST'])
def add_clue():
    # Get the data from the request
    new_clue = request.json

    # Load existing clues from the JSON file
    with open('static/clues.json', 'r') as file:
        data = json.load(file)

    # Append the new clue to the list of clues
    data['clues'].append(new_clue)

    # Write the updated data back to the JSON file
    with open('static/clues.json', 'w') as file:
        json.dump(data, file, indent=4)

    return jsonify({'message': 'Clue added successfully'}), 200

@app.route('/search')
def search():
    query = request.args.get('query')

    with open('clues.json', 'r') as f:
        clues = json.load(f)

    filtered_clues = [clue for clue in clues['clues'] if query.lower() in clue['clue'].lower()]

    return jsonify(filtered_clues)

if __name__ == "__main__":
    app.run(debug=True)
