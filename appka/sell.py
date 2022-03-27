from flask import *
from db import get_db

bp = Blueprint("Pokladna", __name__, url_prefix="/sell")
@bp.route("/sell", methods = ("GET", "POST"))
def sell():
    pass