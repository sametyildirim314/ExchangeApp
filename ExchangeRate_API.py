import requests
import json

api_key="fcc7c87069fd88240d24e4f8"

api_url="https://v6.exchangerate-api.com/v6/fcc7c87069fd88240d24e4f8/latest/"

Currency_to_exchange=input("Currency to exchange: ")
Currency_to_exchange=Currency_to_exchange.upper()
Currency_to_receive=input("Currency to receive: ")
Currency_to_receive=Currency_to_receive.upper()
amount=float(input(f"How much {Currency_to_exchange} do you want to exchange? "))

result=requests.get(api_url+Currency_to_exchange)

result=json.loads(result.text)


# for i in sonuc:
#     print(i)
x=result["conversion_rates"][Currency_to_receive]

    
print(f"{x*amount:.2f} {Currency_to_receive}")  