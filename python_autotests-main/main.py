import requests

URL = "https://api.pokemonbattle.ru/v2"
HEADER = {'Content-Type':'application/json', 
          'Trainer_token':'d62b3f7fb289d8f751311750259bb68b'}
BODY = {
    "name": "generate",
    "photo_id": -1
}

response = requests.post(url=f'{URL}/pokemons', headers=HEADER, json=BODY)
print(response.text)
ID = response.json()['id']

BODY = {
    "pokemon_id": ID,
    "name": "pikachuu",
    "photo_id": 2
}
response = requests.put(url=f'{URL}/pokemons', headers=HEADER, json=BODY)
print(response.text)


BODY = {
    "pokemon_id": ID
}
response = requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADER, json=BODY)
print(response.text)