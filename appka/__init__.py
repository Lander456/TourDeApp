from operator import index
import os
from flask import *

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=os.path.join(app.instance_path, "appka.sqlite"),
    )

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    db.init_app(app)

    from . import inventory
    app.register_blueprint(inventory.bp)

    from . import add_item
    app.register_blueprint(add_item.bp)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import sell
    app.register_blueprint(sell.bp)

    from . import cart
    app.register_blueprint(cart.bp)

    return app