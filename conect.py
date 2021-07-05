import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="Sara123ginoo",
    db="pokemon_db",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)

def convert_array(array):
    list=[]
    for dict in array:
        for key in dict:
            list.append(dict[key])
    return list