class ExceptionCSV(Exception):
    """
    Exceções relacionadas ao arquivo CSV.
    """
    def __init__(self, message):
        super().__init__(message)


class ExceptionDataBase(Exception):
    """
    Exceções relacionadas ao banco de dados.
    """
    def __init__(self, message):
        super().__init__(message)
