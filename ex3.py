import conect

def find_owners(pokemon_name):
    query=f"select trainer.name from trainer, pokemon,owner_by where pokemon.name=\"{pokemon_name}\" and id_pokemon=pokemon.id and id_trainer=trainer.id"
    return conect.select_query(query)
