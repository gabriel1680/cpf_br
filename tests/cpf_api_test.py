import pytest

from cpfbr.cpf import *


def test_should_create_a_cpf():
    cpf = CPF("12345678909")
    assert isinstance(cpf, CPF)


def test_should_not_create_a_invalid_cpf():
    with pytest.raises(Exception):
        CPF("12345678919")


def test_should_format_cpf():
    cpf = CPF("12345678909")
    assert cpf.with_format() == "123.456.789-09"


def test_should_get_value():
    cpf = CPF("12345678909")
    assert cpf.value() == "12345678909"


def test_should_get_length():
    assert len(CPF("12345678909")) == 11


def test_string_equality():
    assert (CPF("12345678909") == "12345678909") is True


@pytest.fixture
def cpf_with_format_list():
    return [
        ["12345678909", "12345678909"],
        ["123.456.789-09", "12345678909"],
        ["12345678909", "123.456.789-09"],
        ["123.456.789-09", "123.456.789-09"],
    ]


def test_string_equality_with_string_formatting(cpf_with_format_list: tuple[str, str]()):
    for cpf_tuple in cpf_with_format_list:
        [first_cpf, second_cpf] = cpf_tuple
        assert (CPF(first_cpf) == second_cpf) is True


def test_object_equality():
    assert (CPF("12345678909") == CPF("12345678909")) is True


def test_string_equality_false():
    assert (CPF("12345678909") == "61762440059") is False


def test_object_equality_false():
    assert (CPF("12345678909") == CPF("61762440059")) is False


def test_object_equality_false_with_list():
    assert (CPF("12345678909") == ["61762440059"]) is False


def test_none_equality():
    assert (CPF("12345678909") == None) is False


def test_string_casting():
    cpf = CPF("12345678909")
    assert f"cpf: {cpf}" == "cpf: 12345678909"
    assert str(cpf) is "12345678909"
