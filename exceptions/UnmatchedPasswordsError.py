class UnmatchedPasswordsError(Exception):

    def __init__(self) -> None:
        super().__init__('Passwords do not match.')