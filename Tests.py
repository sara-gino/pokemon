import pytest
from flask import Flask, Request, Response,request
import requests
import sql_funcs
import json


def add_pokemon():
    name_url = 'http://localhost:3000/pokemon'
    res = requests.post(url=name_url,json=json.dumps({"name":"yanma","id":300,"types":["bug","flying"],"height":12,"weight":380,"ownedBy":[]}))
    print(res.text)
    name_url = 'http://localhost:3000/pokemons_type/bug'
    res = requests.get(url=name_url)
    assert 'yanma' in res
    name_url = 'http://localhost:3000/pokemons_type/flying'
    res = requests.get(url=name_url)
    assert 'yanma' in res
    name_url = 'http://localhost:3000/pokemon'
    res = requests.post(url=name_url,json={"name": "yanma", "id": 3, "types": ["bug", "flying"], "height": 12, "weight": 380,
                               "ownedBy": []})

def Get_pokemons_by_type():
    name_url = 'http://localhost:3000/types/eevee'
    res = requests.get(url=name_url)
    name_url = 'http://localhost:3000/pokemons_type/normal'
    res = requests.get(url=name_url)
    assert 'eevee' in res.json()
    name_url = 'http://localhost:3000/types/eevee'
    res = requests.get(url=name_url)

def update_pokemon_types():
    name_url = 'http://localhost:3000/types/venusaur'
    res = requests.get(url=name_url)
    name_url = 'http://localhost:3000/pokemons_type/grass'
    res = requests.get(url=name_url)
    assert 'venusaur' in res.json()
    name_url = 'http://localhost:3000/pokemons_type/poison'
    res = requests.get(url=name_url)
    assert 'venusaur' in res.json()

def Get_pokemons_by_owner():
    name_url = 'http://localhost:3000/pokemons_trainer/Drasna'
    assert requests.get(url=name_url).status_code == 200

def Get_owners_of_pokemon():
    name_url = 'http://localhost:3000/trainers/charmander'
    assert requests.get(url=name_url).status_code == 200

def Evolve_test():
    name_url = 'http://localhost:3000/evolve'
    sql_funcs.insert_owner_by(127, 19)
    """pinsir pokemon can not evolve"""
    PARAMS = {"pokemon_name":"pinsir","trainer_name":"Whitney"}
    res = request.get(url=name_url,params=PARAMS)
    print(res)

    """Archie does not have a spearow pokemon"""
    PARAMS = {"pokemon_name":"spearow","trainer_name":"Archie"}
    res = requests.get(url=name_url, params=PARAMS)

    """gloom"""
    sql_funcs.insert_owner_by(43, 19)
    PARAMS ={"pokemon_name":"oddish","trainer_name":"Whitney"}
    res = requests.get(url=name_url, params=PARAMS)

    """this pokemon already evolved"""
    PARAMS = {"pokemon_name": "oddish", "trainer_name": "Whitney"}
    res = requests.get(url=name_url, params=PARAMS)

    """assert that gloom in res"""
    name_url = 'http://localhost:3000/pokemons_trainer/Whitney'
    res = requests.get(url=name_url)
    print(res.json())
    assert 'gloom' in res.json()

    """this pokemon already evolved"""
    name_url = 'http://localhost:3000/evolve'
    sql_funcs.insert_owner_by(25, 19)
    sql_funcs.insert_owner_by(26, 19)
    PARAMS = {"pokemon_name": "pikachu", "trainer_name": "Whitney"}
    res = requests.get(url=name_url, params=PARAMS)
    print(res.text)

# Evolve_test()
# Get_pokemons_by_owner()
# Get_owners_of_pokemon()
# Get_pokemons_by_type()
# update_pokemon_types()