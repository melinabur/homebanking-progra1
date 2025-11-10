import json
from datetime import datetime
import os

def registrar_evento(usuario, tipo_evento, detalle):
    """
    Registra un evento en el historial personal del usuario.
    Cada usuario tiene su propio archivo JSON (por DNI).
    """
    dni = usuario["dni"]
    archivo_historial = f"data/historial_{dni}.json"

    # Creamos el diccionario del evento
    evento = {
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "evento": tipo_evento,
        "detalle": detalle
    }

    # Si el archivo ya existe, lo abrimos para leer los datos actuales
    if os.path.exists(archivo_historial):
        with open(archivo_historial, "r", encoding="utf-8") as f:
            try:
                historial = json.load(f)
            except json.JSONDecodeError:
                historial = []
    else:
        historial = []

    # Agregamos el nuevo evento
    historial.append(evento)

    # Guardamos el historial actualizado (crea o sobrescribe el archivo)
    with open(archivo_historial, "w", encoding="utf-8") as f:
        json.dump(historial, f, indent=4, ensure_ascii=False)


def exportar_historial_txt(usuario):
    """
    Exporta el historial personal del usuario a un archivo TXT.
    """
    dni = usuario["dni"]
    nombre = usuario["nombre"]
    apellido = usuario["apellido"]
    archivo_json = f"data/historial_{dni}.json"
    archivo_txt = f"data/historial_{dni}.txt"

    # Verificar si existe el archivo JSON con los movimientos
    if not os.path.exists(archivo_json):
        print("No hay historial para exportar todavía.")
        return

    # Leer los movimientos desde el archivo JSON
    with open(archivo_json, "r", encoding="utf-8") as f:
        try:
            historial = json.load(f)
        except json.JSONDecodeError:
            print("El historial está vacío o dañado.")
            return

    # Crear el archivo TXT y escribir los datos
    with open(archivo_txt, "w", encoding="utf-8") as f:
        f.write(f"Historial de movimientos del usuario {nombre} {apellido}\n")
        f.write("-" * 60 + "\n")

        for evento in historial:
            f.write(f"{evento['fecha']} | {evento['evento']} → {evento['detalle']}\n")

    print(f"✅ Historial exportado correctamente a {archivo_txt}")
