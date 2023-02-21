import requests

API = "https://opentdb.com/api.php"
parameters = {
    "amount": 10,
    "type": "boolean",
}

response = requests.get(API, parameters)
data = response.json()
question_data = data["results"]
