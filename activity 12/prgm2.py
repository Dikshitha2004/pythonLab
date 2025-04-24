class InvalidScoreError(Exception):
    pass
def validate_score(score):
    if score < 0 or score > 100:
        raise InvalidScoreError("Score must be between 0 and 100.")
    return "Score is valid."
try:
    user_score = float(input("Enter your exam score: "))
    message = validate_score(user_score)
    print(message)
except InvalidScoreError as e:
    print(f"InvalidScoreError: {e}")
except ValueError:
    print("Error: Please enter a numeric value.")
