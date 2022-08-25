from sanic import Sanic
from databaseConnection import DatabaseConnection
from routes import *


if __name__ == '__main__':
    db = DatabaseConnection()
    app = Sanic("gym-api")
    app.config.DB = db.connection()


    app.add_route(MuscleRoute.as_view(), "/muscle")
    app.add_route(MuscleRoute.as_view(), "/muscle/<muscle>")

    app.add_route(UserRoute.as_view(), "/user")
    app.add_route(UserRoute.as_view(), "/user/<username>")


    app.run(dev=True)



# muscleHitList = [{"muscle": "Chest", "activation_level": 8}, {"muscle": "Tricep", "activation_level": 5}]
# setList = [{"weight_done": 225, "reps": 6, "reps_in_reserve": None, "time_taken": None}, 
#             {"weight_done": 225, "reps": 6, "reps_in_reserve": None, "time_taken": None}]


# ExerciseType(db.connection(), "Bench Press", 8, muscleHitList).create()

# benchPress = Exercise(db.connection(), 1, "Bench Press", "Bench Press", setList).create()
