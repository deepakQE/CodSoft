import random
while True:
    a = input(" choose rock, paper, or scissors :  ")
    game = ['rock', 'paper', 'scissors']
    computer = random.choice(game)
    if  a == computer:
        print("Draw")
    # User  Wins program 
    elif a == "rock" and computer == 'scissors':
        print("You win")
    
    elif a == "scissors" and computer == "paper":
        print("You win")
    
    elif a == "paper" and computer == "rock":
        print("You win")
    #computer program 

    elif a == "scissors" and computer == "rock":
        print("Computer win")
    
    elif a == "paper" and computer == "scissors":
        print("Computer win")
    elif a == "rock" and computer == "paper":
        print("Computer win")
    # if any error formed create the error or print invalid value the user can use interger symbol and other things then it can create perform else 
    else:
        print("Invalid Input! Try again.")
    x = input("Play more game write 'Yes' OR  exit  for 'No'  :").lower()
    if x  == 'yes':
        continue
    else:
        break
