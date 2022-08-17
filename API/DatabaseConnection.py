import mysql.connector

class DatabaseConnection:

    def __init__(self, user='rebo', password='password', host='192.168.0.101', database='gym_app'):
        self.cnx = mysql.connector.connect(user=user, password=password, host=host, database=database)
        print(self.cnx)

    def __del__(self):
        self.cnx.close()

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
        cursor = self.cnx.cursor()
        cursor.execute("INSERT INTO MUSCLE (muscle) VALUES (%s)", (muscle, ))
        self.cnx.commit()

    def deleteMuscle(self, muscle):
        cursor = self.cnx.cursor()
        cursor.execute("DELETE FROM MUSCLE WHERE muscle = %s", (muscle, ))
        self.cnx.commit()

    def getMuscle(self, muscle=None):
        cursor = self.cnx.cursor()
        if muscle:
            cursor.execute("SELECT muscle FROM MUSCLE WHERE muscle = '%s'", (muscle, ))
        else:
            cursor.execute("SELECT muscle FROM MUSCLE")
        return cursor.fetchall()

    # exercise_type (exercise_type_name, xfr, exercise_type_id)
    def createExerciseType(self):
        return
    def deleteExerciseType(self):
        return
    def updateExersiceType(self):
        return
    def getExercise(self):
        return

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