import pytest

from cpfbr.validation import is_format_valid


@pytest.fixture
def valid_cpfs():
    return ["61762440059", "12345678909"]


def test_format_validation(valid_cpfs: str()):
    for cpf in valid_cpfs:
        assert is_format_valid(cpf) is True


@pytest.fixture
def valid_cpf_masks():
    return ["617.624.400-59", "123.456.789-09"]


def test_format_validation_with_valid_mask(valid_cpf_masks: str()):
    for cpf in valid_cpf_masks:
        assert is_format_valid(cpf) is True


@pytest.fixture
def invalid_cpf_masks():
    return ["617.624.4005-9", "617.62.4400-59", "61.7624.400-59", "617.6244.00-59"]


def test_format_validation_with_invalid_mask(invalid_cpf_masks: str()):
    for cpf in invalid_cpf_masks:
        assert is_format_valid(cpf) is False


def test_format_validation_with_invalid_digits():
    cpf = "61762440069"
    assert is_format_valid(cpf) is True


@pytest.fixture
def cpfs_with_invalid_length():
    return ["6176244005", "617624400591", "617624409"]


def test_format_validation_with_invalid_length(cpfs_with_invalid_length: str()):
    for cpf in cpfs_with_invalid_length:
        assert is_format_valid(cpf) is False


@pytest.fixture
def cpfs_with_invalid_char_sequence():
    return ["123456A8909", "1234-568909", "1234.6A8909", "1234.6A89\09"]


def test_format_validation_with_invalid_char_sequence(cpfs_with_invalid_char_sequence: str()):
    for cpf in cpfs_with_invalid_char_sequence:
        assert is_format_valid(cpf) is False
