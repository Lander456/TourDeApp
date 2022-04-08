from flask import *
from appka.db import get_db

bp = Blueprint("Pokladna", __name__)
@bp.route("/Pokladna", methods = ("GET", "POST"))
def sell():
    db = get_db()
    if request.method == "GET":
        items = db.execute(
            "SELECT * FROM inventory"
        ).fetchall()
        return render_template("inventory/sell.html", items = items)
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
        return render_template("inventory/sell.html", items = items)
        
    elif request.method == "POST" and "addToCart" in request.form and "quantity" in request.form:
        qty = int(request.form["quantity"])
        iName = int(request.form["itemName"])
        db.execute(
            "INSERT INTO cart FROM inventory WHERE itemName = ?;UPDATE cart SET inCart = ? WHERE itemName = ?;UPDATE inventory SET inStock = inStock - ? WHERE itemName = ?"[iName,qty,iName,qty,iName]
        )
    else:
        items = db.execute(
            "SELECT * FROM inventory"
        ).fetchall()
        return render_template("inventory/sell.html", items = items)