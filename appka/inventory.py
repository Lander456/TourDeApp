from flask import *
from db import get_db

bp = Blueprint ("inventory", __name__, url_prefix="/inventory")
@bp.route("/inventory", methods=("GET","POST"))
def inventory():
    if request.method == "POST":
        db = get_db()
        error = None
        items = db.execute(
            "SELECT i.id, item, category, colour, IN_STORE, desc"
            " FROM inventory"
        ).fetchall()
        return render_template("inventory/inventory.html", items = items)