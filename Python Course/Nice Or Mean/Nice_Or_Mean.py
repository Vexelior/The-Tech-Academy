# Python: 3.9.1
#
# Author: Alexander W. Sanderson, Daniel A. Christie
#
# Purpose: The Tech Academy - Python Course, Creating a game together.
#          Demonstrating how to pass variables from function to function
#          while producing a functional game.
#
#          Remember, function_name(variable) means that we pass in the variable.
#          return variable means that we are returning the variable to
#          back to the calling function.




def start(nice=0,mean=0,name=""):
    # Get user's name
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)

    

def describe_game(name):
    """
        Check if this is a new game or not.
        If it is new, get the user's name.
        If it is not a new game, thank the player for
        playing again and continue with the game.
    """
    # Meaning, if we do not already have this user's name,
    # then they are a new player and we need to get their name
    if name != "":
        print("\nThank you for playing again, {}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name? \n>>> ").capitalize()
                if name != "":
                    print("\nWelcome, {}!".format(name))
                    print("\nIn this game, you will be greeted \nby several different people. \nYou can choose to be nice or mean")
                    print("but at the end of the game your fate \nWill be sealed by your actions.")
                    stop = False
    return name



def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input("\nA stranger approaches you for a \nconversation. Will you be nice \nor mean? (N/M) \n>>>: ").lower()
        if pick == "n":
            print("\nThe stranger walks away smiling...")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print("\nThe stranger glares at you \nmenacingly and storms off...")
            mean = (mean + 1)
            stop = False
    score(nice,mean,name) # Pass the 3 variables to the score()

def show_score(nice,mean,name):
    print("\n{}, your current total: \n({}, Nice) and ({}, Mean)".format(name,nice,mean))

    

def score(nice,mean,name):
    # Score function is being passed the values stored within the 3 variables
    if nice > 2: # If condition is valid, call win function passing in the variables so it can use them.
        win(nice,mean,name)
    if mean > 2: # If condition is valid, call win function passing in the variables so it can use them.
        lose(nice,mean,name)
    else:        # Else, call nice_mean function passing in the variables so it can use them.   
        nice_mean(nice,mean,name)

        

def win(nice,mean,name):
    # Substitute the {} wildcards with our variable values.
    print("\nNice job {}, you win! \nEveryone loves you and you've \nmade lots of friends along the way!".format(name))
    # Call again function and pass in our variables.
    again(nice,mean,name)


def lose(nice,mean,name):
    # Substitute the {} wildcards with our variable values.
    print("\nAhhh too bad, game over! \n{}, you live in a dirty beat-up \nvan by the river, wretched and alone!".format(name))
    # Call again function and pass in our variables.
    again(nice,mean,name)
    

def again(nice,mean,name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again? (y/n):\n>>> ").lower()
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        if choice == "n":
            print("\nOh, so sad, sorry to see you go!")
            stop = False
            quit()
        else:
            print("\nEnter( Y ) for 'YES', ( N ) for 'NO':\n>>> ")


def reset(nice,mean,name):
    nice = 0
    mean = 0
    # Notice, I do not reset the name variable as that same user has elected to play again.
    start(nice,mean,name)






if __name__ == "__main__":
    start()
