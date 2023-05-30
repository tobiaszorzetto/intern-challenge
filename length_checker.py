from password_exceptions import ShortPasswordException


class LengthChecker:
    """
    This class should contain the code to check the password length.
    If lower than 8, the password is invalid
    """

    def __init__(self, password: str, min_length: int = 8) -> None:
        #O(1)
        length = len(password)
        if length < min_length:
            raise ShortPasswordException
