from .. import db

class Proveedor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable = False)
    telefono = db.Column(db.String(100), nullable = False)

    def _repr_(self):
        return '<Proveedor: %r %r >' % (self.nombre, self.telefono)
    def to_json(self):
        proveedor_json = {
            'id': self.id,
            'nombre': str(self.nombre),
            'telefono': str(self.telefono)
        }
        return proveedor_json
    @staticmethod

    def from_json(proveedor_json):
        id = proveedor_json.get('id')
        nombre = proveedor_json.get('nombre')
        telefono = proveedor_json.get('telefono')
        return Proveedor(id=id,
                    nombre=nombre,
                    telefono=telefono
                    )
