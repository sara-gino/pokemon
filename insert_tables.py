import pymysql
import json
import conect

def insert_data(id, name, type, height, weight, ownedBy):
    try:
        with conect.connection.cursor() as cursor:
            # query = f"insert into pokemon (id,name,type, height,weight) values ({id},\"{name}\",\"{type}\",{height},{weight})"
            # cursor.execute(query)
            # connection.commit()
            for own in ownedBy:
                name = own["name"]
                town=own["town"]
                query = f"select id from trainer where name=\"{name}\" and town=\"{town}\""
                cursor.execute(query)
                result = cursor.fetchall()
                if(len(result) ==0):
                    query = f"INSERT into trainer (name,town) values (\"{name}\",\"{town}\")"
                    cursor.execute(query)
                    conect.connection.commit()
                    query= f"select id from trainer where name=\"{name}\" and town=\"{town}\""
                    cursor.execute(query)
                    result = cursor.fetchall()
                    id_trainer=result["id"]
                    query = f"INSERT into owner_by (id_pokemon,id_trainer) values (\"{id}\",\"{id_trainer}\")"
                cursor.execute(query)
                conect.connection.commit()
    except:
        print("DB Error")

with open('pokemon_data.json') as f:
        data = json.load(f)
        for pokemon in data:
            insert_data(pokemon["id"],pokemon["name"],pokemon["type"],pokemon["height"],pokemon["weight"],pokemon["ownedBy"])

