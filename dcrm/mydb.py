import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "medoingmagic",
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE elderco")

print("Database created successfully")