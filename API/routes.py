from urllib import response
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
        response = Muscle(request.app.config.DB_CONNECTION, data["muscle"]).create()
        return json(response)

    def delete(self, request, muscle):
        response = Muscle(request.app.config.DB_CONNECTION, muscle).delete()
        return text(response)

class MusclesRoute(HTTPMethodView):

    def get(self, request):
        response = Muscle(request.app.config.DB_CONNECTION).getAll()
        return json(response)

    def delete(self, request):
        response = Muscle(request.app.config.DB_CONNECTION).deleteAll()
        return text(response)
