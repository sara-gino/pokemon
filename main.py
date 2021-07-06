import json
import sql_funcs

with open('pokemon_data.json') as f:
    data = json.load(f)
    for pokemon in data:
        sql_funcs.insert_pokemon(pokemon["id"], pokemon["name"],0, pokemon["height"], pokemon["weight"],pokemon["ownedBy"])
