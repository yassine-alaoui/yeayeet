import random
t = random.randrange(1,99)
atmpt = 0
print("""This is an interactive guessing game!
You have to enter a number between 1 and 99 to find out the secret number.
Type 'exit' to end the game.
Good luck!
""")
while (1):
	b = input("What's your guess between 1 and 99?\n>> ")
	if b == "exit":
		print("Goodbye!")
		exit (0)
	atmpt += 1
	if not b.isdigit():
		print("That's not a number.")
		continue
	b = int(b)
	if b == t: 
		print(("Congratulations, you've got it!\nYou won in %d attempts!" % atmpt) if atmpt > 1 else "Congratulations! You got it on your first try!")
		exit (0)
	elif b > t:
		print("Too high!")
	elif b < t:
		print("Too low!")