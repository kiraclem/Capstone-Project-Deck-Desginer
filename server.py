from flask import Flask, render_template, redirect, request, session, flash
from model import connect_to_db, db
import crud


from jinja2 import StrictUndefined 

app = Flask(__name__)
app.secret_key = "Hello"
app.jinja_env.undefined = StrictUndefined

@app.route("/")
def home():
    return render_template("homepage.html")

@app.route("/login")
def log_in():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    user = crud.get_user_by_username(username)

    if user and user.password == password:
        session["user_id"] = user.user_id
        flash("successfully logged in")
        return redirect("/")
    else:
        flash("login credentials don't match the system")
        return redirect("/login")

@app.route("/logout")
def logout():
    del session["user_id"]
    flash("logged out successfully")
    return redirect("/")

@app.route("/view_decks")
def all_decks():
    return render_template("view_decks.html")

@app.route("/categories")
def users_categories():
    user_session = session.get("user_id")

    if user_session:
        user_id = session["user_id"]
        categories = crud.get_categories_by_user(user_id)
        return render_template("categories.html", categories=categories)
        
    else:
        flash("please log in to get access to this page.")
        return redirect("/")

@app.route("/categories", methods=["POST"])
def create_category():
    return redirect("/categories")

@app.route("/categories/<category_id>")
def decks(category_id):

    user_session = session.get("user_id")

    if user_session:
        decks = crud.get_decks_by_category(category_id)
        return render_template("decks.html", decks=decks, category_id=category_id)
    
    else:
        flash("please log in to get access to this page.")
        return redirect("/")

@app.route("/categories/<category_id>/decks", methods=["POST"])
def create_deck():
    return redirect("/categories/decks")

@app.route("/categories/<category_id>/<deck_id>")
def view_cards(category_id, deck_id):
    user_session = session.get("user_id")

    if user_session:
        cards = crud.get_cards_by_deck(deck_id)
        return render_template("view_user_cards.html", cards=cards)
    else:
        flash("please log in to get access to this page.")
        return redirect("/")


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)