



class ArcServ():
    """
    Класс Архитектуры сервиса
    """

    def __init__(self):
        self.code = ''
        self.description = ''
        self.period = ''
        self.arcitect = ''

    def __str__(self):
        return f'{self.__class__.__name__}: {self.code}; {self.period}; {self.arcitect}'
