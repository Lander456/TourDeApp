from flask import *
from appka.db import get_db

bp = Blueprint ("inventory", __name__, url_prefix="/inventory")
@bp.route("/inventory", methods=("GET","POST"))
def inventory():
    db = get_db()
    if request.method == "GET":
        items = db.execute(
            "SELECT * FROM inventory"
        ).fetchall()
        return render_template("inventory/inventory.html", items = items)
    else:
        category = request.form["categories"]
        search = request.form["search"]
        if search == "" and category == "":
            items = db.execute(
                "SELECT * FROM inventory"
            ).fetchall()
        elif category == "" and search != "":
            items = db.execute(
                "SELECT * FROM inventory WHERE itemName LIKE ?", [search]
            )
        elif category != "" and search == "":
            items = db.execute(
                "SELECT * FROM inventory WHERE category = ?", [category]
            )
        elif category != "" and search != "":
            items = db.execute(
                "SELECT * FROM inventory WHERE category = ? AND itemName LIKE ?", [category,search]
            )
        
        return render_template("inventory/inventory.html", items = items)