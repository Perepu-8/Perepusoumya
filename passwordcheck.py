import re

def check_password_strength(password):
    strength = 0
    remarks = ""

    # Conditions
    length_regex = r'.{8,}'                # Minimum 8 characters
    lowercase_regex = r'[a-z]'             # At least one lowercase
    uppercase_regex = r'[A-Z]'             # At least one uppercase
    digit_regex = r'[0-9]'                 # At least one digit
    special_char_regex = r'[@$!%*?&]'      # At least one special character

    # Checking conditions
    if re.search(length_regex, password):
        strength += 1
    if re.search(lowercase_regex, password):
        strength += 1
    if re.search(uppercase_regex, password):
        strength += 1
    if re.search(digit_regex, password):
        strength += 1
    if re.search(special_char_regex, password):
        strength += 1

    # Remarks
    if strength == 5:
        remarks = "Excellent Password 🔥"
    elif strength == 4:
        remarks = "Strong Password 👍"
    elif strength == 3:
        remarks = "Medium Password 🙂 – IMPROVE"
    elif strength == 2:
        remarks = "Weak Password 😕"
    else:
        remarks = "Very Weak Password 🚫" 

    return strength, remarks


# MAIN PROGRAM
print("# PASSWORD STRENGTH CHECKER")
pwd = input("Enter your password: ")

score, message = check_password_strength(pwd)

print("\nStrength Score:", score, "/ 5")
print("Result:", message)
