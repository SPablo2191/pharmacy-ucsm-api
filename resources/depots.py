from flask import Response, request
from flask_restful import Resource
from database.models.depot import Depot,depots_schema,depot_schema
from database.db import db
from sqlalchemy import and_, or_
class DepotsAPI(Resource):
    def get(self,id):
        depots =  Depot.query.filter(and_(Depot.branch_id==id,Depot.status==True)).all()
        return Response(depots_schema.dumps(depots), mimetype="application/json", status=200)
    def post(self,id):
        body = request.get_json()
        new_depot = depot_schema.load(body)
        new_depot.branch_id = id
        db.session.add(new_depot)
        db.session.commit()
        return Response(depot_schema.dumps(new_depot), mimetype="application/json", status=200)



