def is_valid_password(password):
    if len(password) < 10:
        return False, "Password should have at least 10 characters"
    
    special_characters = "!@#$%^&*_-()"
    has_special_char = any(char in special_characters for char in password)
    if not has_special_char:
        return False, "Password should contain at least one special character: !@#$%^&*_-()"
    
    has_digit = any(char.isdigit() for char in password)
    if not has_digit:
        return False, "Password should contain at least one digit"
    
    has_upper = any(char.isupper() for char in password)
    if not has_upper:
        return False, "Password should contain at least one uppercase letter"
    
    has_lower = any(char.islower() for char in password)
    if not has_lower:
        return False, "Password should contain at least one lowercase letter"
    
    return True, "Password is acceptable"

password = input("Enter a password: ")

valid, reason = is_valid_password(password)

# Display the result
if valid:
    print("Password is valid.")
else:
    print("Password is not valid.")
    print(reason)
