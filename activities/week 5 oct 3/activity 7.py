def breakdown(number):
    num_str = str(number)
    length = len(num_str)
    breakdown_parts = []
    for i, digit in enumerate(num_str):
        place_value = 10 ** (length - i - 1)
        part = int(digit) * place_value
        breakdown_parts.append(str(part))
    expression = ' + '.join(breakdown_parts)
    return expression

def main():
    number = int(input("Enter a number: "))
    result = breakdown(number)
    print(f"{number} broken down looks like:")
    print(f"{result}")

main()