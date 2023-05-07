from flask import Response, request
from flask_restful import Resource
from database.models.branch import Branch, branchs_schema, branch_schema
from database.db import db


class BranchsAPI(Resource):
    def get(self):
        branchs = Branch.query.filter(Branch.status==True).all()
        return Response(
            branchs_schema.dumps(branchs), mimetype="application/json", status=200
        )

    def post(self):
        body = request.get_json()
        new_branch = branch_schema.load(body)
        db.session.add(new_branch)
        db.session.commit()
        return Response(
            branch_schema.dumps(new_branch), mimetype="application/json", status=200
        )


class BranchAPI(Resource):
    def get(self, id):
        existing_branch = Branch.query.get_or_404(id)
        return Response(
            branch_schema.dumps(existing_branch),
            mimetype="application/json",
            status=200,
        )

    def put(self, id):
        existing_branch = Branch.query.get_or_404(id)
        body = request.get_json()
        data = branch_schema.load(body, session=db.session)
        existing_branch.name = data.name
        existing_branch.address = data.address
        existing_branch.status = data.status
        db.session.commit()
        return Response(
            branch_schema.dumps(existing_branch),
            mimetype="application/json",
            status=200,
        )

    def delete(self, id):
        existing_branch = Branch.query.get_or_404(id)
        existing_branch.status = False
        db.session.commit()
        return Response(
            branch_schema.dumps(existing_branch),
            mimetype="application/json",
            status=200,
        )
