import conect

def find_by_type(type):
        query = f"select pokemon.name from type, pokemon where pokemon.id=type.id and type.name=\"{type}\""
        return conect.select_query(query)
