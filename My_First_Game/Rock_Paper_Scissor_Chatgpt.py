import random

while True: 
    user = input("Choose Rock, Paper, or Scissor (or type 'exit' to quit): ").capitalize()
    
    if user == "Exit":
        print("Thanks for playing! Goodbye!")
        break
    
    if user not in ["Rock", "Paper", "Scissor"]:
        print("Invalid input, please choose Rock, Paper, or Scissor.")
        continue
    
    pc = random.choice(["Rock", "Paper", "Scissor"])
    
    print("User chose " + user)
    print("PC chose " + pc)
    
    if user == pc:
        print("It's a tie!")
    elif (user == "Rock" and pc == "Scissor") or (user == "Scissor" and pc == "Paper") or (user == "Paper" and pc == "Rock"):
        print("You won!")
    else:
        print("You lost!")
