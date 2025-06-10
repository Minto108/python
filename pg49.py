def string_both_ends(input_string):
	if len(input_string) < 2:
		return -1
	return input_string[:2] + input_string[-2:]

input_string="w3w"
print(string_both_ends(input_string))