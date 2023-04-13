import re


def is_cpf_valid(cpf: str) -> bool:
    if not is_format_valid(cpf):
        return False
    cpf = strip_chars(cpf)
    if not are_verification_digits_valid(cpf):
        return False
    return not is_same_digits(cpf)


def is_format_valid(cpf: str) -> bool:
    regex = "(^([0-9]){3}\\.([0-9]){3}\\.([0-9]){3}\\-([0-9]){2}$)|(^[0-9]{11}$)"
    return bool(re.match(regex, cpf))


def are_verification_digits_valid(cpf: str) -> bool:
    first_digit = calculate_verification_digit(cpf, 10, 9)
    second_digit = calculate_verification_digit(cpf, 11, 10)
    cpf_verification_digits = cpf[-2:]
    return cpf_verification_digits == str(first_digit) + str(second_digit)


def strip_chars(cpf: str) -> str():
    return re.sub("\\D", "", cpf)


def calculate_verification_digit(cpf: str, factor: int, max: int) -> bool:
    total = 0
    cpf_arr = cpf_to_int_array(cpf)
    for digit in cpf_arr[0:max]:
        total += digit * factor
        factor -= 1
    return 0 if ((total % 11) < 2) else (11 - (total % 11))


def cpf_to_int_array(cpf: str) -> int():
    return list(map(lambda d: int(d), list(cpf)))


def is_same_digits(cpf: str) -> bool:
    return cpf[0] * len(cpf) == cpf
