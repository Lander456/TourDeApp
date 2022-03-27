from flask import *
from appka.db import get_db

bp = Blueprint ("inventory", __name__, url_prefix="/inventory")
@bp.route("/inventory", methods=("GET","POST"))
def inventory():
    if request.method == "GET":
        db = get_db()
        error = None
        items = db.execute(
            "SELECT * FROM inventory"
        ).fetchall()
        return render_template("inventory/inventory.html", items = items)
    else:
        return render_template("inventory/inventory.html", items = items)