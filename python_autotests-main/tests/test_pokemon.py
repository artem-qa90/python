import requests
import pytest

URL = "https://api.pokemonbattle.ru/v2"
HEADER = {'Content-Type':'application/json'}
TOKEN = {'d62b3f7fb289d8f751311750259bb68b'}
TRAINER_ID = '7804'

def test_status_code():
    response = requests.get(url=f'{URL}/trainers', params={'trainer_id' : TRAINER_ID})
    assert response.status_code == 200, "Unexpected status code"

def test_get_trainer_by_id():
    response = requests.get(url=f'{URL}/trainers', params={'trainer_id' : TRAINER_ID})
    assert response.json()["data"][0]['trainer_name'] == 'Artem47', 'Ups, wrong name'