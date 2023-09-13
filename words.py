
def print_upper_words(words, must_start_with):
	"""capitalizes and then prints out all words in words that start with a letter in must_start_with"""
	for w in words:
		if w[0] in must_start_with:
			print(w.capitalize())