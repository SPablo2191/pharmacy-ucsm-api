from datetime import datetime
from database.db import db
from database.db import ma


class Branch(db.Model):
    __tablename__ = "Branch"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    status = db.Column(db.Boolean, default=True, nullable=False)
    registerDate = db.Column(db.DateTime, default=datetime.utcnow())


class BranchSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Branch
        load_instance = True
        sqla_session = db.session
        fields = (
            "id",
            "name",
            "address",
            "status",
            "registerDate",
        )


branch_schema = BranchSchema()
branchs_schema = BranchSchema(many=True)
