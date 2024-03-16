#Import Flask and JSON for backend
from flask import Flask,render_template, request, redirect, session
import json 

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

#Login page routing
@app.route("/login", methods = ["POST","GET"])
def login_page():
    #Check for existing sessions and if it exists redirect to dashboard if not show login page 
    if 'logged_in' in session and session['logged_in']:
        return redirect('/dashboard')
    
    else:
        #Main algorithm involving reading input fields and comparing with our DB
        if request.method == "POST":
            userDetails = request.form
            username = userDetails.get('username')
            password = request.form.get('password')

            if username and password:
                users_data = load_users()
                user = next((user for user in users_data['users'] if user['username'] == username), None)
                if user and user['password'] == password:
                    session['logged_in'] = True
                    return redirect("/dashboard")
                else:
                    return "Invalid username or password!"
            else:
                return "MISSING"
        return render_template('authenticate.html')
    
#Sign up page routing
@app.route("/signup", methods = ["GET","POST"])
def signup_page():
     #Main algorithm involving reading input fields and putting it inside our DB
    if request.method == "POST":
        userDetails = request.form
        username = userDetails.get('username')
        password = userDetails.get('password')
        if username and password:
            users_data = load_users()
            if is_username_unique(username,users_data):
                user_id = generate_user_id(users_data)
                new_user = {"id": user_id,"username":username,"password":password}
                users_data['users'].append(new_user)
                save_users(users_data)
                return redirect("/login")
            else:
                return "Username already exists"
        else:
            return "MISSING"
    return render_template('signup.html')

#Dashboard page routing
@app.route("/dashboard")
def dashboard():
    if 'logged_in' in session and session['logged_in']:
        return render_template("dashboard.html")
    else:
        return redirect("/login")
#Logout routing linked with a button
@app.route("/logout",methods = ["POST"])
def logout():
    session.pop('logged_in',None)
    return redirect("/login")    
if __name__ == "__main__":
    app.run(debug=True)