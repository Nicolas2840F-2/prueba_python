from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
import os
from io import BytesIO
from reportlab.platypus import Image

def generar_pdf(trabajo, ruta_pdf):
    doc = SimpleDocTemplate(ruta_pdf)
    styles = getSampleStyleSheet()

    contenido = []

    contenido.append(Paragraph("<b>REPORTE DE TRABAJO</b>", styles['Title']))
    contenido.append(Spacer(1, 20))

    # Título
    contenido.append(Paragraph(f"<b>Título:</b> {trabajo.titulo}", styles['Normal']))
    contenido.append(Spacer(1, 10))

    contenido.append(Paragraph(f"<b>Tipo:</b> {trabajo.tipo_trabajo}", styles['Normal']))
    contenido.append(Spacer(1, 10))

    contenido.append(Paragraph(f"<b>Autor:</b> {trabajo.autor}", styles['Normal']))
    contenido.append(Spacer(1, 10))

    contenido.append(Paragraph(f"<b>Curso:</b> {trabajo.curso}", styles['Normal']))
    contenido.append(Spacer(1, 10))

    contenido.append(Paragraph(f"<b>Especialidad:</b> {trabajo.especialidad}", styles['Normal']))
    contenido.append(Spacer(1, 10))

    contenido.append(Paragraph(f"<b>Ciudad:</b> {trabajo.ciudad}", styles['Normal']))
    contenido.append(Spacer(1, 10))

    contenido.append(Paragraph(f"<b>Resumen:</b> {trabajo.resumen}", styles['Normal']))
    contenido.append(Spacer(1, 20))

    # Imagen (si quieres intentar mostrarla)
    if trabajo.imagen:
        try:
            imagen_stream = BytesIO(trabajo.imagen)
            img = Image(imagen_stream, width=200, height=150)
            contenido.append(img)
        except Exception as e:
            contenido.append(Paragraph("Error cargando imagen", styles['Normal']))

    doc.build(contenido)