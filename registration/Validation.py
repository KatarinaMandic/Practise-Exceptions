from exceptions.UnmatchedPasswordsError import UnmatchedPasswordsError
from exceptions.InvalidYearError import InvalidYearError
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