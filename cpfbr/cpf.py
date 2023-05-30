from validation import *


class CPF:

    def __init__(self, cpf: str) -> None:
        if not CPF.validate(cpf):
            raise Exception("Invalid CPF")
        self.__value = strip_chars(cpf)

    @staticmethod
    def validate(cpf: str) -> bool:
        return is_cpf_valid(cpf)

    def with_format(self) -> str:
        template = "{}{}{}.{}{}{}.{}{}{}-{}{}"
        return template.format(*list(self.__value))

    def value(self) -> str:
        return self.__value

    def __len__(self) -> int:
        return len(self.__value)

    def __eq__(self, cpf: object | str) -> bool:
        if cpf is None:
            return False
        if type(cpf) is str:
            return self.__value == cpf or self.with_format() == cpf
        if not isinstance(cpf, CPF):
            return False
        return cpf.value() == self.__value

    def __str__(self) -> str:
        return self.__value
