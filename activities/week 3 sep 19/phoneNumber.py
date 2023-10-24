#Activity 9: phoneNumber

phone_number = input("Enter a phone number in the format 226-XXX-XXXX: ")
phone_number = ''.join(filter(str.isdigit, phone_number))

#function that validates the phone number
def is_valid_phone_number(phone_number):
    if len(phone_number) != 10:
        return False

    if not phone_number.startswith("226"):
        return False

    if not phone_number[3:].isdigit():
        return False

    return True

# Check if the input is valid
if is_valid_phone_number(phone_number) == True:
    formatted_number = f"({phone_number[:3]}) {phone_number[3:6]}-{phone_number[6:]}"
    print(f"The phone number {formatted_number} is valid.")
else:
    print("Invalid phone number. Please enter a valid number in the format 226-XXX-XXXX.")

