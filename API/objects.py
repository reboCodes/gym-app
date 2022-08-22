

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
    def __init__(self, connection, exercise, muscle=None, activationLevel=None):
        self.connection = connection
        self.cursor = self.connection.cursor()
        self.exercise = exercise
        self.muscle = muscle
        self.activationLevel = activationLevel

    def create(self):
        try:
            Muscle(self.connection, self.muscle).create()
            sql = "INSERT INTO MUSCLE_HIT (muscle, activation_level, exercise) VALUES (%s, %s, %s);"
            self.cursor.execute(sql, (self.muscle, self.activationLevel, self.exercise))
            self.connection.commit()
            print(f"Created record {self.muscle}, {self.activationLevel}, {self.exercise} in MUSCLE_HIT.")
        except:
            print(f"Could not create record {self.muscle}, {self.activationLevel}, {self.exercise} in MUSCLE_HIT.")
    
    def update(self, activationLevel):
        if not self.muscle or not self.exercise:
            print("Updating a record in MUSCLE_HIT requires values for muscle and exercise.")
            return
        try:
            sql = "UPDATE MUSCLE_HIT SET activation_level = %s WHERE muscle = %s AND exercise = %s;"
            self.cursor.execute(sql, (activationLevel, self.muscle, self.exercise))
            self.connection.commit()
            self.activationLevel = activationLevel
            print(f"Updated record {self.muscle}, {self.activationLevel}, {self.exercise} in MUSCLE_HIT.")
        except:
            print(f"Could not update record {self.muscle}, {self.activationLevel}, {self.exercise} in MUSCLE_HIT.")

    def delete(self):
        try:
            sql = "FROM MUSCLE_HIT WHERE muscle = %s AND exercise = %s;"
            self.cursor.execute(sql, (self.muscle, self.exercise))
            self.connection.commit()
            print(f"Deleted record {self.muscle}, {self.exercise} from MUSCLE_HIT.")
        except:
            print(f"Could not delete record {self.muscle}, {self.exercise} from MUSCLE_HIT.")

    def deleteByExercise(self):
        try:
            sql = "FROM MUSCLE_HIT WHERE exercise = %s;"
            self.cursor.execute(sql, (self.exercise,))
            self.connection.commit()
            print(f"Deleted records from MUSCLE_HIT where exercise = {self.exercise}.")
        except:
            print(f"Could not delete records from MUSCLE_HIT where exercise = {self.exercise}.")

    def get(self):
        try:
            sql = "SELECT * FROM MUSCLE_HIT WHERE muscle = %s AND exercise = %s;"
            self.cursor.execute(sql, (self.muscle, self.exercise))
            return self.cursor.fetchone()
        except:
            print(f"Could not get record {self.muscle}, {self.exercise} from MUSCLE_HIT.")
    
    def getByExercise(self):
        try:
            sql = "SELECT * FROM MUSCLE_HIT WHERE exercise = %s;"
            self.cursor.execute(sql, (self.exercise, ))
            return self.cursor.fetchall()
        except:
            print(f"Could not get records with exercise {self.exercise} from MUSCLE_HIT.")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

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
    def __init__(self, connection, exercise, set=None):
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
        if not self.set:
            print("Deleting a record in SETS_DONE requires a set_id.")
            return
        try:
            sql = "DELETE FROM SETS_DONE WHERE exercise = %s, set_id = %s;"
            self.cursor.execute(sql, (self.exercise, self.id))
            self.connection.commit()
            print(f"Deleted record {self.exercise}, {self.id} from SETS_DONE.")
        except:
            print(f"Could not delete record {self.exercise}, {self.id} from SETS_DONE.")

    def deleteByExercise(self):
        try:
            sql = "DELETE FROM SETS_DONE WHERE exercise = %s;"
            self.cursor.execute(sql, (self.exercise,))
            self.connection.commit()
            print(f"Deleted all records with exercise {self.exercise} from SETS_DONE.")
        except:
            print(f"Could not delete all records with exercise {self.exercise} from SETS_DONE.")

    def getByExercise(self):
        try:
            sql = "SELECT * FROM SETS_DONE WHERE exercise = %s;"
            self.cursor.execute(sql, (self.exercise,))
            return self.cursor.fetchall()
        except:
            print(f"Could not get record with exercise {self.exercise} from SETS_DONE.")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

class Exercise:
    def __init__(self, connection, workout_id, exercise, xfr=None, muscleHitList=None, setList=None):
        self.connection = connection
        self.cursor = self.connection.cursor()
        self.workoutID = workout_id
        self.exercise = exercise
        self.xfr = xfr
        self.muscleHitList = muscleHitList
        self.setList = setList

    def create(self):
        try:
            sql = "INSERT INTO EXERCISE (workout_id, exercise, xfr) VALUES (%s, %s, %s);"
            self.cursor.execute(sql, (self.workoutID, self.exercise, self.xfr))
            self.connection.commit()
            print(f"Created record {self.workoutID}, {self.exercise}, {self.xfr} in EXERCISE.")

            for muscleHit in self.muscleHitList:
                MuscleHit(self.connection, self.exercise, muscleHit["muscle"], muscleHit["acticationLevel"]).create()

            for set in self.setList:
                Set(self.connection, set["reps"], set["weight_done"], set["reps_in_reserve"], set["time_taken"]).create()
        except:
            print(f"Could not create record {self.exercise}, {self.xfr} in EXERCISE.")

    def update(self, xfr):
        if not self.exercise:
            print("Updating a record in EXERCISE required a value for exercise.")
            return
        try:
            sql = "UPDATE EXERCISE SET xfr = %s WHERE exercise = %s and workout_id = %s;"
            self.cursor.execute(sql, (xfr, self.exercise, self.workoutID))
            self.connection.execute()
            self.xfr = xfr
            print(f"Updated record {self.xfr}, {self.exercise}, {self.workoutID} in EXERCISE.")
        except:
            print(f"Could not update record {self.xfr}, {self.exercise}, {self.workoutID} in EXERCISE.")

    def delete(self):
        try:
            MuscleHit(self.connection, self.exercise).deleteByExercise()
            SetsDone(self.connection, self.exercise).deleteByExercise()
            sql = "FROM EXERCISE WHERE exercise = %s;"
            self.cursor.execute(sql, (self.exercise,))
            self.connection.commit()
        except:
            print(f"Could not delete record {self.exercise} from EXERCISE.")

    def get(self):
        try:
            sql = "SELECT * FROM EXERCISE WHERE exercise = %s AND workout_id = %s;"
            self.cursor.execute(sql, (self.exercise, self.workoutID))
            return self.cursor.fetchone()
        except:
            print(f"Could not get record with exercise {self.exercise}, {self.workoutID} from EXERCISE.")
    
    def getMuscleHitList(self):
        return MuscleHit(self.connection, self.exercise).getByExercise()

    def getSetsDone(self):
        return SetsDone(self.connection, self.exercise).getByExercise()


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 


# User (fname, lname, dob, weight, lbs_kg, username, user_id)

# exercise (workout_id, exercise_type(exercise_type_name, exercise_type_id, xfr), sets_done(exercise_id, set_id), exercise_id)

# workout_plan (workout_id, user_id, date, start_time, end_time, is_started, list of exercises)