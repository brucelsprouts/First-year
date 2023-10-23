def main():
    text = "Hello, World!"
    print(strToChar(text))
    chars = strToChar(text)
    print(charToStr(chars))

def strToChar(text):
    array = []
    for i in range(0,len(text)):
        array.append(text[i])
    return array


def charToStr(chars):  
    string = ''
    for i in range(0,len(chars)):
        string = string + chars[i]
    return string
    
main()