from flask import *
from appka.db import get_db

bp = Blueprint ("add-item", __name__, url_prefix="/inventory")
@bp.route("/add-item", methods = ("GET","POST"))
def addItem():
    if request.method == "POST":        
        db = get_db()
        error = None
        name = request.form["name"]
        category = request.form["categories"]
        colour = request.form["color"]
        inStock = int(request.form["stock"])
        decription = request.form["description"]
        price = int(request.form["price"])
        db.execute(
            "INSERT INTO inventory (itemName, category, colour, inStock, price, descript)"
            "VALUES (?, ?, ?, ?, ?, ?)",
            (name, category, colour, inStock, price, decription)
        )
        db.commit()
        return redirect("inventory")
    else:
        return render_template("inventory/add-item.html")