import string
from password_exceptions import InvalidCharacterException


class InvalidChecker:
    """
    This class should contain the code to check
    if the password contains any invalid characters
    """
    def __init__(self, password: int) -> None:
        #O(n)
        special_chars = "!$%&\()*+-/?@_"
        valid_chars = special_chars+string.ascii_uppercase+string.ascii_lowercase+string.digits
        if any(char not in valid_chars for char in password):
            raise InvalidCharacterException
