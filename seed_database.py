import os

import model 
import server 
import crud
from lists import card_list


os.system("dropdb cards")
os.system("createdb cards")

app = server.app
model.connect_to_db(server.app)
with app.app_context():

    model.db.create_all()

    #users
    for u in range(1):
        username = f"username{u}"
        password = f"{u}23"
        db_user = crud.create_user(username, password)
        model.db.session.add(db_user)
        model.db.session.commit()

    #categories
        for c in range(1):
            category_name = f"category{c}"
            user_id = int(f"{u + 1}")

            db_category = crud.create_category(category_name, user_id)
            model.db.session.add(db_category)
            model.db.session.commit()

    #decks
            # for d in range(1):
            #     deck_name= f"deck{d}"
            #     private= True
            #     category_id = int(f"{c + 1}")

            #     db_deck = crud.create_deck(deck_name, private, category_id)
            #     model.db.session.add(db_deck)
            #     model.db.session.commit()
    #images
                # image_ref = "../../image_uploads/card.png"
                # db_image = crud.create_image(image_ref)
                # model.db.session.add(db_image)
                # model.db.session.commit()

    #cards
                # for name in card_list:
                #     card_name = name
                #     card_type = crud.get_card_type(name)
                #     card_family = crud.get_card_family(name)
                #     deck_id = int(f"{c + 1}")
                #     image_id = int(f"{c + 1}")

                #     db_card = crud.create_card(card_name, card_type, card_family, deck_id, image_id)
                #     model.db.session.add(db_card)
                #     model.db.session.commit()
        
 






