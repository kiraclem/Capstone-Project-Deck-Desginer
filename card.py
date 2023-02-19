# 58 cards
card_list = [
    '1 of diamonds',  '1 of clubs',    '1 of hearts',
    '1 of spades',    '2 of diamonds', '2 of clubs',
    '2 of hearts',    '2 of spades',   '3 of diamonds',
    '3 of clubs',     '3 of hearts',   '3 of spades',
    '4 of diamonds',  '4 of clubs',    '4 of hearts',
    '4 of spades',    '5 of diamonds', '5 of clubs',
    '5 of hearts',    '5 of spades',   '6 of diamonds',
    '6 of clubs',     '6 of hearts',   '6 of spades',
    '7 of diamonds',  '7 of clubs',    '7 of hearts',
    '7 of spades',    '8 of diamonds', '8 of clubs',
    '8 of hearts',    '8 of spades',   '9 of diamonds',
    '9 of clubs',     '9 of hearts',   '9 of spades',
    '10 of diamonds', '10 of clubs',   '10 of hearts',
    '10 of spades',   'A of diamonds', 'A of clubs',
    'A of hearts',    'A of spades',   'K of diamonds',
    'K of clubs',     'K of hearts',   'K of spades',
    'Q of diamonds',  'Q of clubs',    'Q of hearts',
    'Q of spades',    'J of diamonds', 'J of clubs',
    'J of hearts',    'J of spades',   'joker',
    'joker'
  ]

# TYPE = 1, 2, A, Q, J ect. or joker
def get_card_type(card): 
    card = card.split(" ")
    card_type = card[0]
    return card_type

# FAMILY = spades, diamonds, hearts ect. 
def get_card_family(card): 
    card = card.split(" ")
    card_type = card[2]
    return card_type

# for c in card_list:
#     print(c)

# print(get_card_type("joker"))
# print(get_card_type("A of hearts"))
# print(get_card_type("10 of diamonds"))

# print(get_card_family("1 of spades"))
# print(get_card_family("A of hearts"))
# print(get_card_family("10 of diamonds"))
