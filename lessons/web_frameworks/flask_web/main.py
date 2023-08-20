import os
from flask import Flask
from src.router import router as auth_router  # payment_router ...
from flask_sqlalchemy import SQLAlchemy

app: Flask = Flask(
    __name__,
    template_folder="templates",
    static_url_path="/static",
    static_folder="static",
)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(os.path.abspath(os.path.dirname(__file__)), "database.sqlite3")  # flask_web/...
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db: SQLAlchemy = SQLAlchemy(app)
app.register_blueprint(auth_router, url_prefix="")
# app.register_blueprint(payment_router, url_prefix="/api/payment")


@app.before_request
def before_first_request():
    # This function will be executed before the first request
    # You can put startup tasks or initialization code here
    print("Flask application has started!")
    # db.drop_all()
    db.create_all()
