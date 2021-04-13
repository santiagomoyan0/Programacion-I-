from .. import db

class Compra(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    clienteid = db.Column(db.Integer, nullable = False)
    bolsonid = db.Column(db.Integer, nullable = False)
    fechacompra = db.Column(db.String(100), nullable = False)
    retirado = db.Column(db.Boolean, nullable = False)

    def _repr_(self):
        return '<Compra: %r %r >' % (self.clienteid, self.bolsonid, self.fechacompra, self.retirado)
    def to_json(self):
        compra_json = {
            'id': self.id,
            'clienteid': self.clienteid,
            'bolsonid': self.bolsonid,
            'fechacompra': self.fechacompra,
            'retirado': self.retirado
        }
        return compra_json
    @staticmethod

    def from_json(compra_json):
        id = compra_json.get('id')
        clienteid = compra_json.get('clienteid')
        bolsonid = compra_json.get('bolsonid')
        fechacompra = compra_json.get('fechacompra')
        retirado = compra_json.get('retirado')
        return Compra(id=id,
                    clienteid=clienteid,
                    bolsonid=bolsonid,
                    fechacompra=fechacompra
                    retirado=retirado
                    )
