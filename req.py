import requests

headers = {'Accept': 'application/json',
           
        "X_country": "AE",
    "X_vehicle_type": "CAR",
        }

r = requests.get('https://listing-service.c24.tech/v2/vehicle?isSeoFilter=true&sf=city:DU&sf=gaId:1120805531.1696266648&size=25&spath=buy-used-cars-dubai&page=0&variant=filterV5', headers=headers)

print(r.json())