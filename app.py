from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "codequest_secret"

# HOME
@app.route("/")
def home():
    return render_template("index.html")

# LOGIN
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "1234":
            session["score"] = 0
            return redirect(url_for("dashboard"))
        else:
            return "Invalid Credentials ❌"

    return render_template("login.html")

# DASHBOARD
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", score=session.get("score", 0))

# LEVEL 1
@app.route("/level1", methods=["GET", "POST"])
def level1():
    result = None

    if request.method == "POST":
        answer = request.form.get("answer")

        if answer == "def":
            session["score"] = session.get("score", 0) + 1
            result = "level1_correct"
        else:
            result = "wrong"

    return render_template("level1.html", result=result, score=session.get("score", 0))

# LEVEL 2
@app.route("/level2", methods=["GET", "POST"])
def level2():
    result = None

    if request.method == "POST":
        answer = request.form.get("answer")

        if answer == "#":
            session["score"] = session.get("score", 0) + 1
            result = "level2_correct"
        else:
            result = "wrong"

    return render_template("level2.html", result=result, score=session.get("score", 0))

# LEVEL 3
@app.route("/level3", methods=["GET", "POST"])
def level3():
    result = None

    if request.method == "POST":
        code = request.form.get("code")

        if code and "print" in code:
            session["score"] = session.get("score", 0) + 1
            result = "level3_correct"
        else:
            result = "wrong"

    return render_template("level3.html", result=result, score=session.get("score", 0))

# LEVEL 4
@app.route("/level4", methods=["GET", "POST"])
def level4():
    result = None

    if request.method == "POST":
        code = request.form.get("code")

        if code and "for" in code:
            session["score"] = session.get("score", 0) + 1
            result = "level4_correct"
        else:
            result = "wrong"

    return render_template("level4.html", result=result, score=session.get("score", 0))

# LEVEL 5
@app.route("/level5", methods=["GET", "POST"])
def level5():
    result = None

    if request.method == "POST":
        code = request.form.get("code")

        if code and ":" in code and "print" in code:
            session["score"] = session.get("score", 0) + 1
            result = "completed"
        else:
            result = "wrong"

    return render_template("level5.html", result=result, score=session.get("score", 0))

# LEVEL 6 
@app.route("/level6", methods=["GET", "POST"])
def level6():
    result = None
    if request.method == "POST":
        code = request.form.get("code")
        # Checking if user used the correct H1 tags
        if code and "<h1>" in code and "</h1>" in code:
            session["score"] = session.get("score", 0) + 1
            result = "completed"
        else:
            result = "wrong"
    
    return render_template("level6.html", result=result, score=session.get("score", 0))

# RUN
if __name__ == "__main__":
    app.run(debug=True)