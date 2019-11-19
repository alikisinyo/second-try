from app import db


class InventoryModel(db.Model):
    __tablename__ = 'inventories'
    id = db.Column(db.Integer, primary_key=True)
    inv_name = db.Column(db.String(55), nullable=False)
    inv_type = db.Column(db.String(55), nullable=False)
    bp = db.Column(db.Float, nullable=False)
    sp = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    rp = db.Column(db.Integer, nullable=False)
    sales = db.relationship("SalesModel", backref='Inventories')

    @classmethod
    def update(cls, id, qt):
        record = cls.query.filter_by(id=id).first()

        if record:
            if qt > record.Stock:
                return False
            else:
                record.Stock -= qt
                db.session.commit()
            return True
        else:
            return False

    @classmethod
    def edit(cls, id, name, type, bp, sp, stock, rp):
        record = cls.query.filter_by(id=id).first()

        if record:
            record.Inv_name = name
            record.Inv_type = type
            record.BP = bp
            record.SP = sp
            record.Stock = stock
            record.RP = rp

            return True
        else:
            return False

    @classmethod

    def delete(cls, id, qt):
        record = cls.query.filter_by(id=id).first()

        if record:
            if qt > record.Stock:
                return False
            else:
                record.Stock -= qt
                db.session.commit()
            return True
        else:
            return False

    @classmethod
    def getCountType(cls, name):
        record = cls.query.filter_by(inv_type=name).count()
        return record
