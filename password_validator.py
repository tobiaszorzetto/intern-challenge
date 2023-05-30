import argparse
from length_checker import LengthChecker
from invalid_checker import InvalidChecker
from score_calculation import ScoreCalculation
from variation_checker import VariationChecker

def validate_password(pwd):
    #O(n)
    print("Checking for invalid characters")
    InvalidChecker(pwd)

    print("Checking the password length")
    LengthChecker(pwd)

    print("Checking for variation")
    VariationChecker(pwd)

    print("Checking password score")
    score = ScoreCalculation(pwd).check_score_characters()

    print("----")
    print(f"Valid password")
    print(f"Score: {score}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--password', action = 'store', dest = 'password')
    pwd = parser.parse_args().password
    validate_password(pwd)
