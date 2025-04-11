def validate_password(password):
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    is_long_enough = len(password) >= 8

    if all([has_upper, has_lower, has_digit, is_long_enough]):
        print("Password is valid.")
    else:
        print("Password is invalid.")
validate_password("Pass1234")
