import re

def validar_telefono(numero):
    if numero.startswith("+51"):
        patron = r"^\+51 9\d{8}$"
        return re.match(patron, numero) is not None
    elif numero.startswith("+1"):
        patron = r"^\+1 \d{10}$"
        return re.match(patron, numero) is not None
    elif numero.startswith("+34"):
        patron = r"^\+34 \d{9}$"
        return re.match(patron, numero) is not None
    else:
        return False
