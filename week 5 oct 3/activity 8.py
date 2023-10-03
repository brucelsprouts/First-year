def print_line(symbol, width):
    """Print a line of symbols."""
    print(symbol * width)

def print_text_with_border(symbol, text, width):
    """Print text with symbols on either side."""
    formatted_text = f"{symbol} {text} {symbol}"
    print(formatted_text.center(width, symbol))

def title(symbol, text, isUpper, width):
    """Format text as a title with a border of symbols."""
    if isUpper:
        text = text.upper()
    
    total_width = width + 4
    print_line(symbol, total_width)
    print_text_with_border(symbol, text, total_width)
    print_line(symbol, total_width)

def main():
    # Get user inputs
    text = input("Enter the title text: ")
    symbol = input("Enter the symbol to use for the border: ")
    is_upper = input("Convert text to uppercase? (Y/N): ")
    width = int(input("Enter the width to add on either side of the text: "))
    
    # Check if the user wants to convert text to uppercase
    if is_upper.upper() == 'Y':
        is_upper = True
    elif is_upper.upper() == 'N':
        is_upper = False
    else:
        print("Error: Please enter 'Y' or 'N' for converting text to uppercase.")
        return
    
    # Call the title function to create the title-like text
    title(symbol, text, is_upper, width)

main()