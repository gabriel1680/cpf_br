from cpfbr.validation import is_cpf_valid


def test_cpf_validation_with_format():
    cpf = "617.624.400-59"
    assert is_cpf_valid(cpf) is True


def test_cpf_validation_without_format():
    cpf = "61762440059"
    assert is_cpf_valid(cpf) is True


def test_invalid_cpf_number_with_same_digits_validation():
    cpf = "11111111111"
    assert is_cpf_valid(cpf) is False


def test_cpf_number_with_invalid_char_validation():
    cpf = "1234567891A"
    assert is_cpf_valid(cpf) is False


def test_cpf_number_with_invalid_verification_digits_validation():
    cpf = "12345678910"
    assert is_cpf_valid(cpf) is False


def test_invalid_cpf_without_format_validation():
    cpf = "1234567891"
    assert is_cpf_valid(cpf) is False


def test_invalid_cpf_with_format_validation():
    cpf = "123.456.789-101"
    assert is_cpf_valid(cpf) is False


def test_cpf_format_validation():
    cpf = "617.624.4005-9"
    assert is_cpf_valid(cpf) is False
