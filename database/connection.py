import mysql.connector as SQLC


def databaseConnection():
    database_config = SQLC.connect(
    host = 'localhost',
    user = 'root',
    password = 'mysql123',
    database = 'market'

)
    
    return database_config
# cursor = database_config.cursor()

