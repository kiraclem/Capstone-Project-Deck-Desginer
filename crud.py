from model import User, Category, Deck, Image, Card


# CREATE TABLES
def create_user(username, password):
    user1 = User(
        username=username,
        password=password
        )
    return user1


def create_category(category_name, user_id):
    category = Category(
        category_name=category_name,
        user_id=user_id,
        )
    return category


def create_deck(deck_name, private, category_id):
    deck = Deck(
        deck_name=deck_name,
        private=private,
        category_id=category_id
        )
    return deck


def create_image(image_ref):
    image = Image(
        image_ref=image_ref
        )
    return image


def create_card(card_name, deck_id, image_id):
    card = Card(
        card_name=card_name,
        deck_id=deck_id,
        image_id=image_id
        )
    return card


#GET BY ID
def get_user_by_id(user_id):
    return User.query.get(user_id)

def get_category_by_id(category_id):
    return User.query.get(category_id)

def get_deck_by_id(deck_id):
    return User.query.get(deck_id)

def get_image_by_id(image_id):
    return User.query.get(image_id)

def get_card_by_id(card_id):
    return User.query.get(card_id)