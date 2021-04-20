from .. import db

class Compra(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fechacompra = db.Column(db.DateTime, nullable = False)
    retirado = db.Column(db.Boolean, nullable = False)

    def _repr_(self):
        return '<Compra: %r %r >' % (self.fechacompra, self.retirado)
    def to_json(self):
        compra_json = {
            'id': self.id,
            'fechacompra': self.fechacompra,
            'retirado': str(self.retirado)
        }
        return compra_json
    @staticmethod

    def from_json(compra_json):
        id = compra_json.get('id')
        fechacompra = compra_json.get('fechacompra')
        retirado = compra_json.get('retirado')
        return Compra(id=id,
                    fechacompra=fechacompra,
                    retirado=retirado
                    )
