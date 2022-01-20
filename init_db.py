import requests

urli = "http://localhost:8080/product"

headersi = { 'Content-Type': 'application/json' }

jsonlst = [{
        "amount": 10,
        "name": "Latte",
        "image": "latte.png",
        "price": 10,
        "type": "hotDrink"

    },
    {   "amount": 10,
        "name": "Cappuccino",
        "image": "cappuccino.png",
        "price": 10,
        "type": "hotDrink"
    },
    {   "amount": 10,
        "name": "Lipton",
        "image": "lipton.png",
        "price": 10,
        "type": "coldDrink"
    },
    {   "amount": 10,
        "name": "Americano",
        "image": "americano.png",
        "price": 10,
        "type": "hotDrink"
    },
    {   "amount": 10,
        "name": "Napoleon",
        "image": "napoleon.png",
        "price": 10,
        "type": "dessert"
    }
]


for jsoni in jsonlst:
    requests.post(url = urli, headers = headersi, json = jsoni)
