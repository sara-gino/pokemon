import conect

def insert_type(id,name):
    query = f"select * from type where id={id} and name=\"{name}\""
    if not conect.select_query(query):
        query = f"insert into type (id,name) values ({id},\"{name}\")"
        conect.insert_query(query)

def delete_pokemon(id_pokemon,id_trainer):
    query = f"delete from owner_by where id_pokemon={id_pokemon} and id_trainer={id_trainer}"
    conect.insert_query(query)

def insert_pokemon(id, name, types, height, weight, ownedBy):
    query = f"select id from pokemon where name=\"{name}\""
    if conect.select_query(query):
        return "this pokemon name already exist"
    query = f"insert into pokemon (id,name,height,weight) values ({id},\"{name}\",{height},{weight})"
    conect.insert_query(query)
    if types!=0:
        for type in types:
            if(type(type)==str):
                name = type
            else:
                name = type["type"]["name"]
            query = f"select id from type where name=\"{name}\" and id=\"{id}\""
            result=conect.select_query(query)
            if len(result)==0:
                query = f"insert into type(id,name) values({id},\"{name}\")"
                conect.insert_query(query)
    for own in ownedBy:
        name = own["name"]
        town=own["town"]
        query = f"select id from trainer where name=\"{name}\" and town=\"{town}\""
        result=conect.select_query(query)
        if len(result)==0:
            query = f"INSERT into trainer (name,town) values (\"{name}\",\"{town}\")"
            conect.insert_query(query)
            query= f"select id from trainer where name=\"{name}\" and town=\"{town}\""
            result=conect.convert_array(conect.select_query(query))
            id_trainer=result[0]
            query = f"INSERT into owner_by (id_pokemon,id_trainer) values (\"{id}\",\"{id_trainer}\")"
            conect.insert_query(query)

def get_id_by_name(name,name_table):
    query=f"select id from {name_table} where name=\"{name}\""
    res = conect.select_query(query)
    if len(res)==0:
        return False
    return res[0]["id"]

def is_owner_by(id_pokemon,id_trainer):
    query = f"select * from owner_by where id_pokemon=\"{id_pokemon}\" and id_trainer=\"{id_trainer}\""
    res = conect.select_query(query)
    if(len(res)==0):
        return False
    return True

def insert_owner_by(id_pokemon,id_trainer):
    query = f"INSERT into owner_by (id_pokemon,id_trainer) values ({id_pokemon},{id_trainer})"
    conect.insert_query(query)


