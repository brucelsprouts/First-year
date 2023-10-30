def read_keywords(keyword_file_name):
    try:
        keyword_dict = {}
        with open(keyword_file_name, 'r') as file:
            for line in file:
                keyword, score = line.strip().split('\t')
                keyword_dict[keyword] = int(score)
        return keyword_dict
    except IOError:
        print(f"Could not open file {keyword_file_name}!")
        return {}

def clean_tweet_text(tweet_text):
    # Remove non-English letters and make lowercase
    return ''.join(char.lower() if char.isalpha() or char.isspace() else '' for char in tweet_text)

def calc_sentiment(tweet_text, keyword_dict):
    words = tweet_text.split()
    sentiment_score = 0
    for word in words:
        if word in keyword_dict:
            sentiment_score += keyword_dict[word]
    return sentiment_score

def classify(score):
    if score > 0:
        return "positive"
    elif score < 0:
        return "negative"
    else:
        return "neutral"

def read_tweets(tweet_file_name):
    try:
        tweet_list = []
        with open(tweet_file_name, 'r') as file:
            for line in file:
                fields = line.strip().split(',')
                tweet = {
                    'date': fields[0],
                    'text': clean_tweet_text(fields[1]),
                    'user': fields[2],
                    'favorite': int(fields[3]),
                    'retweet': int(fields[4]),
                    'lang': fields[5],
                    'city': fields[6],
                    'state': fields[7],
                    'country': fields[8],
                    'lat': float(fields[9]) if fields[9] != 'NULL' else 'NULL',
                    'lon': float(fields[10]) if fields[10] != 'NULL' else 'NULL'
                }
                tweet_list.append(tweet)
        return tweet_list
    except IOError:
        print(f"Could not open file {tweet_file_name}!")
        return []

def make_report(tweet_list, keyword_dict):
    num_favorite = 0
    num_retweet = 0
    num_tweets = len(tweet_list)
    num_positive = 0
    num_negative = 0
    num_neutral = 0
    total_sentiment = 0
    country_sentiments = {}

    for tweet in tweet_list:
        sentiment = calc_sentiment(tweet['text'], keyword_dict)
        total_sentiment += sentiment

        if tweet['favorite'] > 0:
            num_favorite += 1

        if tweet['retweet'] > 0:
            num_retweet += 1

        if sentiment > 0:
            num_positive += 1
        elif sentiment < 0:
            num_negative += 1
        else:
            num_neutral += 1

        if tweet['country'] != 'NULL':
            if tweet['country'] in country_sentiments:
                country_sentiments[tweet['country']].append(sentiment)
            else:
                country_sentiments[tweet['country']] = [sentiment]

    avg_favorite = round(total_sentiment / num_favorite, 2) if num_favorite > 0 else 'NAN'
    avg_retweet = round(total_sentiment / num_retweet, 2) if num_retweet > 0 else 'NAN'
    avg_sentiment = round(total_sentiment / num_tweets, 2) if num_tweets > 0 else 'NAN'

    # Calculate average sentiment for each country
    avg_country_sentiments = {country: round(sum(sentiments) / len(sentiments), 2)
                              for country, sentiments in country_sentiments.items()}
    # Sort countries by average sentiment in descending order
    sorted_countries = sorted(avg_country_sentiments.keys(), key=lambda x: avg_country_sentiments[x], reverse=True)
    top_five_countries = ', '.join(sorted_countries[:5])

    report = {
        'avg_favorite': avg_favorite,
        'avg_retweet': avg_retweet,
        'avg_sentiment': avg_sentiment,
        'num_favorite': num_favorite,
        'num_negative': num_negative,
        'num_neutral': num_neutral,
        'num_positive': num_positive,
        'num_retweet': num_retweet,
        'num_tweets': num_tweets,
        'top_five': top_five_countries
    }

    return report

def write_report(report, output_file):
    try:
        with open(output_file, 'w') as file:
            file.write("avg_favorite\t{}\n".format(report['avg_favorite']))
            file.write("avg_retweet\t{}\n".format(report['avg_retweet']))
            file.write("avg_sentiment\t{}\n".format(report['avg_sentiment']))
            file.write("num_favorite\t{}\n".format(report['num_favorite']))
            file.write("num_negative\t{}\n".format(report['num_negative']))
            file.write("num_neutral\t{}\n".format(report['num_neutral']))
            file.write("num_positive\t{}\n".format(report['num_positive']))
            file.write("num_retweet\t{}\n".format(report['num_retweet']))
            file.write("num_tweets\t{}\n".format(report['num_tweets']))
            file.write("top_five\t{}\n".format(report['top_five']))
        print(f"Wrote report to {output_file}")
    except IOError:
        print(f"Could not open file {output_file}")

# Usage:
# You can call these functions in your main.py script with the appropriate arguments.
