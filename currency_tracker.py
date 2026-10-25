import requests
import json
import sys

try:
    cost = input("Enter the price in KES:")
    converted_cost = float(cost)
    if converted_cost >0:
       print(f"Amount entered: KES {converted_cost:.2f}")        
    else:
        print("Please enter an amount greater than zero")
        sys.exit()
            
except ValueError:
    print("Invalid amount. Please enter a valid number")
    sys.exit()
    


url = "https://open.er-api.com/v6/latest/KES"
try:
    response = requests.get(url, timeout=10)
    if response.status_code == 200:
        data = response.json()  
        if data["result"] == "success":          
            rates = data["rates"]
            usd = rates["USD"]
            eur = rates["EUR"]
            gbp = rates["GBP"]
            print("The rates are as follows:")
            print(f"USD: {usd}")
            print(f"EUR: {eur}")
            print(f"GBP: {gbp}")

            #Converting the KES price
            #Foreign currency amount = KES amount * exchange rate
            usd_amount = converted_cost * usd
            eur_amount = converted_cost * eur
            gbp_amount = converted_cost * gbp

            print("Converting...")
            print("Your converted amount is:")
            print(f"USD: {usd_amount:.2f}")
            print(f"EUR: {eur_amount:.2f}")
            print(f"GBP: {gbp_amount:.2f}")

        else:
            print("The API could not provide the exchange rates")

    elif response.status_code == 404:
        print("API endpoint not found")
    else:
        print("Something went wrong")

except requests.RequestException:
    print("Unable to connect to the exchange-rate service. Please try again")






