import re

def validate_password(password):
    # pattern
    pattern = r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$"

    # Password Validation
    match = re.match(pattern, password)

    # return True if the password matches the pattern
    return bool(match)

password1 = 'Testing123' #replace this
print(validate_password(password1))

result = validate_password(password1)
