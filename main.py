import random as r


choicelist = ["R","S","P"]

def computerchoice():
    
    return r.choice(choicelist)

def getuserinput():
    userinput = input("Please enter R for rock,P for paper,S for scissors:")
    return userinput

def game():
    computer = computerchoice()
    print(computer)
    user = getuserinput()
    while user not in choicelist:
        print("Please you entered an incorrect input")
        user = getuserinput()        
    print(f"Player {user} : CPU {computer}")
    if computer == "S" and user == "P" or computer == "R" and user == "S" or computer == "P" and user == "R":
        print("Computer is the winner")
    elif  user == "S" and computer == "P" or user == "R" and computer == "S" or user == "P" and computer == "R":
        print("User is the winner")
    else:
        print("It's a tie")
        game()
        
game()
        
        