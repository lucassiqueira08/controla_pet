
class InvalidCPFError(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        self.message = msg

    def __str__(self):
        return self.message
