from database.connection import databaseConnection

def getFruits(fruitname:str = None):
    database_config = databaseConnection()
    cursor = database_config.cursor(dictionary = True)
    if fruitname:
        cursor.execute("select * from fruits where name like %s;",(f"%{fruitname}%",))
        fruits = cursor.fetchall()
        
        cursor.close()
        database_config.close()

        return fruits
    
    cursor.execute('select * from fruits;')

    fruits = cursor.fetchall()

    cursor.close()
    database_config.close()

    return fruits
