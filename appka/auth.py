from flask import *
from werkzeug.security import check_password_hash, generate_password_hash
from appka.db import get_db

bp = Blueprint("auth", __name__)

@bp.route("/register", methods=("GET","POST"))
def register():
    if request.method == "POST":
        username = request.form["name"]
        password = request.form["pwd"]
        role = request.form["role"]
        email = request.form["email"]
        db = get_db()
        error = None

        if not username:
            error = "username invalid"
        elif not password:
            error = "password invalid"
        elif not role:
            error = "role required"
        elif not email:
            error = "email required"
        
        if error is None:
            try:
                db.execute(
                    "INSERT INTO users (username, passwords, email, roles) VALUES (?, ?, ?, ?)",
                    (username, generate_password_hash(password), email, role),
                )
                db.commit()
            except db.IntegrityError:
                error = f"User {username} is already registered."
            else:
                return redirect(url_for("auth.login"))

        flash(error)

    return render_template("auth/register.html")

@bp.route("/", methods=("GET","POST"))
def login():
    if request.method == "POST":
        username = request.form["userName"]
        password = request.form["password"]
        db = get_db()
        error = None
        user = db.execute(
            "SELECT passwords FROM users WHERE userName = ?", (username, )
        ).fetchone()

        if user is None:
            error = "incorrect username"
        elif not check_password_hash(user["passwords"], password):
            error = "incorrect password"
        
        if error is None:
            session.clear()
            return redirect(url_for("inventory"))

        flash(error)

    return render_template("auth/login.html")