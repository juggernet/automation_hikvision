from hikvision.obtener_camaras import (
    obtener_camaras
)

from exportadores.excel import (
    exportar_excel
)


def main():

    print("Obteniendo cámaras...\n")

    camaras = obtener_camaras()

    print(f"Total cámaras: {len(camaras)}")

    exportar_excel(camaras)

    print("\nProceso finalizado")


if __name__ == "__main__":
    main()