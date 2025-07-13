from src.validador import validar_telefono

def test_peru_valido():
    assert validar_telefono("+51 987654321")

def test_peru_invalido():
    assert not validar_telefono("+51 123456789")

def test_usa_valido():
    assert validar_telefono("+1 1234567890")

def test_espana_valido():
    assert validar_telefono("+34 612345678")

def test_mexico_valido():
    assert validar_telefono("+52 5512345678")

def test_colombia_valido():
    assert validar_telefono("+57 3123456789")

def test_argentina_valido():
    assert validar_telefono("+54 91123456789")

def test_chile_valido():
    assert validar_telefono("+56 912345678")

def test_brasil_valido():
    assert validar_telefono("+55 11912345678")

def test_francia_valido():
    assert validar_telefono("+33 612345678")

def test_italia_valido():
    assert validar_telefono("+39 3123456789")

def test_alemania_valido():
    assert validar_telefono("+49 15123456789")

def test_canada_valido():
    assert validar_telefono("+1 4161234567")

def test_uruguay_valido():
    assert validar_telefono("+598 91234567")

def test_ecuador_valido():
    assert validar_telefono("+593 991234567")

def test_bolivia_valido():
    assert validar_telefono("+591 71234567")

def test_paraguay_valido():
    assert validar_telefono("+595 961234567")

def test_panama_valido():
    assert validar_telefono("+507 61234567")

def test_venezuela_valido():
    assert validar_telefono("+58 4121234567")

def test_japon_valido():
    assert validar_telefono("+81 9012345678")
