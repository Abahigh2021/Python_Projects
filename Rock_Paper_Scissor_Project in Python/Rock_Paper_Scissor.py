# Start the game
# if user == pc it is a tie
# if user input anythning eles means invaild input 
# If user chose R pc chose S or user chose S pc chose p or user chose p pc chose r then user won
# other than  that pc won
import random

while True: 
  user = input("Choose Rock or Paper or Scissor: ")
  
  if user == "Exit":
    print("Thanks for playing! Goodbye!")
    break

  if user not in ["Rock", "Paper", "Scissor"]:
    print("Invalid input, please choose Rock, Paper, or Scissor.")
    continue

  pc = random.choice(["Rock", "Paper" , "Scissor"])
  print("User chose " + user)
  print("PC chose " + pc)

  if user == pc:
    print("it is a tie")
  elif user == "Rock" and pc == "Scissor" or user == "Scissor" and pc == "Paper" or user == "Paper" and pc == "Rock":
    print("You won")
    
else:
    print("You lost")
