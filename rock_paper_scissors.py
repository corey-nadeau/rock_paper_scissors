import random
options = ('rock','paper','scissors')

comp = options[random.randint(0,2)]
player = False
while player == False:
    player = input('\nWelcome, please choose "rock" "paper" or "scissors"\n"Or you can type "quit":')
    if player == comp:
        print("computer chooses: " ,(comp))
        print("\nTie game")
    
    elif player == "rock":
        if comp == "paper":
            print("computer chooses: " ,(comp))
            print("\nYou lose. Paper covers Rock ")
        else:
            print("computer chooses: " ,(comp))
            print("\nYou win! Rock smashes Scissors! ")
    elif player == "paper":
        if comp == "scissors":
            print("computer chooses: " ,(comp))
            print("\nYou lose! Scissors cuts Paper! ")
        else:
            print("computer chooses: " ,(comp))
            print("\nYou win! Paper covers Rock")
    elif player == "scissors":
        if comp == "rock":
            print("computer chooses: " ,(comp))
            print("\nYou lose! Rock smashes Scissors! ")
        else:
            print("computer chooses: " ,(comp))
            print('\nYou win! Scissors cuts Paper! ')
    elif player == "quit":
        break
    else:
        print("\ninvalid entry. try 'rock','paper','scissors','quit': ")
    player = False
    computer = options[random.randint(0,2)]