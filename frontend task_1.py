from flask import Flask, render_template, request, redirect, url_for, session # type: ignore

app = Flask(__name__)
app.secret_key = "supersecretkey"  

users = {
    "john": {"password": "1234", "role": "user"},
    "admin": {"password": "admin123", "role": "admin"}
}

@app.route("/")
def home():
    if "user" in session:
        return redirect(url_for("dashboard"))
    return "Welcome! <a href='/login'>Login</a> | <a href='/signup'>Sign Up</a>"

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        role = request.form["role"]

        if username in users:
            return "Username already exists! Try another one."

        users[username] = {"password": password, "role": role}
        return "Signup successful! <a href='/login'>Login here</a>"

    return '''
    <h2>Sign Up</h2>
    <form method="post">
        Username: <input type="text" name="username" required><br>
        Password: <input type="password" name="password" required><br>
        Role: <select name="role">
            <option value="user">User</option>
            <option value="admin">Admin</option>
        </select><br>
        <input type="submit" value="Sign Up">
    </form>
    '''

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username in users and users[username]["password"] == password:
            session["user"] = username
            session["role"] = users[username]["role"]
            return redirect(url_for("dashboard"))

        return "Invalid username or password! Try again."

    return '''
    <h2>Login</h2>
    <form method="post">
        Username: <input type="text" name="username" required><br>
        Password: <input type="password" name="password" required><br>
        <input type="submit" value="Login">
    </form>
    '''

@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))

    if session["role"] == "admin":
        return '''
        <h1>Welcome, Admin! You have full access.</h1>
        <ul>
            <li><a href='/view_users'>View All Users</a></li>
            <li><a href='/add_user'>Add New User</a></li>
            <li><a href='/logout'>Logout</a></li>
        </ul>
        '''
    else:
        return '''
        <h1>Welcome, User! You have limited access.</h1>
        <a href='/logout'>Logout</a>
        '''

@app.route("/view_users")
def view_users():
    if "user" not in session or session["role"] != "admin":
        return "Access Denied! <a href='/dashboard'>Go Back</a>"

    user_list = "<h2>All Users:</h2><ul>"
    for username, info in users.items():
        user_list += f"<li>{username} - Role: {info['role']} <a href='/delete_user/{username}'>[Delete]</a></li>"
    user_list += "</ul><a href='/dashboard'>Back to Dashboard</a>"
    
    return user_list

@app.route("/delete_user/<username>")
def delete_user(username):
    if "user" not in session or session["role"] != "admin":
        return "Access Denied! <a href='/dashboard'>Go Back</a>"

    if username in users and username != "admin": 
        del users[username]
        return f"User {username} deleted! <a href='/view_users'>Go Back</a>"

    return "User not found or cannot be deleted. <a href='/view_users'>Go Back</a>"

@app.route("/add_user", methods=["GET", "POST"])
def add_user():
    if "user" not in session or session["role"] != "admin":
        return "Access Denied! <a href='/dashboard'>Go Back</a>"

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        role = request.form["role"]

        if username in users:
            return "Username already exists! <a href='/add_user'>Try Again</a>"

        users[username] = {"password": password, "role": role}
        return f"User {username} added! <a href='/view_users'>View Users</a>"

    return '''
    <h2>Add New User</h2>
    <form method="post">
        Username: <input type="text" name="username" required><br>
        Password: <input type="password" name="password" required><br>
        Role: <select name="role">
            <option value="user">User</option>
            <option value="admin">Admin</option>
        </select><br>
        <input type="submit" value="Add User">
    </form>
    <a href='/dashboard'>Back to Dashboard</a>
    '''

@app.route("/logout")
def logout():
    session.pop("user", None)
    session.pop("role", None)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
