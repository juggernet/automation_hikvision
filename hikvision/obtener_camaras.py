import xml.etree.ElementTree as ET

from hikvision.conexion import peticion_get


def obtener_camaras():

    endpoint = "/ISAPI/ContentMgmt/InputProxy/channels"

    respuesta = peticion_get(endpoint)

    root = ET.fromstring(respuesta.text)

    ns = {
        'hik': 'http://www.hikvision.com/ver20/XMLSchema'
    }

    canales = root.findall(
        'hik:InputProxyChannel',
        ns
    )

    lista_camaras = []

    for canal in canales:

        id_canal = canal.find('hik:id', ns)

        nombre = canal.find('hik:name', ns)

        source = canal.find(
            'hik:sourceInputPortDescriptor',
            ns
        )

        ip = source.find('hik:ipAddress', ns)

        modelo = source.find('hik:model', ns)

        usuario = source.find('hik:userName', ns)

        camara = {

            "canal": f"D{id_canal.text}",

            "nombre": nombre.text,

            "ip": ip.text,

            "modelo": modelo.text,

            "usuario": usuario.text
        }

        lista_camaras.append(camara)

    return lista_camaras