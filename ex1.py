import conect

def heaviest_pokemon():
        query = "select name  from pokemon where weight=(select max(weight) as weight from pokemon)"
        return conect.select_query(query)
