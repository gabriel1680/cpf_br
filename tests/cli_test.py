import subprocess


def test_should_validate_a_cpf_from_cli():
    process_result = subprocess.run(
        ['python3', 'cpfbr', '1234567890', '-v'], stdout=subprocess.PIPE)
    print(process_result.stdout)
    assert process_result.stdout == b'invalid\n'


def test_should_format_a_cpf_from_cli():
    process_result = subprocess.run(
        ['python3', 'cpfbr', '61762440059', '-f'], stdout=subprocess.PIPE)
    print(process_result.stdout)
    assert process_result.stdout == b'617.624.400-59\n'
