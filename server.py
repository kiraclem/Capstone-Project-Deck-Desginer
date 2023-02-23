from flask import Flask, render_template, redirect, request, session, flash
from model import connect_to_db, db
from lists import card_list
import crud


from jinja2 import StrictUndefined 

app = Flask(__name__)
app.secret_key = "Hello"
app.jinja_env.undefined = StrictUndefined

#HOME, LOGIN, AND LOGOUT:
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

#PUBLIC DECKS:
@app.route("/view_decks")
def all_decks():
    public_decks = crud.get_public_decks()
    return render_template("view_decks.html", public_decks=public_decks)


#CATEGORIES:
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

    #CREATE
@app.route("/categories/create")
def create_category():
    return render_template("create_category.html")


@app.route("/categories", methods=["POST"])
def create_cat():
    user_session = session.get("user_id")

    if user_session:
        user_id = session["user_id"]
        category_name = request.form.get("category_name")
        category = crud.create_category(category_name, user_id)
        with app.app_context():
            db.session.add(category)
            db.session.commit()
            return redirect("/categories")
    
    else:
        flash("please log in to get access to this page.")
        return redirect("/")
    
    #DELETE
@app.route("/categories/delete/<category_id>")
def delete(category_id):
    user_session = session.get("user_id")

    if user_session:
        with app.app_context():
            category = crud.get_category_by_id(category_id)
            db.session.delete(category)
            db.session.commit()
        return redirect("/categories")
    else:
        flash("please log in to get access to this page.")
        return redirect("/")
    

#DECKS
@app.route("/categories/<category_id>")
def decks(category_id):

    user_session = session.get("user_id")

    if user_session:
        decks = crud.get_decks_by_category(category_id)
        return render_template("decks.html", decks=decks, category_id=category_id)
    
    else:
        flash("please log in to get access to this page.")
        return redirect("/")

    #CREATE
@app.route("/categories/create_deck/<category_id>")
def create_deck(category_id):
    
    user_session = session.get("user_id")

    if user_session:
        return render_template("create_deck.html", category_id=category_id)
    
    else:
        flash("please log in to get access to this page.")
        return redirect("/")


@app.route("/categories/<category_id>", methods=["POST"])
def create_decks(category_id):

    user_session = session.get("user_id")

    if user_session:
        deck_name = request.form.get("deck_name")
        private = request.form.get("private")
        private = bool(private)
        with app.app_context():
            deck1 = crud.create_deck(deck_name, private, category_id)
            db.session.add(deck1)
            db.session.commit()
            for name in card_list:
                card_name = name
                card_type = crud.get_card_type(name)
                card_family = crud.get_card_family(name)
            
                db_card = crud.create_card(card_name, card_type, card_family, deck1.deck_id, 1)
                db.session.add(db_card)
                db.session.commit()
        return redirect ("/categories")
    else:
        flash("please log in to get access to this page.")
        return redirect("/")

    #DELETE
@app.route("/categories/delete/<category_id>/<deck_id>")
def delete_deck(category_id, deck_id):
    user_session = session.get("user_id")

    if user_session:
        with app.app_context():
            deck = crud.get_deck_by_id(deck_id)
            db.session.delete(deck)
            db.session.commit()
        return redirect("/categories")
    else:
        flash("please log in to get access to this page.")
        return redirect("/")
    

#CARDS
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
    connect_to_db(app, echo=False)
    app.run(host="0.0.0.0", debug=True)