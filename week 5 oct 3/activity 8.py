def title(symbol, text, isUpper=False):
    width = len(text) + 4
    if isUpper:
        text = text.upper()
    result = ""
    result += symbol * width + "\n"
    result += f"{symbol} {text} {symbol}\n"
    result += symbol * width + "\n"
    return result

def main():
    user_input = input("Enter your title text: ")
    formatted_title = title('#', user_input, isUpper=False)
    print(formatted_title)

main()