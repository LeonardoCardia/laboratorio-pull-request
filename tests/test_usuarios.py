from usuarios import validar_email


def test_valido():
    assert validar_email("ana@exemplo.com") is True


def test_sem_arroba():
    assert validar_email("ana.exemplo.com") is False