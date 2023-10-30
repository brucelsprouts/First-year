# Import the sentiment_analysis module
from sentiment_analysis import *

def main():
    try:
        # Get user input for filenames
        keyword_file_name = input("Input keyword filename (.tsv file): ")
        tweet_file_name = input("Input tweet filename (.csv file): ")
        report_file_name = input("Input filename to output report in (.txt file): ")

        # Check file extensions
        if not keyword_file_name.endswith('.tsv'):
            raise Exception("Must have tsv file extension!")

        if not tweet_file_name.endswith('.csv'):
            raise Exception("Must have csv file extension!")

        if not report_file_name.endswith('.txt'):
            raise Exception("Must have txt file extension!")

        # Read keywords and tweets
        keyword_dict = read_keywords(keyword_file_name)
        tweet_list = read_tweets(tweet_file_name)

        # Check for empty data
        if not keyword_dict or not tweet_list:
            raise Exception("Tweet list or keyword dictionary is empty!")

        # Generate and write the report
        report = make_report(tweet_list, keyword_dict)
        write_report(report, report_file_name)

    except Exception as e:
        print(e)

main()