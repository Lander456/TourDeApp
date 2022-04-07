from flask import *
from appka.db import get_db

bp = Blueprint("cart",__name__)
@bp.route("/kosik", methods = ("GET", "POST"))
def cart():
    db = get_db()
    items = db.execute(
        "SELECT * FROM cart"
    ).fetchall()
    return render_template("inventory/cart.html", items = items)