import requests

Initial_currency = input("Enter your initial currecny: ")
Target_currency =  input("Enter your target currecny: ")

while True:
    try:
        Amount = float(input("Enter your amount: "))
    except:
        print("The amount must be a numerical value! ")
        continue
    
    if Amount == 0:
        print("The amount must greater then 0! ")
    else:
        break    


    
url = "https://api.apilayer.com/fixer/convert?to={Target_currency}&from={Initial_currency}&amount={Amount}"


payload = {}
headers= {
  "apikey": "uHQTiBV5Y90CbJtrSNRMuPJu7UyIDVJg"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code

if status_code != 200:
    print("Sorry, somthing went wrong. Please try again later. ")
    quit()


result = response.json()
result["result"]
print(f"{Amount} {Initial_currency} = {result["result"]} {Target_currency}" )