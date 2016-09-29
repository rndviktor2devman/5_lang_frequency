import re
import string
import sys
from itertools import islice

def load_data(filepath):
    try:
        with open(filepath) as data_file:
            splitted_text = re.findall(r"[\w']+", data_file.read())
            return splitted_text
    except UnicodeDecodeError:
        raise Exception("Wrong file type.")


def get_most_frequent_words(text):
    frequencies_dictionary = {}
    for word in text:
        lower_word = word.lower()
        if lower_word in frequencies_dictionary.keys():
            frequencies_dictionary[lower_word] += 1
        else:
            frequencies_dictionary[lower_word] = 1
    return frequencies_dictionary


def print_top_ten(dictionary, length):
    sorted_dictionary = sorted(dictionary.items(), key=lambda x:x[1])
    reversed_dictionary = reversed(sorted_dictionary)
    for (word, frequency) in islice(reversed_dictionary, length):
        print("word '{}' found {} times".format(word, frequency))

def get_output_length():
    default = 10
    try:
        if len(sys.argv) > 2:
            return int(sys.argv[2])
        else:
            return default
    except ValueError:
        return default

if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_parameter = sys.argv[1]
        splitted_text = load_data(input_parameter)
        words_frequency = get_most_frequent_words(splitted_text)
        output_length = get_output_length()
        print_top_ten(words_frequency, output_length)
    else:
        raise Exception('Missing input file.')
