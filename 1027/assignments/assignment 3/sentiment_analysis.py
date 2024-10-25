# Function to read keywords and their scores from a file and create a dictionary
def read_keywords(keyword_file_name):
    keyword_dict = {}
    try:
        with open(keyword_file_name, 'r') as file:
            for line in file:
                keyword, score = line.strip().split('\t')
                keyword_dict[keyword] = int(score)
    except IOError:
        print(f"Could not open file {keyword_file_name}")
        return {}

    return keyword_dict

# Function to clean tweet text by removing non-alphabetic characters and converting to lowercase
def clean_tweet_text(tweet_text):
    clean_tweet = ''
    for char in tweet_text:
        if char.isalpha() or char.isspace():
            clean_tweet += char.lower()
    
    return clean_tweet

# Function to read tweets from a file and create a list of dictionaries representing each tweet
def read_tweets(tweet_file_name):
    tweet_list = []
    try:
        with open(tweet_file_name, 'r') as file:
            lines = file.readlines()
            for line in lines:
                data = line.strip().split(',')
                tweet = {
                    'date': data[0],
                    'text': clean_tweet_text(data[1]),
                    'user': data[2],
                    'retweet': int(data[3]),
                    'favorite': int(data[4]),
                    'lang': data[5],
                    'country': data[6] if data[6] != 'NULL' else 'NULL',
                    'state': data[7] if data[7] != 'NULL' else 'NULL',
                    'city': data[8] if data[8] != 'NULL' else 'NULL',
                    'lat': float(data[9]) if data[9] != 'NULL' else 'NULL',
                    'lon': float(data[10]) if data[10] != 'NULL' else 'NULL',
                }
                tweet_list.append(tweet)
    except IOError:
        print(f"Could not open file {tweet_file_name}")
        return []
    return tweet_list

# Function to calculate sentiment score of a tweet based on keywords and their scores
def calc_sentiment(tweet_text, keyword_dict):
    words = tweet_text.split()
    score = sum(keyword_dict.get(word, 0) for word in words)
    return score

# Function to classify sentiment based on the calculated score
def classify(score):
    if score > 0:
        return "positive"
    elif score < 0:
        return "negative"
    else:
        return "neutral"

# Function to generate a report based on tweet data and keyword dictionary
def make_report(tweet_list, keyword_dict):
    # Initialize report dictionary with default values
    report = {
        'avg_favorite': 'NAN',
        'avg_retweet': 'NAN',
        'avg_sentiment': 'NAN',
        'num_favorite': 0,
        'num_negative': 0,
        'num_neutral': 0,
        'num_positive': 0,
        'num_retweet': 0,
        'num_tweets': len(tweet_list),
        'top_five': ''
    }

    if len(tweet_list) > 0:
        # Variables for calculating averages and counts
        total_sentiment = 0
        num_fav = 0
        num_retweet = 0
        fav_sentiment = 0
        retweet_sentiment = 0
        sentiment_count = {'positive': 0, 'negative': 0, 'neutral': 0}
        country_sentiments = {}

        # Iterating through each tweet to calculate various metrics
        for tweet in tweet_list:
            total_sentiment += calc_sentiment(tweet['text'], keyword_dict)
            fav = tweet['favorite']
            retweet = tweet['retweet']

            # Calculate sentiment for favorited and retweeted tweets
            if fav > 0:
                num_fav += 1
                fav_sentiment += calc_sentiment(tweet['text'], keyword_dict)
            if retweet > 0:
                num_retweet += 1
                retweet_sentiment += calc_sentiment(tweet['text'], keyword_dict)

            # Classify sentiment and count occurrences
            sentiment = classify(calc_sentiment(tweet['text'], keyword_dict))
            sentiment_count[sentiment] += 1

            # Calculate sentiment for each country
            if tweet['country'] != 'NULL':
                if tweet['country'] not in country_sentiments:
                    country_sentiments[tweet['country']] = [calc_sentiment(tweet['text'], keyword_dict), 1]
                else:
                    country_sentiments[tweet['country']][0] += calc_sentiment(tweet['text'], keyword_dict)
                    country_sentiments[tweet['country']][1] += 1

        # Calculate averages and update the report
        report['avg_sentiment'] = round(total_sentiment / len(tweet_list), 2)
        if num_fav > 0:
            report['avg_favorite'] = round(fav_sentiment / num_fav, 2)
        if num_retweet > 0:
            report['avg_retweet'] = round(retweet_sentiment / num_retweet, 2)

        # Update counts in the report
        report['num_favorite'] = num_fav
        report['num_retweet'] = num_retweet
        report['num_negative'] = sentiment_count['negative']
        report['num_positive'] = sentiment_count['positive']
        report['num_neutral'] = sentiment_count['neutral']

        # Sort countries by average sentiment and extract top five
        sorted_countries = sorted(country_sentiments.items(), key=lambda x: x[1][0] / x[1][1], reverse=True)
        top_five_countries = [country[0] for country in sorted_countries[:5] if country[0] != 'NULL']
        report['top_five'] = ', '.join(top_five_countries)

    return report

# Function to write the generated report to an output file
def write_report(report, output_file):
    try:
        with open(output_file, 'w') as file:
            file.write('Average sentiment of all tweets: {}\n'.format(report['avg_sentiment']))
            file.write('Total number of tweets: {}\n'.format(report['num_tweets']))
            file.write('Number of positive tweets: {}\n'.format(report['num_positive']))
            file.write('Number of negative tweets: {}\n'.format(report['num_negative']))
            file.write('Number of neutral tweets: {}\n'.format(report['num_neutral']))
            file.write('Number of favorited tweets: {}\n'.format(report['num_favorite']))
            file.write('Average sentiment of favorited tweets: {}\n'.format(report['avg_favorite']))
            file.write('Number of retweeted tweets: {}\n'.format(report['num_retweet']))
            file.write('Average sentiment of retweeted tweets: {}\n'.format(report['avg_retweet']))
            file.write('Top five countries by average sentiment: {}\n'.format(report['top_five']))
        print(f"Wrote report to {output_file}")
    except IOError:
        print(f"Could not open file {output_file}")
