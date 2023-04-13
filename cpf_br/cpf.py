from cpf_br.validation import is_cpf_valid


class CPF:

    def __init__(self, cpf: str) -> None:
        if not CPF.validate(cpf):
            raise ValueError("Invalid CPF")
        self.value = cpf

    @staticmethod
    def validate(cpf: str) -> bool:
        return is_cpf_valid(cpf)
