#Import Flask and JSON for backend
from flask import Flask,render_template, request, redirect, session,jsonify,flash 
import json 
import random

#Creating a Flask app
app = Flask(__name__)
#Create a secret key for sessions module
app.secret_key = "df86c319adcd8242593ce55f3d5cb8b2"

#Loading data from external json file
def load_users():
    try: 
        with open('users.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"users": [], "next_id": 1}
    
def load_cases():
    try: 
        with open('cases.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"cases": []}
    
    

#Updating external json file with new data
def save_users(users_data):
    with open('users.json','w') as file:
        json.dump(users_data, file, indent=4)

#Create unique id for every user for structuring in table in future
def generate_user_id(users_data):
    user_id = users_data["next_id"]
    users_data["next_id"] +=1
    return user_id

#Check if username already exists in our DB
def is_username_unique(username,users_data):
    return not any(user['username'] ==  username for user in users_data['users'])

#Home page routing
@app.route("/")
def hello_world():
    #Check for existing sessions and if it exists redirect to dashboard if not show home page
    if 'logged_in' in session and session['logged_in']:
        return redirect("/dashboard")
    else:
        return render_template('home.html')

@app.route("/authenticate", methods=["POST", "GET"])
def authenticate():
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
            # Clear error message when page is loaded initially
            return render_template('authenticate.html', error=None)

#Dashboard page routing
@app.route("/dashboard")
def dashboard():
    if 'logged_in' in session and session['logged_in']:
        return redirect("/dashboard/cases")
    else:
        return redirect("/authenticate")

@app.route("/dashboard/cases")
def dashboard_cases():
    if 'logged_in' in session and session['logged_in']:
        data = load_cases()
        random_case = random.choice(data["cases"])
        return render_template("cases.html", description = random_case)
    else:
        return redirect("/authenticate")
    
@app.route("/dashboard/clues")
def dashboard_clues():
    if 'logged_in' in session and session['logged_in']:
        return render_template("clues.html")
    else:
        return redirect("/authenticate")
    
    
@app.route("/dashboard/suspect")
def dashboard_suspects():
    if 'logged_in' in session and session['logged_in']:
        return render_template("suspect.html")
    else:
        return redirect("/authenticate")
    

@app.route("/dashboard/timeline")
def dashboard_timeline():
    if 'logged_in' in session and session['logged_in']:
        return render_template("timeline.html")
    else:
        return redirect("/authenticate")
    
    
#Logout routing linked with a button
@app.route("/logout",methods = ["POST"])
def logout():
    session.pop('logged_in',None)
    return redirect("/authenticate")    
if __name__ == "__main__":
    app.run(debug=True)