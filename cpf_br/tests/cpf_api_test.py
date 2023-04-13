import pytest

from cpf_br.cpf import *


def test_should_create_a_cpf():
    cpf = CPF("12345678909")
    assert isinstance(cpf, CPF)


def test_should_not_create_a_invalid_cpf():
    with pytest.raises(Exception):
        CPF("12345678919")


def test_should_format_cpf():
    cpf = CPF("12345678909")
    assert cpf.with_format() == "123.456.789-09"
