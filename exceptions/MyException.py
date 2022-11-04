import inspect

class MyException(Exception):

    def __init__(self,message) -> None:
        super().__init__(message)
        self.exception_file = inspect.stack()[1].filename

    def details(self):
        return f'File: {self.exception_file}\nLine: {self.__traceback__.tb_lineno}\nMessage: {self}'