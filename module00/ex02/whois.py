import sys
map = ["I'm Even.", "I'm Odd.", "I'm Zero."]
if (len(sys.argv) == 2):
	num = int(sys.argv[1])
	if (num == 0):
		print(map[2])
	else:
		print(map[num%2])
else:
	print("ERROR")

