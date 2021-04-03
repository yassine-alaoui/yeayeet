import sys
arr = ["I'm Even.", "I'm Odd.", "I'm Zero."]
if len(sys.argv) == 2 and sys.argv[1].isdigit():
	num = int(sys.argv[1])
	if (num == 0):
		print(arr[2])
	else:
		print(arr[num%2])
else:
	print("ERROR")