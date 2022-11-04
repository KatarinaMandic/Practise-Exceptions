from exceptions.UnmatchedPasswordsError import UnmatchedPasswordsError
from exceptions.InvalidYearError import InvalidYearError
from exceptions.InvalidEmailError import InvalidEmailError
from exceptions.InvalidTelephoneError import InvalidTelephoneError
import re

class Validation:

    @staticmethod
    def check_password(password, confirmed_password):
        if password == confirmed_password:
            return True
        else:
            raise UnmatchedPasswordsError()

    def check_year(year):
        pattern = re.compile('^\d{4}$')
        if pattern.match(year) != None:
            year = int(year)
            if year > 1900 and year < 2009:
                return True
            else:
                raise InvalidYearError()
        else:
            raise InvalidYearError()

    def check_email(email):
        pattern = re.compile('.+@+.+\.+.+')
        if pattern.match(email) != None:
            return True
        else:
            raise InvalidEmailError()

    def check_telephone(telephone):
        pattern = re.compile('^06\d\s\d{3}\s\d{3,4}$')
        if pattern.match(telephone) != None:
            return True
        else: 
            raise InvalidTelephoneError()