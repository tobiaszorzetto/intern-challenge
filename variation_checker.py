import re

from password_exceptions import MissingCharacterException

class VariationChecker:
    """
    This class should contain the code to check if there's a minimum of:
     - One numerical digit
     - One special character
     - One uppercase letter
     - One lowercase letter
     If not, the password is invalid
    """

    def __init__(self, password: str) -> None:
        #O(n)
        if not re.search("[0-9]", password):
            raise MissingCharacterException("digit")
        if not re.search("[a-z]", password):
            raise MissingCharacterException("lowercase character")
        if not re.search("[A-Z]", password):
            raise MissingCharacterException("uppercase character")
        if not re.search("[!$%&\()*+-/?@_]", password):
            raise MissingCharacterException("special character")

        
