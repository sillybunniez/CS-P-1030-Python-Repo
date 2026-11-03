import random 

computer = ""
chosen = random.randint(1,3)
print(chosen)
"""
1 = r
2 = p
3 = s
"""
if chosen == 1:
    computer = "r"
elif chosen == 2:
    computer = "p"
else:
    computer = "s" 
print(computer)

player = input("Please select either Rock, Paper, or Scissors: ")

#Draw
if computer == player:
    print("Draw!")
#player wins
elif computer == "s" and player =="r" or computer == "r" and player == "p" or computer == "p" and player == "s":
    print("You win!")
#Computer wins
else:
    print("Computer wins!")
