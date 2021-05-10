from .. import db
from werkzeug.security import  generate_password_hash, check_password_hash

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable = False)
    apellido = db.Column(db.String(100), nullable = False)
    telefono = db.Column(db.String(100), nullable = False)
    mail = db.Column(db.String(100), nullable = False)
    password = db.Column(db.String(128), nullable=False)
    rol = db.Column(db.String(10), nullable=False, default="cliente")
    compras = db.relationship('Compra', back_populates='usuario', cascade='all, delete-orphan')
    productos = db.relationship('Producto', back_populates='usuario')

    @property
    def plain_password(self):
        raise AttributeError('Password cant be read')
    @plain_password.setter

    def plain_password(self, password):
        self.password = generate_password_hash(password)

    def validate_pass(self,password):
        return check_password_hash(self.password, password)

    def _repr_(self):
        return '<Usuario: %r %r %r %r >' % (self.nombre, self.apellido, self.telefono, self.mail)
    def to_json(self):
        usuario_json = {
            'id': self.id,
            'nombre': str(self.nombre),
            'apellido': str(self.apellido),
            'telefono': str(self.telefono),
            'mail': str(self.mail)
        }
        return usuario_json
    @staticmethod

    def from_json(usuario_json):
        id = usuario_json.get('id')
        nombre = usuario_json.get('nombre')
        apellido = usuario_json.get('apellido')
        telefono = usuario_json.get('telefono')
        mail = usuario_json.get('mail')
        password = usuario_json.get('password')
        rol = usuario_json.get('rol')

        return Usuario(id=id,
                    nombre=nombre,
                    apellido=apellido,
                    telefono=telefono,
                    mail=mail,
                    plain_password=password,
                    rol=rol
                    )
