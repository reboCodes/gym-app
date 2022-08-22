

class Muscle:
    def __init__(self, connection, muscle=None):
        self.muscle = muscle
        self.connection = connection
        self.cursor = self.connection.cursor()
    
    def create(self):
        try:
            self.cursor.execute("INSERT IGNORE INTO MUSCLE (muscle) VALUES (%s);", (self.muscle, ))
            self.connection.commit()
            print(f"Created record {self.muscle} in MUSCLE.")
        except:
            print(f"Could not create record {self.muscle} in MUSCLE.")

    def delete(self):
        try:
            self.cursor.execute("FROM MUSCLE WHERE muscle = %s;", (self.muscle, ))
            self.connection.commit()
            print(f"Deleted record {self.muscle} from MUSCLE.")
        except:
            print(f"Could not delete record {self.muscle} from MUSCLE.")

    def deleteAll(self):
        try:
            self.cursor.execute("FROM MUSCLE;")
            self.connection.commit()
            print(f"Deleted all records from MUSCLE.")
        except:
            print(f"Could not delete all records from MUSCLE.")

    def get(self):
        try:
            self.cursor.execute("SELECT muscle FROM MUSCLE WHERE muscle = '%s';", (self.muscle, ))
            return self.cursor.fetchone()
        except:
            print(f"Could not get record {self.muscle} from MUSCLE.")

    def getAll(self):
        try:
            self.cursor.execute("SELECT muscle FROM MUSCLE;")
            return self.cursor.fetchall()
        except:
            print(f"Couldn't get record from MUSCLE, none exist.")

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
            print(f"Created record {self.muscle}, {self.activationLevel}, {self.exerciseType} in MUSCLE_HIT.")
        except:
            print(f"Could not create record {self.muscle}, {self.activationLevel}, {self.exerciseType} in MUSCLE_HIT.")
    
    def update(self, activationLevel):
        if not self.muscle or not self.exerciseType:
            print("Updating a record in MUSCLE_HIT requires values for muscle and exercise_type.")
            return
        try:
            sql = "UPDATE MUSCLE_HIT SET activation_level = %s WHERE muscle = %s AND exercise_type = %s;"
            self.cursor.execute(sql, (activationLevel, self.muscle, self.exerciseType))
            self.connection.commit()
            self.activationLevel = activationLevel
            print(f"Updated record {self.muscle}, {self.activationLevel}, {self.exerciseType} in MUSCLE_HIT.")
        except:
            print(f"Could not update record {self.muscle}, {self.activationLevel}, {self.exerciseType} in MUSCLE_HIT.")

    def delete(self):
        try:
            sql = "FROM MUSCLE_HIT WHERE muscle = %s AND exercise_type = %s;"
            self.cursor.execute(sql, (self.muscle, self.exerciseType))
            self.connection.commit()
            print(f"Deleted record {self.muscle}, {self.exerciseType} from MUSCLE_HIT.")
        except:
            print(f"Could not delete record {self.muscle}, {self.exerciseType} from MUSCLE_HIT.")

    def deleteByExerciseType(self):
        try:
            sql = "FROM MUSCLE_HIT WHERE exercise_type = %s;"
            self.cursor.execute(sql, (self.exerciseType,))
            self.connection.commit()
            print(f"Deleted records from MUSCLE_HIT where exercise_type = {self.exerciseType}.")
        except:
            print(f"Could not delete records from MUSCLE_HIT where exercise_type = {self.exerciseType}.")

    def get(self):
        try:
            sql = "SELECT * FROM MUSCLE_HIT WHERE muscle = %s AND exercise_type = %s;"
            self.cursor.execute(sql, (self.muscle, self.exerciseType))
            return self.cursor.fetchone()
        except:
            print(f"Could not get record {self.muscle}, {self.exerciseType} from MUSCLE_HIT.")
    
    def getByExerciseType(self):
        try:
            sql = "SELECT * FROM MUSCLE_HIT WHERE exercise_type = %s;"
            self.cursor.execute(sql, (self.exerciseType, ))
            return self.cursor.fetchall()
        except:
            print(f"Could not get records with exercise_type {self.exerciseType} from MUSCLE_HIT.")

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
            print(f"Created record {self.exerciseType}, {self.xfr} in EXERCISE_TYPE.")

            for muscleHit in self.muscleHitList:
                MuscleHit(self.connection, self.exerciseType, muscleHit["muscle"], muscleHit["acticationLevel"]).create()
        except:
            print(f"Could not create record {self.exerciseType}, {self.xfr} in EXERCISE_TYPE.")

    def update(self, xfr):
        if not self.exerciseType:
            print("Updating a record in EXERCISE_TYPE required a value for exercise_type.")
            return
        try:
            sql = "UPDATE EXERCISE_TYPE SET xfr = %s WHERE exercise_type = %s;"
            self.cursor.execute(sql, (xfr, self.exerciseType))
            self.connection.execute()
            self.xfr = xfr
            print(f"Updated record {self.xfr}, {self.exerciseType} in EXERCISE_TYPE.")
        except:
            print(f"Could not update record {self.xfr}, {self.exerciseType} in EXERCISE_TYPE.")

    def delete(self):
        try:
            MuscleHit(self.connection, self.exerciseType).deleteByExerciseType()
            sql = "FROM EXERCISE_TYPE WHERE exercise_type = %s;"
            self.cursor.execute(sql, (self.exerciseType,))
            self.connection.commit()
        except:
            print(f"Could not delete record {self.exerciseType} from EXERCISE_TYPE.")

    def get(self):
        try:
            sql = "SELECT * FROM EXERCISE_TYPE WHERE exercise_type = %s;"
            self.cursor.execute(sql, (self.exerciseType,))
            return self.cursor.fetchone()
        except:
            print(f"Could not get record with exercise_type {self.exerciseType} from EXERCISE_TYPE.")


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    
# set (set_id, weight_done, reps, reps_in_reserve, time_taken)

