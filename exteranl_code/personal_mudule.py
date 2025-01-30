from personal_mudule import cal 
import math 
import random2 

Frist = input("Insert you frist number? : ")
Second = input("Insert you Second number? : ")
Operation = input("Insert you operation? : ")

Frist = int(Frist)
Second = int(Second)

result = 0 

if Operation == "+":
     result = cal.adding(Frist , Second)
elif Operation == "-":
    result = cal.sub(Frist , Second)
elif Operation == "*":
    result = cal.multipy(Frist , Second)
elif Operation == "/":
    result = cal.div(Frist , Second)
elif Operation == "pow":
    result = math.pow(Frist , Second)
elif Operation == "sqrt":
    result = math.sqrt(Frist)
elif Operation == "random":
    result = random2.randint(Frist , Second)

print(f" reuslt : {result}")