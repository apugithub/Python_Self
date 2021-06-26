import requests
import json

url = "https://weatherapi-com.p.rapidapi.com/forecast.json"

querystring = {"q":"Oslo","days":"5"}

headers = {
    'x-rapidapi-key': "caca550ce0msh841b31180f7b290p13c608jsn6b9a68723b06",
    'x-rapidapi-host': "weatherapi-com.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
h = requests.get(url=url, params=querystring, headers=headers)
data = response.json()
print(response.json())

