from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home Page
@app.route("/")
def home():
    return render_template("index.html")

# Login Page
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "1234":
            return redirect(url_for("dashboard"))
        else:
            return "Invalid Credentials ❌"

    return render_template("login.html")

# Dashboard Page
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

# Level 1 Page
@app.route("/level1")
def level1():
    return render_template("level1.html")

# Run App
if __name__ == "__main__":
    app.run(debug=True)