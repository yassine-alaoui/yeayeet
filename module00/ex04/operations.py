import sys
import math
if len(sys.argv) == 3:
	if (sys.argv[1].isdigit() == False) or (sys.argv[2].isdigit() == False):
		print("InputError: only numbers\n\nUsage: python operations.py <number1> <number2>\nExample:\n    python operations.py 10 3")
		exit(1)
	print("Sum:			" +  str(int(sys.argv[1]) + int(sys.argv[2])))
	print("Difference:		" +  str(int(sys.argv[1]) - int(sys.argv[2])))
	print("Product:		" +  str(int(sys.argv[1]) * int(sys.argv[2])))
	if (int(sys.argv[2]) != 0):
		print("Quotient:		" +  str(int(sys.argv[1]) / int(sys.argv[2])))
	else:
		print("Quotient:		ERROR (div by zero)")
	if (int(sys.argv[2]) != 0):
		print("Remainder:		" +  str(int(sys.argv[1]) % int(sys.argv[2])))
	else:
		print("Remainder:		ERROR (modulo by zero)")
elif len(sys.argv) > 3:
	print("InputError: too many arguments\n\nUsage: python operations.py <number1> <number2>\nExample:\n    python operations.py 10 3")
else:
	print("Usage: python operations.py <number1> <number2>\nExample:\n    python operations.py 10 3")