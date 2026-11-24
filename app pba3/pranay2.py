import re

def validate_password(password):

    patterns = {
        "Minimum 8 characters": r".{8,}",
        "At least one uppercase letter": r"[A-Z]",
        "At least one lowercase letter": r"[a-z]",
        "At least one digit": r"[0-9]",
        "At least one special character": r"[!@#$%^&*(),.?\":{}|<>]"
    }

    errors = []

    for rule, pattern in patterns.items():
        if not re.search(pattern, password):
            errors.append(rule)

    if errors:
        print("Password is INVALID!")
        print("Missing requirements:")
        for error in errors:
            print("-", error)
    else:
        print("Password is VALID!")


password = input("Enter your password: ")

validate_password(password)
