from hikvision.obtener_camaras import (
    obtener_camaras
)

from hikvision.cambiar_nombre import (
    obtener_nombre_actual,
    cambiar_nombre
)


def main():

    camaras = obtener_camaras()

    for camara in camaras:

        canal = camara["canal"]

        ip = camara["ip"]

        nombre_nvr = camara["nombre_nvr"]

        nombre_actual = obtener_nombre_actual(
            ip
        )

        print("\n====================")

        print(f"Canal    : {canal}")

        print(f"IP        : {ip}")

        print(f"Actual  : {nombre_actual}")

        print(f"Sugerido : {nombre_nvr}")

        if nombre_actual == nombre_nvr:

            print("✔ Nombre correcto")

            continue

        opcion = input(
            "\n[s] sugerido | [m] manual | [n] omitir | [q] salir: "
        ).lower()

        if opcion == "s":

            nuevo_nombre = nombre_nvr

        elif opcion == "m":

            nuevo_nombre = input(
                "Ingrese nuevo nombre: "
            )

        elif opcion == "n":

            print("Omitido")

            continue

        elif opcion == "q":

            print("Finalizando programa")

            break

        else:

            print("Opción inválida")

            continue

        status = cambiar_nombre(
            ip,
            nuevo_nombre
        )

        if status == 200:

            print(" Nombre actualizado")

        else:

            print(f" Error: {status}")


if __name__ == "__main__":
    main()