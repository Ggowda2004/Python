#regular expressions in python is handled by the re module. It provides functions to search, match, and manipulate strings using regular expressions.
import re
#searching for a pattern in a string
text = "The rain in Spain stays mainly in the plain."
pattern = r"ain"
matches = re.findall(pattern, text)
print(matches)  # Output: ['ain', 'ain', 'ain']


#replacing a pattern in a string
new_text = re.sub(pattern, "XXX", text)
print(new_text)  # Output: "The rXXX in SpXXX stays mXXXly in the plXXX."


#splitting a string based on a pattern
split_text = re.split(r"\s+", text)
print(split_text)  # Output: ['The', 'rain', 'in', 'Spain', 'stays', 'mainly', 'in', 'the', 'plain.']

#using raw strings to searh 1 \w - is used to match any word character (alphanumeric or underscore), \d - is used to match any digit, \s - is used to match any whitespace character
raw_pattern = r"\w+"
raw_matches = re.findall(raw_pattern, text)