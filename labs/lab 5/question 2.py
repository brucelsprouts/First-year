#counts strings that fufill condition
def count_strings_with_same_first_last(input_list):
    count = 0
    for word in input_list:
        if len(word) >= 2 and word[0] == word[-1]:
            count += 1
    return count

#example usage
word_list = ['bgh', 'wer', 'yuy', '1661']
result = count_strings_with_same_first_last(word_list)
print("Number of strings that follow the conditions: ", result)