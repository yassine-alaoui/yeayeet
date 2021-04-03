import sys
if len(sys.argv) > 1:
	txt = ""
	prev = ""
	for i, arg in enumerate(sys.argv):
		if i > 0:
			prev = txt
			txt = arg[::-1].swapcase()
			if i - 1:
				txt += " "
			txt += prev
	print(txt)