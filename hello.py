# Asks the user for their name and stores it as a variable
name = input("What is your name? ")
# yofb = “Year of Birth” Asks the user for their year of birth and also stores it as a variable
yofb = int(input("What year were you born? "))
# F string is to show the txt in the console; This line prints a string to the console and uses {contenation} to take the stored variables from the user's input and displays them in the printed string.
txt = f"Hello {name}, you were born in {yofb}."
# This prints the F string to the console for you to see!
print(txt)