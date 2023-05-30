# Description

## PT-BR
cpfbr é uma abstração escrita em python para ajudar com as tarefas do dia a dia dos desenvolvedores que precisem lidar com a validação, criação, teste e formatação de cpfs brasileiros.

## US-EN
cpfbr is a abstraction written in python to help with developer every day tasks, that need to deal with validation, creation, testing and formatting of brasilian cpfs.

# Usage

## Main CPF class

use as value object inside a domain entity class

```python
# create_customer_controller.py

def handle_request(request) -> None:
    try:
        Customer(request.name, request.cpf, request.birth_date)
        customer_repository.add(customer)
        return { 'status': 'success', 'message': '', 'code': 201 }
    except ValueError e:
        return { 'status': 'error', 'message': e.message, 'code': 422 }

```

```python
# customer.py
from cpfbr import CPF
from datetime import datetime

class Customer:
    def __init__(self, name: str, cpf: str,  birth_date: str) -> None:
        self.__name = name
        self.__cpf = CPF(cpf)
        self.__birth_date = datetime.fromisoformat(birth_date)

    def name(self) -> str:
        return self.__name

    def cpf(self) -> CPF:
        return self.__cpf

    def birth_date(self) -> datetime:
        return self.__birth_date

    def __str__(self) -> str:
        return f"name: {self.__name}\ncpf: {self.__cpf}\nbirth_date: {self.__birth_date}"

    # ...

```

## Validation functions

use only functions to validate cpfs

```python
# create_customer_controller.py

from cpfbr import is_cpf_valid

def handle_request(request) -> None:
    if not request.name or not request.cpf or not request.birth_date:
        return bad_request("Invalid parameters")

    if not is_cpf_valid(request.cpf):
        return unprocessable_entity("Invalid CPF")

    Customer(request.name, request.cpf, request.birth_date)
    customer_repository.add(customer)

    return { 'status': 'success', 'message': '', 'code': 201 }

def unprocessable_entity(msg: str):
    return { 'status': 'Unprocessable Entity', 'message': msg, 'code': 422 }

def bad_request(msg: str):
    return { 'status': 'Bad Request', 'message': msg, 'code': 400 }
    
```
## Cli

You can use it from cli too!

command:

```sh
    python3 cpfbr 12345678909 -v -f
```
output:

```sh
    invalid, Invalid CPF number. Could not format
```

Command options:

flag | function
--- | ---
-v | Will execute the validate function and print it out on stdout
-f | Will execute the formatting function and print it out on stdout if the cpf is valid otherwise it will print a warning