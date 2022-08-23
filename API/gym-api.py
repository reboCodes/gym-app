from sanic import Sanic
from sanic.response import text, json
from databaseConnection import DatabaseConnection
from objects import *


db = DatabaseConnection()
app = Sanic("gym-api")

muscleHitList = [{"muscle": "Chest", "activation_level": 8}, {"muscle": "Tricep", "activation_level": 5}]
setList = [{"weight_done": 225, "reps": 6, "reps_in_reserve": None, "time_taken": None}, 
            {"weight_done": 225, "reps": 6, "reps_in_reserve": None, "time_taken": None}]


@app.get("/muscle/<tag>")
async def tag_handler(request, tag):
    return json(Muscle(db.connection(),tag).get())


# ExerciseType(db.connection(), "Bench Press", 8, muscleHitList).create()

# benchPress = Exercise(db.connection(), 1, "Bench Press", "Bench Press", setList).create()


if __name__ == '__main__':
    app.run(dev=True)
    # print(Muscle(db.connection(),"Tricep").get())
