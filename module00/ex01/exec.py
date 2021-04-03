import sys
if len(sys.argv) > 1:
	txt = ""
	for arg in sys.argv[1:]:
			txt = arg[::-1].swapcase() + " " + txt
	print(txt[:-1])