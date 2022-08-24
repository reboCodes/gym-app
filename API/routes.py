from sanic.views import HTTPMethodView
from sanic.response import json, text
import json as j
from objects import *

class MuscleRoute(HTTPMethodView):

    def get(self, request, muscle):
        return json(Muscle(request.app.config.DB_CONNECTION, muscle).get())

    async def post(self, request, muscle):
        data = j.loads(request.body)
        asdf = data["muscle"]
        Muscle(request.app.config.DB_CONNECTION, data["muscle"]).create()
        return text(f"Muscle: {asdf} has been created.")

    def delete(self, request, muscle):
        Muscle(request.app.config.DB_CONNECTION, muscle).delete()
        return text(f"Muscle: {muscle} has been deleted.")

