
class InvalidCPFError(Exception):
    def __init__(self, msg="CPF invalido"):
        super().__init__(msg)
        self.message = msg

    def __str__(self):
        return self.message


class DateError(Exception):
    def __init__(self, msg="Data inválida"):
        self.message = msg

    def __str__(self):
        return self.message


class MicrochipError(Exception):
    def __init__(self, msg="Microchip inválido"):
        self.message = msg

    def __str__(self):
        return self.message
