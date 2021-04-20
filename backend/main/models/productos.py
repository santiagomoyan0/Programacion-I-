from .. import db

class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable = False)

    def _repr_(self):
        return '<Producto: %r >' % self.nombre
    def to_json(self):
        producto_json = {
            'id': self.id,
            'nombre': str(self.nombre)

        }
        return producto_json
    @staticmethod

    def from_json(producto_json):
        id = producto_json.get('id')
        nombre = producto_json.get('nombre')
        return Producto(id=id,
                    nombre=nombre
                    )
