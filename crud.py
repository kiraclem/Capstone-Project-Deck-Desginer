from model import User, Category, Deck, Image, Card
from lists import card_list


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

def create_card(card_name, card_type, card_family, deck_id, image_id):
    card = Card(
        card_name=card_name,
        card_type=card_type,
        card_family=card_family,
        deck_id=deck_id,
        image_id=image_id
        )
    return card


# GET ALL PUBLIC DECKS
def get_public_decks():
    public_decks = Deck.query.filter(Deck.private == False).all()
    return public_decks
    
def get_all_decks():
    decks = Deck.query.all()
    return decks

#GET BY ID
def get_user_by_id(user_id):
    return User.query.get(user_id)

def get_category_by_id(category_id):
    return Category.query.get(category_id)

def get_deck_by_id(deck_id):
    return Deck.query.get(deck_id)

def get_image_by_id(image_id):
    return Image.query.get(image_id)

def get_card_by_id(card_id):
    return Card.query.get(card_id)


# GET BY
def get_user_by_username(username):
    username = User.query.filter(User.username == username).first()
    return username

def get_categories_by_user(user):
    user = User.query.get(user)
    return user.category

def get_decks_by_category(category):
    category = Category.query.get(category)
    return category.deck

def get_cards_by_deck(deck):
    deck = Deck.query.get(deck)
    return deck.card



# CARD FUNCTIONS
    # TYPE = 1, 2, A, Q, J ect. or joker
def get_card_type(card): 
    card = card.split(" ")
    card_type = card[0]
    return card_type

# CREATE ALL CARDS

def create_deck_of_cards(deck_id, image_id):
    for name in card_list:
        card_name = name
        card_type = get_card_type(name)
        card_family = get_card_family(name)

        cards = create_card(card_name, card_type, card_family, deck_id, image_id)
        return cards

    # FAMILY = spades, diamonds, hearts ect. 
def get_card_family(card): 
    card = card.split(" ")
    if len(card) > 1:
        card_family = card[2]
        return card_family
    else:
        card_family = "joker"
        return card_family
