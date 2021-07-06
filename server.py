from flask import Flask, Request, Response,request
import requests
import json
import conect
import sql_funcs
from ex1 import heaviest_pokemon
from ex3 import find_owners
from ex4 import find_roster
from ex2 import find_by_type

app=Flask(__name__)
@app.route('/')
def welcome():
    return "welcome pokemon play"

@app.route("/types/<pokemon_name>")
def insert_types(pokemon_name):
    id_pokemon = sql_funcs.get_id_by_name(pokemon_name, "pokemon")
    try:
        m_url = f'https://pokeapi.co/api/v2/pokemon/{id_pokemon}'
        res = requests.get(url=m_url,verify=False)
        res=res.json()
        for type in res["types"]:
            name = type["type"]["name"]
            sql_funcs.insert_type(id_pokemon,name)
        return "types added to {} pokemon".format(pokemon_name)
    except:
            return "pokemon name not valid"

@app.route("/pokemon",methods=["POST"])
def add_pokemon():
    pokemon = request.get_json()
    res=sql_funcs.insert_pokemon(pokemon["id"],pokemon["name"],pokemon["types"],pokemon["height"],pokemon["weight"],pokemon["ownedBy"])
    if res:
        return res
    return "the pokemon added"

@app.route('/heaviest_pokemon')
def get_heaviest_pokemon():
    return Response(json.dumps(conect.convert_array(heaviest_pokemon())))

@app.route('/pokemons_trainer/<trainer>')
def find_pokemons(trainer):
    return Response(json.dumps(conect.convert_array(find_roster(trainer))))

@app.route('/pokemons_type/<type>')
def find_pokemon_by_type(type):
    return Response(json.dumps(conect.convert_array(find_by_type(type))))

@app.route('/trainers/<pokemon>')
def find_trainers(pokemon):
    return Response(json.dumps(conect.convert_array(find_owners(pokemon))))

@app.route("/delete_pokemon",methods=["DELETE"])
def delete_pokemon():
    trainer_name=request.get_json()["trainer_name"]
    pokemon_name=request.get_json()["pokemon_name"]
    id_pokemon = sql_funcs.get_id_by_name(pokemon_name, "pokemon")
    id_trainer = sql_funcs.get_id_by_name(trainer_name, "trainer")
    sql_funcs.delete_pokemon(id_pokemon,id_trainer)
    return "delete pokemon {} of trainer {}".format(pokemon_name,trainer_name)

@app.route("/evolve")
def evolve():
    pokemon_name=request.get_json()["pokemon_name"]
    trainer_name=request.get_json()["trainer_name"]
    id_pokemon=sql_funcs.get_id_by_name(pokemon_name,"pokemon")
    id_trainer = sql_funcs.get_id_by_name(trainer_name,"trainer")
    if not id_pokemon:
        return "{} pokemon not exist".format(pokemon_name)
    if not id_trainer:
        return "{} trainer not exist".format(trainer_name)
    owner_by=sql_funcs.is_owner_by(id_pokemon,id_trainer)
    if not owner_by:
        return "{} does not have a {} pokemon".format(trainer_name,pokemon_name)
    m_url = f'https://pokeapi.co/api/v2/pokemon/{id_pokemon}'
    res = requests.get(url=m_url,verify=False)
    res = res.json()
    m_url= res["species"]["url"]
    res = requests.get(url=m_url,verify=False)
    res=res.json()
    m_url=res["evolution_chain"]["url"]
    res = requests.get(url=m_url,verify=False)
    res=res.json()
    chain=res["chain"]
    try:
        name_next=chain["evolves_to"][0]["species"]["name"]
    except:
        return "{} pokemon can not evolve".format(pokemon_name)
    id_pokemon=sql_funcs.get_id_by_name(name_next,"pokemon")
    owner_by=sql_funcs.is_owner_by(id_pokemon,id_trainer)
    if(not owner_by):
        sql_funcs.insert_owner_by(id_pokemon,id_trainer)
        return Response(name_next)
    else:
        return "this pokemon already evolved"

if(__name__=="__main__"):
    app.run(port=3000)