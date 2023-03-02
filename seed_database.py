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
    username = f"username"
    password = f"123"
    db_user = crud.create_user(username, password)
    model.db.session.add(db_user)
    model.db.session.commit()

        
 






