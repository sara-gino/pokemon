import conect

def find_by_type(type):
    if(conect.connection.open):
        try:
            with conect.connection.cursor() as cursor:
                query = f"select name from pokemon where type=\"{type}\""
                cursor.execute(query)
                result = cursor.fetchall()
                return conect.convert_array(result)
        except:
            print("DB Error")

print(find_by_type("grass"))