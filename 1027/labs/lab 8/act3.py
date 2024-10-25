sentence = "I had such a horrible day It was awful so bad sigh it could not have been worse but actually though it was such a terrible horrible awful bad day"

makeItHappy = {"horrible":"amazing","bad":"good","awful":"awesome","worse":"better","terrible":"great"}

spsentence = sentence.split()
for word in range(len(spsentence)-1): # Should iterate trhough the index of spsentence not the values
    if spsentence[word] in makeItHappy:
        spsentence[word] = makeItHappy[spsentence[word]] # Incorrect access point for dictionary, should be spsentence[word]

newString = ""

for word in spsentence:
    newString = newString + word + " "

print(newString)