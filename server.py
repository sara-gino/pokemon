import flask
import conect
import requests
from flask import Flask

app=Flask(__name__)

@app.route("/types/<pokemon_name> ")
def insert_types(pokemon_name):
    m_url = 'https://pokeapi.co/api/v2/pokemon'
    res = requests.get(url=m_url)
    for obj in res["results"]:
        if(obj["name"]==pokemon_name):
            m_url = obj["url"]
            res = requests.get(url=m_url)
            break
    for type in res["types"]:
        try:
            with conect.connection.cursor() as cursor:
                query = f"insert into pokemon (type) values ({id},\"{name}\",\"{type}\",{height},{weight})"
                cursor.execute(query)
        except:
            print("DB Error")




if(__name__=="__main__"):
    app.run(port=3000)