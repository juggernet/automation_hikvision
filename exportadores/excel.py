from openpyxl import Workbook


def exportar_excel(camaras):

    wb = Workbook()

    ws = wb.active

    ws.title = "Camaras"

    encabezados = [
        "Canal",
        "Nombre",
        "IP",
        "Modelo"
    ]

    ws.append(encabezados)

    for camara in camaras:

        ws.append([
            camara["canal"],
            camara["nombre"],
            camara["ip"],
            camara["modelo"]
        ])

    wb.save(
        "reportes/inventario_camaras.xlsx"
    )

    print("Excel generado correctamente")