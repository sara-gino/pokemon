import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="Sara123ginoo",
    db="noa",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)

def select_query(query):
    if (connection.open):
        try:
            with connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
                return result
        except:
            print("DB Error")
            exit()

def insert_query(query):
    if (connection.open):
        try:
            with connection.cursor() as cursor:
                cursor.execute(query)
                connection.commit()
        except:
            print("DB Error")
            exit()

def convert_array(array):
    list=[]
    for dict in array:
        for key in dict:
            list.append(dict[key])
    return list