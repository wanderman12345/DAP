
import mysql.connector as connector
from numpy import isin

# Gives connection back

def get_connection():
    mysql_connect = connector.connect(
    port = 3306,
    host = "localhost",
    user = "root",
    password = "password",
    database = "SEDAP"
    )
    return mysql_connect

def close_connection(conn):
    conn.disconnect()
