from datetime import datetime

from sweater import db


class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR(length=50), nullable=False)
    description = db.Column(db.Text, default="No description")
    registration_date = db.Column(db.DateTime, default=datetime.utcnow())
    product_id = db.Column(db.Integer, nullable=False)

    def __init__(self, name, product_id, description):
        self.name = name
        self.product_id = product_id
        self.description = description

    def __repr__(self):
        return '<Company %>' % self.id
