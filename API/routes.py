from sanic.views import HTTPMethodView
from sanic.response import json, text
import json as j
from objects import *

class MuscleRoute(HTTPMethodView):

    def get(self, request, muscle):
        response = Muscle(request.app.config.DB, muscle).get() if muscle else Muscle(request.app.config.DB).getAll()
        return json(response)

    def post(self, request):
        data = j.loads(request.body)
        response = Muscle(request.app.config.DB, data["muscle"]).create()
        return json(response)

    def delete(self, request, muscle):
        response = Muscle(request.app.config.DB, muscle).delete() if muscle else Muscle(request.app.config.DB).deleteAll()
        return json(response)


class UserRoute(HTTPMethodView):
    def post(self, request):
        data = j.loads(request.body)
        response = User(request.app.config.DB, data).create()
        return json(response)

    def get(self, request, username):
        response = User(request.app.config.DB, username).get()
        return json(response)

