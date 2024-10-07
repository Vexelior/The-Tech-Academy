class User:
    name = "No name provided"
    email = " "
    password = "1234abcd"
    account_number = 0

class Player(User):
    member = False
    free_to_play = 'General'
    world = 55

class Admin(User):
    moderator = False
    user_list = True
    email = " "
    mailing_list = True


