from app import db
import datetime
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class SalesModel(db.Model):
    __tablename__ = "sales"
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    inv_id = db.Column(db.Integer, db.ForeignKey('inventories.id'))
    created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)