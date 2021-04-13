from .. import db

class Producto(db.Model):
    productoid = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable = False)
    proveedorid = db.Column(db.Integer, nullable = False)

    def _repr_(self):
        return '<Producto: %r %r >' % (self.nombre, self.proveedorid)
    def to_json(self):
        producto_json = {
            'productoid': self.productoid,
            'nombre': str(self.nombre),
            'proveedorid': self.proveedorid
        }
        return producto_json
    @staticmethod

    def from_json(producto_json):
        productoid = productoid_json.get('id')
        nombre = producto_json.get('nombre')
        proveedorid = producto_json.get('proveedorid')
        return Producto(productoid=productoid,
                    nombre=nombre,
                    proveedorid=proveedorid
                    )
