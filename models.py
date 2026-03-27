from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Trabajo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(255))
    tipo_trabajo = db.Column(db.String(50))
    autor = db.Column(db.String(100))
    universidad = db.Column(db.String(100))
    palabras_claves = db.Column(db.Text)
    resumen = db.Column(db.Text)
    curso = db.Column(db.String(50))
    imagen = db.Column(db.LargeBinary)
    pdf = db.Column(db.String(255))
    ciudad = db.Column(db.String(100))
    especialidad = db.Column(db.String(50))