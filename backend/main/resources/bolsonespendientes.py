from flask_restful import Resource
from flask import request
BOLSONESPENDIENTES = {


}

class BolsonesPendientes(Resource):

    def get(self, id):

        if int(id) in BolsonesPendientes:

            return BolsonesPendientes[int(id)]

        return '', 404
class BolsonPendiente(Resource):
    def get(self, id):

        if int(id) in BolsonPendiente:

            return BolsonPendiente[int(id)]

        return '', 404
