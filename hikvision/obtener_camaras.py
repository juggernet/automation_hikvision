import requests

import xml.etree.ElementTree as ET

from requests.auth import HTTPDigestAuth


import urllib3

urllib3.disable_warnings(
    urllib3.exceptions.InsecureRequestWarning
)

from config.config import (
    IP_NVR,
    USUARIO_NVR,
    PASSWORD_NVR,
    USUARIO_CAMARA,
    PASSWORD_CAMARA
)


def obtener_nombre_camara(ip):

    url = f"https://{ip}/ISAPI/System/deviceInfo"

    try:

        respuesta = requests.get(
            url,
            auth=HTTPDigestAuth(
                USUARIO_CAMARA,
                PASSWORD_CAMARA
            ),
            verify=False,
            timeout=10
        )

        if respuesta.status_code != 200:

            return "SIN_ACCESO"

        root = ET.fromstring(
            respuesta.text
        )

        namespace = {
            "hik": "http://www.hikvision.com/ver20/XMLSchema"
        }

        nombre = root.find(
            "hik:deviceName",
            namespace
        )

        if nombre is None:

            return "SIN_NOMBRE"

        return nombre.text

    except:

        return "ERROR"


def obtener_camaras():

    url = (
        f"http://{IP_NVR}"
        "/ISAPI/ContentMgmt/InputProxy/channels"
    )

    respuesta = requests.get(
        url,
        auth=HTTPDigestAuth(
            USUARIO_NVR,
            PASSWORD_NVR
        )
    )

    root = ET.fromstring(
        respuesta.text
    )

    namespace = {
        "hik": "http://www.hikvision.com/ver20/XMLSchema"
    }

    camaras = []

    canales = root.findall(
        "hik:InputProxyChannel",
        namespace
    )

    for canal in canales:

        id_canal = canal.find(
            "hik:id",
            namespace
        ).text

        nombre = canal.find(
            "hik:name",
            namespace
        ).text

        ip = canal.find(
            ".//hik:ipAddress",
            namespace
        ).text

        modelo = canal.find(
            ".//hik:model",
            namespace
        ).text

        serie = canal.find(
            ".//hik:serialNumber",
            namespace
        ).text

        nombre_camara = obtener_nombre_camara(
            ip
        )

        camaras.append({

            "canal": f"D{id_canal}",

            "nombre_nvr": nombre,

            "nombre_camara": nombre_camara,

            "ip": ip,

            "modelo": modelo,

            "serie": serie
        })

    return camaras