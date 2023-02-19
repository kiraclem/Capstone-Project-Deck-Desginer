import os 
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    def __repr__(self):
        return f'<User user_id = {self.user_id} username = {self.username}>'

class Category(db.Model):

    __tablename__ = "categories"

    category_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    category_name = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))

    user = db.relationship("User", backref="category") #DOUBLE CHECK THAT ITS CARDS!!

    def __repr__(self):
        return f'<Category category_id = {self.category_id} category_name = {self.category_name}>'

class Deck(db.Model):

    __tablename__ = "decks"

    deck_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    deck_name = db.Column(db.String)
    private = db.Column(db.Boolean, default=True)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.category_id"))

    def __repr__(self):
        return f'<Decks deck_id = {self.deck_id} deck_name = {self.deck_name}>'

class Image(db.Model):

    __tablename__ = "images"

    image_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    #LargeBinary, (file selection HTML)
    image_ref = db.Column(db.String)
    

    def __repr__(self):
        return f'<Image image_id = {self.image_id} image_ref = {self.image_ref}>'

class Card(db.Model):
    __tablename__ = "cards"

    card_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    card_name = db.Column(db.String)
    deck_id =  db.Column(db.Integer, db.ForeignKey("decks.deck_id"))
    image_id = db.Column(db.Integer, db.ForeignKey("images.image_id"))

    def __repr__(self):
            return f'<Image card_id = {self.card_id} card_name = {self.card_name}>'


def connect_to_db(flask_app, echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["POSTGRES_URI"]
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    connect_to_db(app, echo=False)