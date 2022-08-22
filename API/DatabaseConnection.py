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


db = DatabaseConnection()

muscleHitList = [{"muscle": "Chest", "activation_level": 8}, {"muscle": "Tricep", "activation_level": 5}]
setList = [{"weight_done": 225, "reps": 6, "reps_in_reserve": None, "time_taken": None}, 
            {"weight_done": 225, "reps": 6, "reps_in_reserve": None, "time_taken": None}]

ExerciseType(db.connection(), "Bench Press", 8, muscleHitList).create()

benchPress = Exercise(db.connection(), 1, "Bench Press", "Bench Press", setList).create()