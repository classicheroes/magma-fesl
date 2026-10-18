from flask import Flask
from datetime import datetime

from config import (
    DATABASE_URL,
    HOST,
    PORT,
    SERVER_NAME,
    SERVER_POWERED
)

from database import db


# =====================================
# CREATE APP
# =====================================

app = Flask(__name__)


# =====================================
# DATABASE
# =====================================

app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.config["SQLALCHEMY_ECHO"] = False


db.init_app(app)



# =====================================
# IMPORT MODELS
# =====================================

from models import models



# =====================================
# IMPORT ROUTES
# =====================================

from routes.nucleus import nucleus_bp
from routes.store import store_bp
from routes.relationships import relationships_bp
from routes.telemetry import telemetry_bp



# =====================================
# REGISTER BLUEPRINTS
# =====================================

app.register_blueprint(
    nucleus_bp
)

app.register_blueprint(
    store_bp
)

app.register_blueprint(
    relationships_bp
)

app.register_blueprint(
    telemetry_bp
)



# =====================================
# HOME
# =====================================

@app.route("/")
def index():

    return """
    <!DOCTYPE html>

    <html>

    <head>
        <title>Classic Heroes Magma</title>
    </head>

    <body>

    <center>

        <h1>
        Classic Heroes Magma
        </h1>

        <h3>
        Powered by Classic Heroes
        </h3>

        <p>
        Server Online
        </p>

    </center>

    </body>

    </html>
    """



# =====================================
# STATUS
# =====================================

@app.route("/status")
def status():

    return {

        "server":
        SERVER_NAME,

        "powered":
        SERVER_POWERED,

        "status":
        "online"

    }



# =====================================
# BANNER
# =====================================

def banner():

    print("")
    print("================================")
    print("      Classic Heroes Magma")
    print("      Powered by Classic Heroes")
    print("================================")
    print("")

    print(
        "Started:",
        datetime.now()
    )

    print(
        f"Running on port {PORT}"
    )

    print("")



# =====================================
# START SERVER
# =====================================

if __name__ == "__main__":


    with app.app_context():

        db.create_all()



    banner()


    app.run(

        host=HOST,

        port=PORT,

        debug=True,

        ssl_context="adhoc"

    )