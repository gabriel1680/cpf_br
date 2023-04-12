import re


class CPF:
    FACTOR_DIGIT_1 = 10
    FACTOR_DIGIT_2 = 11
    MAX_DIGITS_1 = 9
    MAX_DIGITS_2 = 10

    def __init__(self, cpf: str) -> None:
        if not CPF.validate(cpf):
            raise ValueError("Invalid CPF")
        self.value = cpf

    @staticmethod
    def validate(cpf: str) -> bool:
        cpf_len = len(cpf)
        if cpf_len == 11:
            return CPF.validate_numbers(stripe_chars(cpf))
        if cpf_len == 14:
            return CPF.validate_format_and_numbers(cpf)
        return False

    @staticmethod
    def validate_numbers(cpf_numbers: str) -> bool:
        if len(cpf_numbers) != 11:
            return False
        if cpf_numbers[0] * len(cpf_numbers) == cpf_numbers:
            return False
        return CPF.validate_verification_digits(cpf_numbers)

    @staticmethod
    def validate_verification_digits(cpf: str) -> str:
        first_digit = calculate_verification_digit(
            cpf, CPF.FACTOR_DIGIT_1, CPF.MAX_DIGITS_1)
        second_digit = calculate_verification_digit(
            cpf, CPF.FACTOR_DIGIT_2, CPF.MAX_DIGITS_2)
        cpf_verification_digits = cpf[-2:]
        return cpf_verification_digits == str(first_digit) + str(second_digit)

    @staticmethod
    def validate_format_and_numbers(cpf: str) -> bool:
        if not re.match('^([0-9]){3}\\.([0-9]){3}\\.([0-9]){3}\\-([0-9]){2}$', cpf):
            return False
        return CPF.validate_numbers(stripe_chars(cpf))


def cpf_to_int_array(cpf: str) -> int():
    return list(map(lambda d: int(d), list(cpf)))


def stripe_chars(cpf: str) -> str():
    return re.sub("\\D", "", cpf)


def calculate_verification_digit(cpf: str, factor: int, max: int) -> bool:
    total = 0
    cpf_arr = cpf_to_int_array(cpf)
    for digit in cpf_arr[0:max]:
        total += digit * factor
        factor -= 1
    return 0 if ((total % 11) < 2) else (11 - (total % 11))
