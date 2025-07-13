import re

def validar_telefono(numero):
    if numero.startswith("+51"):
        # Perú: +51 9XXXXXXXX (9 dígitos, empieza con 9)
        patron = r"^\+51 9\d{8}$"
    elif numero.startswith("+1"):
        # EE.UU. / Canadá: +1 XXXXXXXXXX (10 dígitos)
        patron = r"^\+1 \d{10}$"
    elif numero.startswith("+34"):
        # España: +34 [6-7]XXXXXXXX (9 dígitos)
        patron = r"^\+34 [67]\d{8}$"
    elif numero.startswith("+52"):
        # México: +52 XXXXXXXXXX (10 dígitos)
        patron = r"^\+52 \d{10}$"
    elif numero.startswith("+57"):
        # Colombia: +57 3XXXXXXXXX (10 dígitos, empieza con 3)
        patron = r"^\+57 3\d{9}$"
    elif numero.startswith("+54"):
        # Argentina: +54 9XXXXXXXXXXX (11 dígitos después del 9)
        patron = r"^\+54 9\d{10}$"
    elif numero.startswith("+56"):
        # Chile: +56 9XXXXXXXX (9 dígitos)
        patron = r"^\+56 9\d{8}$"
    elif numero.startswith("+55"):
        # Brasil: +55 DDD9XXXXXXXX (11 dígitos, empieza con 11 o similar)
        patron = r"^\+55 \d{2}9\d{8}$"
    elif numero.startswith("+33"):
        # Francia: +33 [67]XXXXXXXX (9 dígitos, empieza con 6 o 7)
        patron = r"^\+33 [67]\d{8}$"
    elif numero.startswith("+39"):
        # Italia: +39 3XXXXXXXXX (10 dígitos, empieza con 3)
        patron = r"^\+39 3\d{9}$"
    elif numero.startswith("+49"):
        # Alemania: +49 1[5-7]\d{8,9} (10-11 dígitos móviles)
        patron = r"^\+49 1[5-7]\d{8,9}$"
    elif numero.startswith("+598"):
        # Uruguay: +598 9XXXXXXX (8 dígitos, empieza con 9)
        patron = r"^\+598 9\d{7}$"
    elif numero.startswith("+593"):
        # Ecuador: +593 9XXXXXXXX (9 dígitos, empieza con 9)
        patron = r"^\+593 9\d{8}$"
    elif numero.startswith("+591"):
        # Bolivia: +591 [67]XXXXXXX (8 dígitos, empieza con 6 o 7)
        patron = r"^\+591 [67]\d{7}$"
    elif numero.startswith("+595"):
        # Paraguay: +595 9XXXXXXXX (9 dígitos, empieza con 9)
        patron = r"^\+595 9\d{8}$"
    elif numero.startswith("+507"):
        # Panamá: +507 6XXXXXXX (8 dígitos, empieza con 6)
        patron = r"^\+507 6\d{7}$"
    
        return False

    return re.match(patron, numero) is not None