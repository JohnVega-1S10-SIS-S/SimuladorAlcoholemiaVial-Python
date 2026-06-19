import json
import os
import secrets
from datetime import datetime
from tabulate import tabulate

# Guardar en archivo JSON
RUTA_DB = os.path.join('data', 'data.json')

def _load_data():

    if not os.path.exists(RUTA_DB):

        os.makedirs(os.path.dirname(RUTA_DB), exist_ok=True)

        with open(RUTA_DB, 'w', encoding='utf-8') as f:
            json.dump([], f)
        
        return []
    
    try:
        with open(RUTA_DB, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def _insert_data(drivers_data):

    with open(RUTA_DB, 'w', encoding='utf-8') as f:
        json.dump(drivers_data, f, indent=4, ensure_ascii=False)

def inser_data(data):
    try:
        # Cargar datos existentes
        drivers_data = _load_data()

        # Agregar nuevo dato
        drivers_data.append(data)

        # Guardar todo nuevamente
        _insert_data(drivers_data)

        return True, tabulate([data], headers="keys", tablefmt="fancy_grid")
    
    except Exception as e:
        return False, {e}

def gen_id():

    existing_ids = _load_data()

    while True:
        _id = secrets.randbelow(90000) + 10000
        if _id not in existing_ids:
            return _id
        
def driver_exists(driver_id, license_plate):

    drivers_data = _load_data()

    for driver in drivers_data:

        if (
            driver["Cedula del conductor"] == driver_id
            and
            driver["Placa del coche"] == license_plate
        ):
            return True

    return False

def get_driver_by_id(selected_id):

    drivers_data = _load_data()

    for driver in drivers_data:

        if str(driver["ID"]) == str(selected_id):
            return True, driver

    return False, "No se encontró ningún conductor."

def count_offenses(driver_id):

    drivers_data = _load_data()

    count = 0

    for driver in drivers_data:

        if driver["Cedula del conductor"] == driver_id:
            count += 1

    return count + 1

def process_driver(driver_id, plate, alcohol_level):

    if alcohol_level <= 0.5:
        estado = "Embriaguez ligera"
        multa = "C$ 2500"
        sancion = "Retención de licencia por 3 meses"

    elif alcohol_level <= 2:
        estado = "Embriaguez"
        multa = "C$ 3500"
        sancion = "Retención de licencia por 6 meses"

    else:
        estado = "Embriaguez extrema"
        multa = "C$ 5000"
        sancion = "Retención por 1 año o cancelación de licencia"

    data = {
        "ID": gen_id(),
        "Cedula del conductor": driver_id.upper(),
        "Placa del coche": plate.upper(),
        "Nivel de Alcohol": alcohol_level,
        "Estado": estado,
        "Multa": multa,
        "Sanción": sancion,
        "Multas acumuladas": count_offenses(driver_id),
        "Fecha": datetime.now().strftime("%d/%m/%Y %H:%M")
    }

    return data

def load_data():
    """
        Mostrar usuarios registrados en el sistema.
    """
    try:
        # Cargar datos existentes
        drivers_data = _load_data()
    
        if not drivers_data:
            return False, 'A ocurrido un error interno al cargar los datos.'
        return True, drivers_data
    except Exception as e:
        print(f"Error: {e}")
        return False

def search_driver(search_term):

    drivers_data = _load_data()
    results = []

    for driver in drivers_data:

        driver_id = driver["Cedula del conductor"]
        driver_plate = driver["Placa del coche"]

        if (
            search_term.upper() in driver_id.upper()
            or
            search_term.upper() in driver_plate.upper()
        ):
            results.append(driver)

    if results:
        return True, results

    return False, "No se encontró ningún conductor."

def filter_table(filter_term):

    drivers_data = _load_data()
    results = []

    for driver in drivers_data:

        if driver["Estado"] == filter_term:
            results.append(driver)

    if results:
        return True, results

    return False, "No se encontró ningún conductor."

def delete_driver(value):

    drivers_data = _load_data()

    for index, driver in enumerate(drivers_data):

        if (driver["ID"] == value):

            del drivers_data[index]

            _insert_data(drivers_data)

            return True, "Registro eliminado."

    return False, "No se encontró ningún conductor."

def get_statistics():

    drivers_data = _load_data()

    stats = {
        "total": len(drivers_data),
        "ligera": 0,
        "embriaguez": 0,
        "extrema": 0,
        "multas": 0
    }

    for driver in drivers_data:

        estado = driver["Estado"]

        if estado == "Embriaguez ligera":
            stats["ligera"] += 1

        elif estado == "Embriaguez":
            stats["embriaguez"] += 1

        elif estado == "Embriaguez extrema":
            stats["extrema"] += 1

    return stats