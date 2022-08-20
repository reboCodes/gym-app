import mysql.connector

class DatabaseConnection:

    def __init__(self, user='rebo', password='password', host='192.168.0.101', database='gym_app', logging=False):
        self.cnx = mysql.connector.connect(user=user, password=password, host=host, database=database)
        self.logging = logging
        self.log(self.cnx)

    def __del__(self):
        self.cnx.close()

    def log(self, data):
        if self.logging:
            print(data)

    ### Objects

    # User
    # Muscle
    # Exercise
    # Exercise Type
    # Set
    # Workout Plan

    # User (fname, lname, dob, weight, lbs_kg, username, user_id)
    def createUser(self):
        return
    def updateUser(self):
        return
    def deleteUser(self):
        return
    def getUser(self):
        return

    # Muscle (muscle, muscle_id)
    def createMuscle(self, muscle):
        try:
            self.log(f"Trying to add {muscle} into MUSCLE.")
            cursor = self.cnx.cursor()
            cursor.execute("INSERT INTO MUSCLE (muscle) VALUES (%s);", (muscle, ))
            self.cnx.commit()
            self.log(f"Added {muscle} into MUSCLE.")
        except:
            self.log(f"Could not add {muscle} into MUSCLE.")

    def deleteMuscle(self, muscle):
        cursor = self.cnx.cursor()
        cursor.execute("DELETE FROM MUSCLE WHERE muscle = %s;", (muscle, ))
        self.cnx.commit()

    def getMuscle(self, muscle=None):
        cursor = self.cnx.cursor()
        if muscle:
            cursor.execute("SELECT muscle FROM MUSCLE WHERE muscle = '%s';", (muscle, ))
        else:
            cursor.execute("SELECT muscle FROM MUSCLE;")
        return cursor.fetchall()

    # muscle_hit (muscle, activation_level, exercise_type)
    def createMuscleHit(self, muscle, activationLevel, exerciseTypeName):
        try:
            self.log(f"Trying to add {muscle}, {activationLevel}, {exerciseTypeName} into MUSCLE_HIT.")
            cursor = self.cnx.cursor()
            sql = "INSERT INTO MUSCLE_HIT (muscle, activation_level, exercise_type) VALUES (%s, %s, %s);"
            cursor.execute(sql, (muscle, activationLevel, exerciseTypeName))
            self.cnx.commit()
            self.log(f"Added {muscle}, {activationLevel}, {exerciseTypeName} into MUSCLE_HIT.")
            return True
        except:
            self.log(f"Could not add {muscle}, {activationLevel}, {exerciseTypeName} into MUSCLE_HIT.")
            return False

    def deleteMuscleHit(self):
        return

    # exercise_type (exercise_type_name, xfr, exercise_type_id)
    def createExerciseType(self, exerciseTypeName, xfr, muscleHitList):
        try:
            self.log(f"Trying to add {exerciseTypeName}, {xfr} into EXERCISE_TYPE.")
            cursor = self.cnx.cursor()
            cursor.execute("INSERT INTO EXERCISE_TYPE (exercise_type, xfr) VALUES (%s, %s);", (exerciseTypeName, xfr))
            self.cnx.commit()
            self.log(f"Added {exerciseTypeName}, {xfr} into EXERCISE_TYPE.")
            for muscleHitTuple in muscleHitList:
                if not self.createMuscleHit(muscleHitTuple[0] ,muscleHitTuple[1], exerciseTypeName):
                    self.createMuscle(muscleHitTuple[0])
                    self.createMuscleHit(muscleHitTuple[0] ,muscleHitTuple[1], exerciseTypeName)
        except:
            self.log(f"Could not add {exerciseTypeName}, {xfr} into EXERCISE_TYPE.")

    def deleteExerciseType(self, exerciseTypeName):
        cursor = self.cnx.cursor()
        cursor.execute("DELETE FROM EXERCISE_TYPE WHERE exercise_type = %s;", (exerciseTypeName,))
        self.cnx.commit()
        return

    def updateExersiceType(self, exersice_type_name):
        return

    def getExercise(self, exerciseTypeName, ):
        try:
            cursor = self.cnx.cursor()
            cursor.execute("SELECT * FROM ", (exerciseTypeName))
            return cursor.fetchone()
        except:
            self.log(f"{exerciseTypeName} doesn't exists")

    # exercise (workout_id, exercise_type(exercise_type_name, exercise_type_id, xfr), sets_done(exercise_id, set_id), exercise_id)
    
    def createExercise(self):
        return
    def deleteExercise(self):
        return
    def updateExercise(self):
        return
    def getExercise(self):
        return

    # set (set_id, weight_done, reps, reps_in_reserve, time_taken)
    def createSet(self):
        return
    def deleteSet(self):
        return
    def updateSet(self):
        return
    def getSet(self):
        return
    
    # workout_plan (workout_id, user_id, date, start_time, end_time, is_started, list of exercises)
    def createWorkoutPlan(self):
        return
    def deleteWorkoutPlan(self):
        return
    def updateWorkoutPlan(self):
        return
    def getWorkoutPlan(self):
        return


db = DatabaseConnection()

db.deleteMuscle("Chest")
db.deleteMuscle("Tricep")
db.deleteExerciseType("Bench Press")
db.createExerciseType("Bench Press", 6, [("Chest",9),("Tricep",6)])