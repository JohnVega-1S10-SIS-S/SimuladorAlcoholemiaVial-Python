import re

def validate_alcohol_level(value):

    try:
        value = float(value)

        if value < 0:
            return False, 'El nivel no puede ser negativo.'

        return True, value

    except ValueError:
        return False, 'Ingrese un número válido.'
    
def validate_user_input(value):

    if value.strip() == "":
        return False, 'El campo esta vacio.'
    
    return True, value

def validate_number(value):

    try:
        value = int(value)
        return True, value
    
    except ValueError:
        return False, 'Porfavor ingrese un número del 1 al 4.'

def is_number(value):

    try:
        value = int(value)
        return True, value
    
    except ValueError:
        return False, 'Solo se permiten numeros.'

def normalize_cedula(cedula):
    """
    Convierte una cédula sin guiones al formato estándar.
    """

    cedula = cedula.strip().upper()

    if re.fullmatch(r"\d{13}[A-Z]", cedula):
        return (
            f"{cedula[:3]}-"
            f"{cedula[3:9]}-"
            f"{cedula[9:]}"
        )

    return cedula

def validate_cedula(cedula):
    """
    Valida una cédula nicaragüense.
    """

    cedula = normalize_cedula(cedula)

    pattern = r"^\d{3}-\d{6}-\d{4}[A-Z]$"

    if re.match(pattern, cedula):
        return True, cedula

    return False, "Formato de cédula inválido."

def normalize_license_plate(plate):
    """
    Normaliza una placa nicaragüense.

    Ejemplos:
    M123456 -> M 123 456
    GR8173  -> GR 8173
    """

    plate = plate.strip().upper().replace(" ", "")

    # M123456 -> M 123 456
    if re.fullmatch(r"[A-Z]\d{6}", plate):
        return (
            f"{plate[:1]} "
            f"{plate[1:4]} "
            f"{plate[4:]}"
        )

    # GR8173 -> GR 8173
    if re.fullmatch(r"[A-Z]{2}\d{4}", plate):
        return (
            f"{plate[:2]} "
            f"{plate[2:]}"
        )

    return plate

def validate_license_plate(plate):
    """
    Valida una placa nicaragüense.
    """

    plate = normalize_license_plate(plate)

    patterns = [
        r"^[A-Z] \d{3} \d{3}$",  # M 123 456
        r"^[A-Z]{2} \d{4}$"      # GR 8173
    ]

    for pattern in patterns:
        if re.fullmatch(pattern, plate):
            return True, plate

    return False, (
        "Formato de placa inválido. "
        "Ejemplos válidos: M123456 o GR8173"
    )
