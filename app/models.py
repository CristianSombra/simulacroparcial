from . import db

class Persona(db.Model):
    __tablename__ = 'personas'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    foto_url = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return f"<Persona {self.nombre} ({self.email})>"
