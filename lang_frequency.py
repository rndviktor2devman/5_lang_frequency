import re, string, sys
from itertools import islice

def load_data(filepath):
	with open(filepath) as data_file:
		splitted_text = re.findall(r"[\w']+", data_file.read())
	return splitted_text


def get_most_frequent_words(text):
	frequencies_dictionary = {}
	for word in text:
		lower_word = word.lower()
		if lower_word in frequencies_dictionary.keys():
			frequencies_dictionary[lower_word] += 1
		else:
			frequencies_dictionary[lower_word] = 1

	for (word, frequency) in islice(reversed(sorted(frequencies_dictionary.items(), key=lambda x:x[1])), 10):
		print("the word '{}' was found {} times in the text".format(word, frequency))


if __name__ == '__main__':
	input_parameter = sys.argv[1]
	if input_parameter.lower().endswith('.txt'):
		solid_text = load_data(input_parameter)
		get_most_frequent_words(solid_text)
	else:
		raise NameError('Wrong file type!')
