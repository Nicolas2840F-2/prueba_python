from flask import Flask, render_template, request, redirect,send_file
from pdf_generator import generar_pdf
from config import Config
from models import db, Trabajo
from io import BytesIO
import os

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

# Crear tablas
with app.app_context():
    db.create_all()

# DASHBOARD
@app.route('/')
def dashboard():
    return render_template('dashboard.html')

# FORMULARIO
@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        imagen = request.files['imagen']
        pdf = request.files['pdf']

        pdf_path = os.path.join(app.config['PDF_FOLDER'], pdf.filename)
        pdf.save(pdf_path)

        trabajo = Trabajo(
            titulo=request.form['titulo'],
            tipo_trabajo=request.form['tipo_trabajo'],
            autor=request.form['autor'],
            universidad=request.form['universidad'],
            palabras_claves=request.form['palabras'],
            resumen=request.form['resumen'],
            curso=request.form['curso'],
            imagen=imagen.read(),
            pdf=pdf.filename,
            ciudad=request.form['ciudad'],
            especialidad=request.form['especialidad']
        )

        db.session.add(trabajo)
        db.session.commit()

        return redirect('/list')

    return render_template('form.html')

# LISTADO
@app.route('/list')
def list_trabajos():
    trabajos = Trabajo.query.all()
    return render_template('list.html', trabajos=trabajos)

# Generar PDF
@app.route('/generar_pdf/<int:id>')
def generar_pdf_route(id):
    trabajo = Trabajo.query.get_or_404(id)
    buffer = BytesIO()
    generar_pdf(trabajo, buffer)
    buffer.seek(0)

    return send_file(buffer, as_attachment=True,download_name=f"{id}.pdf",mimetype='application/pdf')

if __name__ == '__main__':
    app.run(debug=True)

    