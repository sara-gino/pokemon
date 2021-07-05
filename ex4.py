import conect
def find_roster(trainer_name):
    if(conect.connection.open):
        try:
            with conect.connection.cursor() as cursor:
                query=f"select pokemon.name from trainer, pokemon,owner_by where trainer.name=\"{trainer_name}\" and id_pokemon=pokemon.id and id_trainer=trainer.id"
                cursor.execute(query)
                result=cursor.fetchall()
                return conect.convert_array(result)
        except:
            print("DB Error")
print(find_roster("Loga"))