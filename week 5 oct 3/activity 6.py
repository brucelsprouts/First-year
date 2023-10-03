def twoOrMore(text):
    num_a = 0
    for char in text:
        if char == "a":
            num_a = num_a + 1
    return(num_a)

def main():
    string_word = input("Please enter a string: ")
    a_count = twoOrMore(string_word)
    if a_count >= 2:
        print("The string contians two or more 'a' charecters.")
    else:
        print("The string does not contain two or more 'a' charecters.")

main()