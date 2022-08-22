

class Muscle:
    def __init__(self, connection, muscle=None):
        self.muscle = muscle
        self.connection = connection
        self.cursor = self.connection.cursor()
    
    def create(self):
        try:
            self.cursor.execute("INSERT IGNORE INTO MUSCLE (muscle) VALUES (%s);", (self.muscle, ))
            self.connection.commit()
            print(f"Added {self.muscle} to MUSCLE.")
        except:
            print(f"Could not add {self.muscle} into MUSCLE.")

    def delete(self):
        try:
            self.cursor.execute("DELETE FROM MUSCLE WHERE muscle = %s;", (self.muscle, ))
            self.connection.commit()
            print(f"Deleted {self.muscle} from MUSCLE.")
        except:
            print(f"Could not delete {self.muscle} from MUSCLE.")

    def deleteAll(self):
        try:
            self.cursor.execute("DELETE FROM MUSCLE;")
            self.connection.commit()
            print(f"Deleted all records from MUSCLE.")
        except:
            print(f"Could not delete all records from MUSCLE.")

    def get(self):
        try:
            self.cursor.execute("SELECT muscle FROM MUSCLE WHERE muscle = '%s';", (self.muscle, ))
            return self.cursor.fetchone()
        except:
            print(f"Couldn't get {self.muscle}, it does not exist.")

    def getAll(self):
        try:
            self.cursor.execute("SELECT muscle FROM MUSCLE;")
            return self.cursor.fetchall()
        except:
            print(f"Couldn't get Muscles, none exist.")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

class MuscleHit:
    def __init__(self, connection, exerciseType, muscle=None, activationLevel=None):
        self.connection = connection
        self.cursor = self.connection.cursor()
        self.exerciseType = exerciseType
        self.muscle = muscle
        self.activationLevel = activationLevel

    def create(self):
        try:
            Muscle(self.connection, self.muscle).create()
            sql = "INSERT INTO MUSCLE_HIT (muscle, activation_level, exercise_type) VALUES (%s, %s, %s);"
            self.cursor.execute(sql, (self.muscle, self.activationLevel, self.exerciseType))
            self.connection.commit()
            print(f"Added {self.muscle}, {self.activationLevel}, {self.exerciseType} into MUSCLE_HIT.")
        except:
            print(f"Could not add {self.muscle}, {self.activationLevel}, {self.exerciseType} into MUSCLE_HIT.")

    def delete(self):
        try:
            sql = "DELETE FROM MUSCLE_HIT WHERE muscle = %s AND exercise_type = %s;"
            self.cursor.execute(sql, (self.muscle, self.exerciseType))
            self.connection.commit()
            print(f"Deleted {self.muscle}, {self.exerciseType} from MUSCLE_HIT")
        except:
            print(f"Could not delete {self.muscle}, {self.exerciseType} from MUSCLE_HIT, it does not exist.")

    def deleteByExerciseType(self):
        try:
            sql = "DELETE FROM MUSCLE_HIT WHERE exercise_type = %s;"
            self.cursor.execute(sql, (self.exerciseType,))
            self.connection.commit()
            print(f"Deleted records from MUSCLE_HIT where exercise_type = {self.exerciseType}.")
        except:
            print(f"Could not delete records from MUSCLE_HIT where exercise_type = {self.exerciseType}.")

    def get(self):
        try:
            sql = "SELECT muscle FROM MUSCLE_HIT WHERE muscle = %s AND exercise_type = %s;"
            self.cursor.execute(sql, (self.muscle, self.exerciseType))
            return self.cursor.fetchone()
        except:
            print(f"Could not get {self.muscle}, {self.exerciseType} from MUSCLE_HIT, it does not exist.")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

class ExerciseType:
    def __init__(self, connection, exerciseType, xfr=None, muscleHitList=None):
        self.connection = connection
        self.cursor = self.connection.cursor()
        self.exerciseType = exerciseType
        self.xfr = xfr
        self.muscleHitList = muscleHitList

    def create(self):
        try:
            sql = "INSERT INTO EXERCISE_TYPE (exercise_type, xfr) VALUES (%s, %s);"
            self.cursor.execute(sql, (self.exerciseType, self.xfr))
            self.connection.commit()
            print(f"Added {self.exerciseType}, {self.xfr} into EXERCISE_TYPE.")

            for muscleHit in self.muscleHitList:
                MuscleHit(self.connection, self.exerciseType, muscleHit["muscle"], muscleHit["acticationLevel"]).create()
        except:
            print(f"Could not add {self.exerciseType}, {self.xfr} into EXERCISE_TYPE.")

    def delete(self):
        MuscleHit(self.connection, self.exerciseType).deleteByExerciseType()
        sql = "DELETE FROM EXERCISE_TYPE WHERE exercise_type = %s;"
        self.cursor.execute(sql, (self.exerciseType,))
        self.connection.commit()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    
# exercise (exercise_type(exercise_type_name, exercise_type_id, xfr), sets_done(exercise_id, set_id), exercise_id)

# User (fname, lname, dob, weight, lbs_kg, username, user_id)

# exercise (workout_id, exercise_type(exercise_type_name, exercise_type_id, xfr), sets_done(exercise_id, set_id), exercise_id)

# set (set_id, weight_done, reps, reps_in_reserve, time_taken)

# workout_plan (workout_id, user_id, date, start_time, end_time, is_started, list of exercises)