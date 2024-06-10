import mysql.connector

def connect():
    condb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="loja")
    return condb
