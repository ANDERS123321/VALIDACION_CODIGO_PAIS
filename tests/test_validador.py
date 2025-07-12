from src.validador import validar_telefono

def test_peru_valido():
    assert validar_telefono("+51 987654321")

def test_peru_invalido():
    assert not validar_telefono("+51 123456789")

def test_usa_valido():
    assert validar_telefono("+1 1234567890")

def test_espana_valido():
    assert validar_telefono("+34 612345678")