from exceptions.UnmatchedPasswordsError import UnmatchedPasswordsError

class Validation:

    @staticmethod
    def password_check(password, confirmed_password):
        if password == confirmed_password:
            return True
        else:
            raise UnmatchedPasswordsError()