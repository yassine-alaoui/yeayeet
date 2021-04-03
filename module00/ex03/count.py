def counter(string):
	upper = 0
	lower = 0
	space = 0
	puncs = 0
	for char in string:
		if char == ' ':
			space += 1
		elif char.isupper():
			upper += 1
		elif char.islower():
			lower += 1
		else:
			puncs += 1
	print("- " + str(upper)+ " upper letters")
	print("- " + str(lower)+ " lower letters")
	print("- " + str(puncs)+ " punctuation marks")
	print("- " + str(space)+ " spaces")

def text_analyzer(*string):
	if len(string) == 0:
		counter(str(input("What is the text to analyse?\n>>>")))
	elif len(string) > 0:
		print("ERROR")
	else:
		counter(string[0])