"""
CS1026a 2023
Assignment 03
Bruce
251368377
blin232
11/15/2023

This file takes inputs from the user and call the functions in sentiment_analysis.py
"""

# Import the sentiment_analysis module
from sentiment_analysis import *

# Main function to take inputs
def main():
    try:
        keyword_file_name = input("Input keyword filename (.tsv file): ")
        tweet_file_name = input("Input tweet filename (.csv file): ")
        report_file_name = input("Input filename to output report in (.txt file): ")

        if not keyword_file_name.endswith('.tsv'):
            raise Exception("Must have tsv file extension!")

        if not tweet_file_name.endswith('.csv'):
            raise Exception("Must have csv file extension!")

        if not report_file_name.endswith('.txt'):
            raise Exception("Must have txt file extension!")

        keyword_dict = read_keywords(keyword_file_name)
        tweet_list = read_tweets(tweet_file_name)

        if not keyword_dict or not tweet_list:
            raise Exception("Tweet list or keyword dictionary is empty!")
            
        report = make_report(tweet_list, keyword_dict)

        write_report(report, report_file_name)

    except Exception as e:
        print(e)

main()
