from common_password_checker import CommonPasswordChecker
from password_exceptions import InsufficientScoreException

class ScoreCalculation:
    """
    This class contains the code to calculate the score.
    Passwords with score lower than 16 are invalid
    """

    def __init__(self, password: str) -> None:
        self.password = password
        self.common_checker = CommonPasswordChecker(password).check_common()
        self.score = 0

    def check_score_characters(self) -> int:
        # O(n)
        special_chars = "!$%&\()*+-/?@_"

        for i, char in enumerate(self.password):
            if char in special_chars:
                self.score+=3
            else:
                self.score+=1

            if(i!=0 and self.password[i] == self.password[i-1]):
                self.score-=2
        
        if self.common_checker:
            self.score-=8

        if(self.score < 16):
            raise InsufficientScoreException(self.score)

        return self.score
