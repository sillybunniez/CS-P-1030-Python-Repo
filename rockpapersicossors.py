import random 

#Algorithm
def rockpapersicossors():
    computer = ""
    chosen = random.randint(1,3)
    #1 = r
    #2 = p
    #3 = s
    
    if chosen == 1:
        computer = "r"
    elif chosen == 2:
        computer = "p"
    else:
        computer = "s" 
    
    #Player and game algorithm
    player = input("Please select either Rock (r), Paper(p), or Scissors(s): ")
    
    #Draw
    if computer == player:
        winner == True
        print("Draw!")
    #player wins
    elif computer == "s" and player =="r" or computer == "r" and player == "p" or computer == "p" and player == "s":
        print("You win!")
        winner == True
    #Computer wins
    else:
        print("Computer wins!")
        winner == True
    return(winner)

winner = False
#Computer Selection
while winner == False:
    rockpapersicossors
#If winner == True
    if winner == True:
        playagain = input("Do you want to play again? (Y) or (N) ")
        if playagain == "Y":
            winner == False
        else: 
            print("Ending Game.")
