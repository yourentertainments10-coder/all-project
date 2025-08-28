from flask import Flask, render_template, request, redirect, session, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.secret_key = "secret123"  # Change in production

# Database Config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///college.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# ------------------ MODELS ------------------
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(10), nullable=False)  # student/faculty

class Assignment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(300))
    faculty_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    date = db.Column(db.String(20))
    status = db.Column(db.String(10))  # Present/Absent
    faculty_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    # Admin: List all students
    @app.route("/admin/students")
    def admin_students():
        students = User.query.filter_by(role="student").all()
        return render_template("admin_students.html", students=students)

    # Admin: List all faculty
    @app.route("/admin/faculty")
    def admin_faculty():
        faculty = User.query.filter_by(role="faculty").all()
        return render_template("admin_faculty.html", faculty=faculty)

    # Admin: List all assignments
    @app.route("/admin/assignments")
    def admin_assignments():
        assignments = Assignment.query.all()
        return render_template("admin_assignments.html", assignments=assignments)

    # Admin: List all attendance records
    @app.route("/admin/attendance")
    def admin_attendance():
        attendance = Attendance.query.all()
        return render_template("admin_attendance.html", attendance=attendance)

        # Admin Dashboard Route
    @app.route("/admin")
    def admin_dashboard():
        student_count = User.query.filter_by(role="student").count()
        faculty_count = User.query.filter_by(role="faculty").count()
        assignment_count = Assignment.query.count()
        attendance_count = Attendance.query.count()
        return render_template("admin_dashboard.html",
            student_count=student_count,
            faculty_count=faculty_count,
            assignment_count=assignment_count,
            attendance_count=attendance_count)
with app.app_context():
    db.create_all()

# ------------------ ROUTES ------------------

@app.route("/")
def home():
    return redirect(url_for("login"))

# Signup
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = generate_password_hash(request.form["password"])
        role = request.form["role"].lower()

        if User.query.filter_by(username=username).first():
            return "User already exists!"

        new_user = User(username=username, password=password, role=role)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("login"))
    return render_template("signup.html")

# Login
@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session["user_id"] = user.id
            session["role"] = user.role
            if user.role == "faculty":
                return redirect(url_for("faculty_dashboard"))
            else:
                return redirect(url_for("student_dashboard"))
        error = "Invalid Credentials!"
    return render_template("login.html", error=error)

# Faculty Dashboard
@app.route("/faculty")
def faculty_dashboard():
    if "role" in session and session["role"] == "faculty":
        user = db.session.get(User, session["user_id"])
        return render_template("faculty_dashboard.html", user=user)
    return redirect(url_for("login"))

@app.route("/faculty/add-assignment", methods=["GET", "POST"])
def add_assignment():
    if "role" in session and session["role"] == "faculty":
        if request.method == "POST":
            title = request.form["title"]
            desc = request.form["description"]
            faculty_id = session["user_id"]
            new_task = Assignment(title=title, description=desc, faculty_id=faculty_id)
            db.session.add(new_task)
            db.session.commit()
            return redirect(url_for("faculty_dashboard"))
        return render_template("faculty_add_assignment.html")
    return redirect(url_for("login"))

@app.route("/faculty/mark-attendance", methods=["GET", "POST"])
def mark_attendance():
    if "role" in session and session["role"] == "faculty":
        students = User.query.filter_by(role="student").all()
        if request.method == "POST":
            date = request.form["date"]
            for student in students:
                status = request.form.get(f"status_{student.id}")
                attendance = Attendance(student_id=student.id, date=date, status=status, faculty_id=session["user_id"])
                db.session.add(attendance)
            db.session.commit()
            return redirect(url_for("faculty_dashboard"))
        return render_template("faculty_mark_attendance.html", students=students)
    return redirect(url_for("login"))

# Student Dashboard
@app.route("/student")
def student_dashboard():
    if "role" in session and session["role"] == "student":
        return render_template("student_dashboard.html")
    return redirect(url_for("login"))

@app.route("/student/assignments")
def student_assignments():
    if "role" in session and session["role"] == "student":
        assignments = Assignment.query.all()
        return render_template("student_assignments.html", assignments=assignments)
    return redirect(url_for("login"))

@app.route("/student/attendance")
def student_attendance():
    if "role" in session and session["role"] == "student":
        attendance = Attendance.query.filter_by(student_id=session["user_id"]).all()
        return render_template("student_attendance.html", attendance=attendance)
    return redirect(url_for("login"))

# Logout
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

# ------------------ RUN ------------------
if __name__ == "__main__":
    app.run(debug=True)
