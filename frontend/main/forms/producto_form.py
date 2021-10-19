from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_wtf.file import FileField, FileRequired
from wtforms import validators


mess = "Campo obligatorio"


class FormProducto(FlaskForm):
    # imagen = FileField("",
    #         validators = [
    #             FileRequired(message="imagen obligatoria")
    #         ],
    #         )
    nombre = StringField("Nombre",
            [
                validators.Required(message=mess),
                validators.Length(max=100, message="El nombre debe tener menos de 100 caracteres")
            ],
                render_kw={"placeholder": "Nombre del producto"}
            )
    usuarioid = StringField("Usuarioid",
            [
                validators.Required(message=mess),
                validators.Length(max=500, message="El id del usuario debe ser un numero")
            ],
                render_kw={"placeholder": "Id del Usuario"}
            )
    