import requests
import urllib3

import xml.etree.ElementTree as ET

from requests.auth import HTTPDigestAuth

from config.config import (
    USUARIO_CAMARA,
    PASSWORD_CAMARA
)

# Desactivar warnings HTTPS
urllib3.disable_warnings(
    urllib3.exceptions.InsecureRequestWarning
)


def obtener_nombre_actual(ip):

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

        print(f"\nGET {ip}: {respuesta.status_code}")

        if respuesta.status_code != 200:

            print(respuesta.text)

            return "SIN_NOMBRE"

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

    except Exception as e:

        print(f"ERROR GET {ip}: {e}")

        return "ERROR"


def cambiar_nombre(ip, nuevo_nombre):

    url = f"https://{ip}/ISAPI/System/deviceInfo"

    xml_data = f"""
    <DeviceInfo xmlns="http://www.hikvision.com/ver20/XMLSchema">
        <deviceName>{nuevo_nombre}</deviceName>
    </DeviceInfo>
    """

    headers = {
        "Content-Type": "application/xml"
    }

    try:

        respuesta = requests.put(
            url,
            data=xml_data,
            headers=headers,
            auth=HTTPDigestAuth(
                USUARIO_CAMARA,
                PASSWORD_CAMARA
            ),
            verify=False,
            timeout=10
        )

        print(f"\nPUT {ip}: {respuesta.status_code}")

        print(respuesta.text)

        return respuesta.status_code

    except Exception as e:

        print(f"ERROR PUT {ip}: {e}")

        return 500