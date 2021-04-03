import sys
if len(sys.argv) != 3:
	print("ERROR")
else:
	if not sys.argv[2].isdigit():
		print("ERROR")
	else:
		var = [elm for elm in sys.argv[1].split(' ') if len(elm) > int(sys.argv[2])]
		print(var if len(var) > 0 else "ERROR")
	