from cpfbr.validation import are_verification_digits_valid


def test_verification_digits_validation():
    cpf = "61762440059"
    assert are_verification_digits_valid(cpf) is True


def test_verification_digits_validation_with_invalid_first_digit():
    cpf = "61762440069"
    assert are_verification_digits_valid(cpf) is False


def test_verification_digits_validation_with_invalid_last_digit():
    cpf = "61762440058"
    assert are_verification_digits_valid(cpf) is False
