#Fourth error ( string wasnt defined, however the parameter that should be used is word)

def countVowels(word):
    numVowels = 0 #Starts with no vowels counted not 1
    for letter in word: #Use "word" as teh parameter, not "string"
        if letter in "aeiou":
            numVowels += 1
    return numVowels #Returns the count of vowels, not "lette"

#Test Cases:
print(countVowels("AEIOu"))
print(countVowels("apple"))
print(countVowels("APPLE"))
print(countVowels("JfAOIDwnNIOW"))
print(countVowels(""))

#The initial output before the corrections are not correct and it dosnt output anything
#Since the counter vairable "letter" is being returned as well as nothing being printed