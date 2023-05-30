class CommonPasswordChecker:
    """
    This class should contain the code to check
    if the password contains a common word, using the common_words.txt dataset
    """
    def __init__(self, password: str) -> None:
        self.password = password

    def check_common(self) -> bool:
        #O(n) -> number of common words is constant
        with open("common_words.txt", "r") as file:
            data = file.read()
        data = [line for line in data.splitlines()]
        if any(word in self.password for word in data):
            return True
        return False
