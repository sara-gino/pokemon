import conect

def find_roster(trainer_name):
        query=f"select pokemon.name from trainer, pokemon,owner_by where trainer.name=\"{trainer_name}\" and id_pokemon=pokemon.id and id_trainer=trainer.id"
        return conect.select_query(query)
