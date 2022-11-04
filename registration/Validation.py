from exceptions.UnmatchedPasswordsError import UnmatchedPasswordsError
from exceptions.InvalidYearError import InvalidYearError
from exceptions.InvalidEmailError import InvalidEmailError
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