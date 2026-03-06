import sqlite3
from flask import Flask, render_template, request, redirect, url_for
import os
import sqlite3
import uuid
def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS piezas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            imagen TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

init_db()


app = Flask(__name__)

UPLOAD_FOLDER = "static/images/piezas"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Extensiones permitidas
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
@app.route("/agregar", methods=["GET", "POST"])
def agregar():
    if request.method == "POST":
        nombre = request.form["nombre"]
        descripcion = request.form["descripcion"]
        imagen = request.files["imagen"]

        if imagen and allowed_file(imagen.filename):

            # Generar nombre único
            extension = imagen.filename.rsplit(".", 1)[1].lower()
            nombre_unico = f"{uuid.uuid4()}.{extension}"
            ruta = os.path.join(app.config["UPLOAD_FOLDER"], nombre_unico)

            imagen.save(ruta)

            conn = sqlite3.connect("database.db")
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO piezas (nombre, descripcion, imagen) VALUES (?, ?, ?)",
                (nombre, descripcion, ruta)
            )
            conn.commit()
            conn.close()

            return redirect(url_for("index"))

    return render_template("agregar.html")
@app.route("/")
def index():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM piezas")
    piezas = cursor.fetchall()
    conn.close()

    return render_template("index.html", piezas=piezas)