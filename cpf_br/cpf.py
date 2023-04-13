from cpf_br.validation import *


class CPF:

    def __init__(self, cpf: str) -> None:
        if not CPF.validate(cpf):
            raise Exception("Invalid CPF")
        self.value = strip_chars(cpf)

    @staticmethod
    def validate(cpf: str) -> bool:
        return is_cpf_valid(cpf)

    def with_format(self) -> str:
        format = "{}{}{}.{}{}{}.{}{}{}-{}{}"
        return format.format(*list(self.value))
