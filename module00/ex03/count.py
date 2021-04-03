def counter(string):
	print("- " + str(sum([char.isupper() for char in string])) + " upper letters")
	print("- " + str(sum([char.islower() for char in string])) + " lower letters")
	print("- " + str(sum([char in ",;:." for char in string])) + " punctuation marks")
	print("- " + str(string.count(" ")) + " spaces")

def text_analyzer(*string):
	if len(string) == 0:
		counter(str(input("What is the text to analyse?\n>>>")))
	elif len(string) > 1:
		print("ERROR")
	else:
		counter(string[0])