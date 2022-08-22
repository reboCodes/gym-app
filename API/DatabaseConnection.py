import mysql.connector

from objects import *

class DatabaseConnection:

    def __init__(self, user='rebo', password='password', host='192.168.0.101', database='gym_app', logging=False):
        try:
            self.cnx = mysql.connector.connect(user=user, password=password, host=host, database=database)
        except:
            print("Could not create connection to database.")

    def __del__(self):
        self.cnx.close()
    
    def connection(self):
        return self.cnx