class Set:
    def __init__(self, connection, reps=None, weightDone=None, repsInReserve=None, timeTaken=None, id=None):
        self.connection = connection
        self.cursor = self.connection.cursor()
        self.reps = reps
        self.weightDone = weightDone
        self.repsInReserve = repsInReserve
        self.timeTaken = timeTaken
        self.id = id

    def create(self):
        try:
            sql = "INSERT INTO EXERCISE_SET (weight_done, reps_in_reserve, reps,time_taken) VALUES (%s, %s, %s, %s);"
            self.cursor.execute(sql, (self.weightDone, self.repsInReserve, self.reps, self.timeTaken))
            self.connection.commit()
            print(f"Created record {self.weightDone}, {self.repsInReserve}, {self.reps}, {self.timeTaken} in EXERCISE_SET.")
        except:
            print(f"Could not create record {self.weightDone}, {self.repsInReserve}, {self.reps}, {self.timeTaken} in EXERCISE_SET.")

    def update(self, reps=None, weightDone=None, repsInReserve=None, timeTaken=None):
        if not self.id:
            print("Updating a record in EXERCISE_SET requires set_id.")
            return
        try:
            if reps: self.reps = reps
            if weightDone: self.weightDone = weightDone
            if repsInReserve: self.repsInReserve = repsInReserve
            if timeTaken: self.timeTaken = timeTaken
            sql = """UPDATE EXERCISE_SET SET weight_done = %s, reps_in_reserve = %s, reps = %s, time_taken = %s
            WHERE set_id = %s;"""
            self.cursor.execute(sql, (self.weightDone, self.repsInReserve, self.reps, self.timeTaken, self.id))
            self.connection.commit()
            print(f"Updated record in EXERSICE_SET with set_id {self.id}.")
        except:
            print(f"Could not update record in EXERSICE_SET with set_id {self.id}.")

    def delete(self):
        if not self.id:
            print("Deleting a Set requires ID.")
            return
        try:
            sql = "DELETE FROM SET WHERE set_id = %s;"
            self.cursor.execute(sql, (self.id))
            self.connection.commit()
            print(f"Deleted Set {self.id}.")
        except:
            print(f"Could not delete Set {self.id}.")

    def get(self, id):
        try:
            self.id = id
            sql = "SELECT * FROM EXERCISE_SET WHERE set_id = %s;"
            self.cursor.execute(sql, (self.id,))
            record = self.cursor.fetchone()
            self.weightDone = record[1]
            self.repsInReserve = record[2]
            self.reps = record[3]
            self.timeTaken = record[4]
        except:
            print(f"Could not get Set {id}")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

class SetsDone:
    def __init__(self, connection, exercise, set):
        self.connection = connection
        self.cursor = self.connection.cursor()
        self.exercise = exercise
        self.set = set
    
    def create(self):
        try:
            sql = "INSERT INTO SETS_DONE (exercise, set_id) VALUES (%s, %s);"
            self.cursor.execute(sql, (self.exercise, self.set))
            self.connection.commit()
            print(f"Created record {self.exercise}, {self.set} in SETS_DONE.")
        except:
            print(f"Could not create record {self.exercise}, {self.set} to SETS_DONE.")

    def delete(self):
        try:
            sql = "DELETE FROM SETS_DONE WHERE exercise = %s, set_id = %s;"
            self.cursor.execute(sql, (self.exercise, self.id))
            self.connection.execute()
            print(f"Deleted record {self.exercise}, {self.id} from SETS_DONE.")
        except:
            print(f"Could not delete record {self.exercise}, {self.id} from SETS_DONE.")

    def getByExercise(self):
        try:
            sql = "SELECT * FROM SETS_DONE WHERE exercise = %s;"
            self.cursor.execute(sql, (self.exercise,))
            return self.cursor.fetchall()
        except:
            print(f"Could not get record with exercise {self.exercise} from SETS_DONE.")


# exercise (exercise_type, sets_done(exercise_id, set_id))

# User (fname, lname, dob, weight, lbs_kg, username, user_id)

# exercise (workout_id, exercise_type(exercise_type_name, exercise_type_id, xfr), sets_done(exercise_id, set_id), exercise_id)

# workout_plan (workout_id, user_id, date, start_time, end_time, is_started, list of exercises)