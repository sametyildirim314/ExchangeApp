import requests
import json

api_key="fcc7c87069fd88240d24e4f8"

api_url="https://v6.exchangerate-api.com/v6/fcc7c87069fd88240d24e4f8/latest/"

bozulan_doviz=input("Döviz türü: ")
bozulan_doviz=bozulan_doviz.upper()
Alinan_doviz=input("Alinan döviz: ")
Alinan_doviz=Alinan_doviz.upper()
miktar=float(input(f"ne kadar {Alinan_doviz} bozdurmak istiyorsunuz: "))

sonuc=requests.get(api_url+bozulan_doviz)

sonuc=json.loads(sonuc.text)


# for i in sonuc:
#     print(i)
x=sonuc["conversion_rates"][Alinan_doviz]

    
print(f"{x*miktar:.2f} {Alinan_doviz}")   