from flask import Flask, render_template, redirect
from model import connect_to_db, db

from jinja2 import StrictUndefined 

app = Flask(__name__)
app.secret_key = "Hello"
app.jinja_env.undefined = StrictUndefined

@app.route("/")
def home():
    return render_template("homepage.html")

@app.route("/view_decks")
def all_decks():
    return render_template("view_decks.html")

@app.route("/categories")
def users_categories():
    return render_template("categories.html")

@app.route("/categories", methods=["POST"])
def create_category():
    return redirect("/categories")

@app.route("/categories/decks")
def users_decks():
    return render_template("decks.html")

@app.route("/categories/decks", methods=["POST"])
def create_deck():
    return redirect("/categories/decks")

@app.route("/categories/decks/<deck_id>")
def view_cards():
    return render_template("view_user_cards.html")


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)