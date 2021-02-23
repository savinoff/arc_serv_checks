


class TestResult():
    """
    Результат теста
    """

    def __init__(self, result_code: str = '', result_description: str = ''):
        self.result_code: str = result_code
        self.result_description: str = result_description

    def __str__(self):
        return f'Результат: {self.result_code}; {self.result_description}'

if __name__ == '__main__':
    rd = TestResult('OK')
    print(rd)
