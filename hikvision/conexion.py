import requests

from requests.auth import HTTPDigestAuth

from config.config import (
    IP_NVR,
    USUARIO,
    PASSWORD
)

def peticion_get(endpoint):

    url = f"http://{IP_NVR}{endpoint}"

    respuesta = requests.get(
        url,
        auth=HTTPDigestAuth(
            USUARIO,
            PASSWORD
        )
    )

    return respuesta