from cpf_br.cpf import *


def test_should_create_a_cpf() -> None:
    cpf = CPF("12345678909")
    assert isinstance(cpf, CPF)


def test_should_create_a_cpf_1() -> None:
    assert calculate_verification_digit('12345678909', 10, 9) == 0
    assert calculate_verification_digit('12345678909', 11, 10) == 9
