from flask import *
from appka.db import get_db

bp = Blueprint ("inventory", __name__, url_prefix="/inventory")
@bp.route("/inventory", methods=("GET","POST"))
def inventory():
    if request.method == "GET":
        db = get_db()
        error = None
        items = db.execute(
            "SELECT itemId, itemName, category, colour, IN_STORE, descript"
            " FROM inventory"
        ).fetchall()
        return render_template("inventory/inventory.html", items = items)
    else:
        return render_template("inventory/inventory.html", items = items)

@bp.route("/add-item", methods = ("GET","POST"))
def addItem():
    if request.method == "POST":
        return render_template("inventory/add-item.html")
    else:
        return render_template("inventory/add-item.html")