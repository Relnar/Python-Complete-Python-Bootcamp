import re

def multi_re_findall(patterns, phrase):
	for pattern in patterns:
		match = re.findall(pattern, phrase)
		print(f'pattern "{pattern}:"', match)


if __name__ == "__main__":
	patterns = ['term1', 'term2']
	text = "This is a string with term1, but not the other term"

	for pattern in patterns:
		print(f"search for {pattern} in: \n{text}:")

		if re.search(pattern, text):
			print("Match was found\n")
		else:
			print("No match was found\n")

	print(f'search "{patterns[0]}" in "{text}"')
	match = re.search(patterns[0], text)
	print(f"Match start: {match.start()}")
	print(f"Match end: {match.end()}")
	print("")

	split_term = "@"
	phrase = "What is your email, is it hello@gmail.com?"
	print(f'split "{phrase}" at the {split_term} character')
	print(re.split(split_term, phrase))
	print("")

	match = "match"
	phrase = "Here is one match, here is another match"
	print(f'findall "{match}" in "{phrase}"')
	print(re.findall(match, phrase))
	print("")

	test_phrase = "sdsd..sssdd...sdddsddd...dsds...dsssss...sdddd"
	test_patterns = [ "sd*",			# s followed by zero or mode d's
					  "sd+",			# s followed by one or more d's
					  "sd?",			# s followed by zero or one d's
					  "sd{3}",			# s followed by three d's
					  "sd{2,3}"			# s followed by two to three d's
					]
	print(f"Test phrase: {test_phrase}")
	multi_re_findall(test_patterns, test_phrase)
	print("")

	# Character sets
	test_patterns = [ "[sd]",			# either s or d
					  "s[sd]+"			# s followed by one or more s or d
					]
	print("Character sets")
	multi_re_findall(test_patterns, test_phrase)
	print("")

	# Exclusion
	print("Exclusion")
	test_phrase = "This is a string! But it has punctuation. How can we remove it?"
	test_patterns = [ "[^!.? ]+" ]
	print(f"Test phrase: {test_phrase}")
	multi_re_findall(test_patterns, test_phrase)
	print("")

	# Character ranges
	print("Character ranges")
	test_phrase = "This is an example sentence. Let's see if we can find some letters.?"
	test_patterns = [ "[a-z]+",			# sequences of lower case letters
					  "[A-Z]+",			# sequences of upper case letters
					  "[a-zA-Z]+",		# sequences of lower or upper case letters
					  "[A-Z][a-z]+"		# one upper case letter followed by lower case letters
					]
	print(f"Test phrase: {test_phrase}")
	multi_re_findall(test_patterns, test_phrase)
	print("")

	# Escape codes
	print("Escape codes")
	test_phrase = "This is a string with some numbers 1233 and a symbol #hashtag"
	test_patterns = [ r"\d+",			# sequence of digits
					  r"\D+",			# sequence of non-digits
					  r"\s+",			# sequence of whitespace
					  r"\S+",			# sequence of non-whitespace
					  r"\w+",			# alphanumeric characters
					  r"\W+",			# non-alphanumeric
					  r"[^\w\s]",		# only hashtag
					]
	print(f"Test phrase: {test_phrase}")
	multi_re_findall(test_patterns, test_phrase)
