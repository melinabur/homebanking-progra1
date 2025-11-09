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
