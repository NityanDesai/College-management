from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")

# @app.route("/calendar")
# def calendar():
#     return render_template("calendar.html")

@app.route("/admin_dash")
def admin_dash():
    return render_template("index.html")

@app.route("/faculty_dash")
def faculty_dash():
    return render_template("dashboard.html")

@app.route("/edit_faculty")
def edit_faculty():
    return render_template("edit_faculty.html")

@app.route("/edit_subject")
def edit_subject():
    return render_template("edit_subject.html")

@app.route("/edit_stream")
def edit_stream():
    return render_template("edit_stream.html")

@app.route("/faculties")
def faculties():
    return render_template("faculties.html")

@app.route("/add_f")
def add_f():
    return render_template("setting.html")

@app.route("/add_s")
def add_s():
    return render_template("profile.html")

@app.route("/subjects")
def subjects():
    return render_template("subjects.html")

@app.route("/stream")
def stream():
    return render_template("stream.html")

app.run(debug=True)