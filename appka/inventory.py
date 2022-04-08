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
    elif request.method == "POST" and "categories" in request.form and "search" in request.form:
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

    elif request.method == "POST" and "removeBtn" in request.form:
        qty = int(request.form["quantity"])
        iId = int(request.form[""])
        db.execute(
            "UPDATE inventory SET inStock = inStock - ? WHERE itemName = ?;", [qty, iId]
        )
        db.commit()
        items = db.execute(
            "SELECT * FROM inventory"
        ).fetchall()
    elif request.method == "POST" and "addBtn" in request.form:
        qty = int(request.form["quantity"])
        iName = int(request.form["itemName"])
        db.execute(
            "UPDATE inventory SET inStock = inStock + ? WHERE itemName = ?", [qty, iName]
        )
        db.commit()
        items = db.execute(
            "SELECT * FROM inventory"
        ).fetchall()
        
        return render_template("inventory/inventory.html", items = items)
    
    else:
        items = db.execute(
            "SELECT * FROM inventory"
        ).fetchall()
        return render_template("inventory/inventory.html", items = items)