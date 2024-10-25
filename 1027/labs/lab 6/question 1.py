#Open file
f = open("text.txt", "r")

#State lists
positive = []
neutral = []
negative = []

#For every line in find, attach the word to their corresponding lists
for line in f:
    entries = line.split(",")
    entries[1] = int(entries[1].rstrip("\n"))
    if entries [1] == 20:
        positive.append(entries[0])
    elif entries[1] == 0:
        neutral.append(entries[0])
    else:
        negative.append(entries[0])

#Tweet message
tweet = "I really am very happy for you I love the weather I am also sad and have some regrets about being so tired"

#Spkits the tweet and for every word determine their sentiment from how positive or negative the words are
tweetWords = tweet.split()
sentiment = 0
for word in tweetWords:
    if word in positive:
        sentiment += 20
    elif word in negative:
        sentiment -= 10

#Output the keywords of file and sentiment of tweet
print("The postitive keywords are {}".format(positive))
print("The neutral keywords are {}".format(neutral))
print("The negative keywords are {}".format(negative))
print("The sentiment of the tweet is {}".format(sentiment))

#Close file
f.close()