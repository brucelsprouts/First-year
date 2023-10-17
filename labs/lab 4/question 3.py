#Fourth error (string wasnt defined, however the parameter that should be used is word)

def countVowels(word):
    numVowels = 0  #Starts with no vowels counted not 1
    for letter in word:  #Use "word" as the parameter, not "string"
        if letter in "aeiou":
            numVowels += 1
    return numVowels  #Returns the count of vowels, not "letter"

#Test Cases:
print(countVowels("AEIOu"))
print(countVowels("apple"))
print(countVowels("APPLE"))
print(countVowels("Jdjadwaa*8DJ"))
print(countVowels(""))

#The initial output before the corrections are not correct and it dosnt ouput anything
#Since the counter variable "letter" is being returned as well as nothing being printed