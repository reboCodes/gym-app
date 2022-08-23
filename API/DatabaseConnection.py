import mysql.connector

class DatabaseConnection:

    def __init__(self, user='rebo', password='password', host='192.168.0.101', database='gym_app'):
        self.__connect(user, password, host, database)

    def __del__(self):
        if self.cnx: self.cnx.close()
    
    def connection(self):
        return self.cnx

    def __connect(self, user, password, host, database):
        self.cnx = None
        try:
            self.cnx = mysql.connector.connect(user=user, password=password, host=host, database=database)
        except:
            return
