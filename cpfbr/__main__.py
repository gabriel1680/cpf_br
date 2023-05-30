from sys import argv
from validation import is_cpf_valid
from cpf import CPF


def cli():
    if len(argv) < 3:
        return
    cpf = argv[1]
    flags = argv[2:]
    output = []
    if '-v' in flags:
        output.append('valid' if is_cpf_valid(cpf) else 'invalid')
    if '-f' in flags:
        try:
            output.append(CPF(cpf).with_format())
        except:
            output.append("Invalid CPF number. Could not format")
    return print(", ".join(output))


if __name__ == "__main__":
    cli()
