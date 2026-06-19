from datetime import datetime
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)
from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime

PDF_FOLDER = Path("pdf")

def get_available_filename(base_name):
    """
    Genera nombres como:
    tabla_completa.pdf
    tabla_completa_1.pdf
    tabla_completa_2.pdf
    """

    PDF_FOLDER.mkdir(exist_ok=True)

    file_path = PDF_FOLDER / f"{base_name}.pdf"

    if not file_path.exists():
        return str(file_path)

    counter = 1

    while True:

        file_path = PDF_FOLDER / f"{base_name}_{counter}.pdf"

        if not file_path.exists():
            return str(file_path)

        counter += 1

def export_driver_pdf(driver):

    pdf_path = get_available_filename(
        f"conductor_{driver['ID']}"
    )

    pdf = SimpleDocTemplate(
        pdf_path
    )

    styles = getSampleStyleSheet()

    elements = []

    elements.append(
        Paragraph(
            "Reporte de Conductor",
            styles["Title"]
        )
    )

    elements.append(Spacer(1, 20))

    for key, value in driver.items():

        elements.append(
            Paragraph(
                f"<b>{key}:</b> {value}",
                styles["BodyText"]
            )
        )

        elements.append(
            Spacer(1, 5)
        )

    pdf.build(elements)

    return True

def export_statistics_pdf(stats):

    pdf_path = get_available_filename(
        "estadisticas_alcoholemia"
    )

    pdf = SimpleDocTemplate(
        pdf_path
    )

    styles = getSampleStyleSheet()

    elements = []

    elements.append(
        Paragraph(
            "Reporte Estadístico",
            styles["Title"]
        )
    )

    elements.append(Spacer(1, 20))

    elements.append(
        Paragraph(
            f"Fecha de generación: {datetime.now().strftime('%d/%m/%Y %H:%M')}",
            styles["BodyText"]
        )
    )

    elements.append(Spacer(1, 15))

    elements.append(
        Paragraph(
            f"Total de registros: {stats['total']}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"Embriaguez ligera: {stats['ligera']}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"Embriaguez: {stats['embriaguez']}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"Embriaguez extrema: {stats['extrema']}",
            styles["BodyText"]
        )
    )

    pdf.build(elements)

    return True

def export_table_pdf(drivers_data):

    pdf_path = get_available_filename(
        "tabla_completa"
    )

    pdf = SimpleDocTemplate(
        pdf_path
    )

    styles = getSampleStyleSheet()

    elements = []

    elements.append(
        Paragraph(
            "Reporte General de Conductores",
            styles["Title"]
        )
    )

    elements.append(Spacer(1, 20))

    elements.append(
        Paragraph(
            f"Fecha: {datetime.now().strftime('%d/%m/%Y %H:%M')}",
            styles["BodyText"]
        )
    )

    elements.append(Spacer(1, 15))
    
    # ---------------------------------------------------
    # headers = list(drivers_data[0].keys())

    # table_data = [headers]

    # for driver in drivers_data:

    #     row = []

    #     for value in driver.values():
    #         row.append(str(value))

    #     table_data.append(row)

    #     table = Table(table_data)


    #     table.setStyle(
    #         TableStyle([
    #             ('GRID', (0,0), (-1,-1), 1, colors.black),
    #             ('BACKGROUND', (0,0), (-1,0), colors.lightgrey),
    #             ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    #         ])
    #     )

    #     elements.append(table)

    #     pdf.build(elements)
    # ---------------------------------------------------

    table_data = [[
        "ID",
        "Fecha",
        "Conductor",
        "Estado",
        "Multas"
    ]]

    for driver in drivers_data:

        row = [
            driver["ID"],
            driver["Fecha"],
            driver["Cedula del conductor"],
            driver["Estado"],
            driver["Multas acumuladas"]
        ]

        table_data.append(row)

        table = Table(table_data)

        table.setStyle(
            TableStyle([
                ('GRID', (0,0), (-1,-1), 1, colors.black),
                ('BACKGROUND', (0,0), (-1,0), colors.lightgrey),
                ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
            ])
        )

        elements.append(table)

        pdf.build(elements)

    return True

