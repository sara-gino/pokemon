import conect

def find_owners(pokemon_name):
    if(conect.connection.open):
        try:
            with conect.connection.cursor() as cursor:
                query=f"select trainer.name from trainer, pokemon,owner_by where pokemon.name=\"{pokemon_name}\" and id_pokemon=pokemon.id and id_trainer=trainer.id"
                cursor.execute(query)
                result=cursor.fetchall()
                return conect.convert_array(result)
        except:
            print("DB Error")
print(find_owners("gengar"))