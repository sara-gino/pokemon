import conect

def heaviest_pokemon():
    if(conect.connection.open):
        try:
            with conect.connection.cursor() as cursor:
                query = "select name  from pokemon where weight=(select max(weight) as weight from pokemon)"
                cursor.execute(query)
                result = cursor.fetchall()
                return conect.convert_array(result)
        except:
            print("DB Error")


print(heaviest_pokemon())