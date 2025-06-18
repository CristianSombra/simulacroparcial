from flask import Blueprint, render_template, request, redirect, url_for, flash
from . import db
from .models import Persona
import cloudinary
import cloudinary.uploader
import os

# Configurar Cloudinary desde variables de entorno
cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET"),
    secure=True
)

bp = Blueprint('main', __name__)

@bp.route("/")
def index():
    personas = Persona.query.all()
    return render_template("index.html", personas=personas)

@bp.route("/create")
def create():
    return render_template("create.html")

@bp.route("/store", methods=["POST"])
def store():
    nombre = request.form["nombre"]
    edad = request.form["edad"]
    email = request.form["email"]
    foto = request.files["foto"]

    # Subir imagen a Cloudinary y obtener URL
    resultado = cloudinary.uploader.upload(foto)
    foto_url = resultado.get("secure_url")

    nueva_persona = Persona(
        nombre=nombre,
        edad=int(edad),
        email=email,
        foto_url=foto_url
    )
    db.session.add(nueva_persona)
    db.session.commit()

    flash("Persona creada exitosamente")
    return redirect(url_for("main.index"))

@bp.route("/edit/<int:id>")
def edit(id):
    persona = Persona.query.get_or_404(id)
    return render_template("edit.html", persona=persona)

@bp.route("/update/<int:id>", methods=["POST"])
def update(id):
    persona = Persona.query.get_or_404(id)

    persona.nombre = request.form["nombre"]
    persona.edad = int(request.form["edad"])
    persona.email = request.form["email"]

    # Si se sube una nueva imagen, la reemplaza
    if "foto" in request.files and request.files["foto"].filename != "":
        resultado = cloudinary.uploader.upload(request.files["foto"])
        persona.foto_url = resultado.get("secure_url")

    db.session.commit()
    flash("Persona actualizada correctamente")
    return redirect(url_for("main.index"))


@bp.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    persona = Persona.query.get_or_404(id)
    db.session.delete(persona)
    db.session.commit()
    flash("Persona eliminada")
    return redirect(url_for("main.index"))

@bp.route("/acerca/<int:id>")
def acerca(id):
    persona = Persona.query.get_or_404(id)
    return render_template("about.html", persona=persona)
