import sys
import traceback

from exceptions.MyException import MyException

try:
    raise MyException('This is some message')
except:
    tb = sys.exc_info()[2]
    print(sys.exc_info()[1])
    #print(traceback.format_tb(tb))