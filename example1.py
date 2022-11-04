from exceptions.MyException import MyException

try:
    raise MyException('This is some message')
except MyException as ex:
    print(ex.details())