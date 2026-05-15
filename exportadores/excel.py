from openpyxl import Workbook

import os


def exportar_excel(camaras):

    os.makedirs(
        "reportes",
        exist_ok=True
    )

    wb = Workbook()

    ws = wb.active

    ws.title = "Camaras"

    encabezados = [

        "Canal",

        "IP",

        "Nombre NVR",

        "Nombre Camara",

        "Modelo",

        "Serie"
    ]

    ws.append(encabezados)

    for camara in camaras:

        ws.append([

            camara["canal"],

            camara["ip"],

            camara["nombre_nvr"],

            camara["nombre_camara"],

            camara["modelo"],

            camara["serie"]
        ])

    ruta = (
        "reportes/"
        "inventario_camaras.xlsx"
    )

    wb.save(ruta)

    print(
        f"\nExcel generado:"
        f"\n{ruta}"
    )