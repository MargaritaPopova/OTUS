from flask import Flask

from .views.portfolio import portfolio_app

app = Flask(__name__)
app.register_blueprint(portfolio_app, url_prefix="/portfolio")


@app.route("/")
def index():
    return "<h1><em>Base page</em></h1>"
