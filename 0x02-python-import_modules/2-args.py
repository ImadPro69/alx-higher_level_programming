#!/usr/bin/python3

if __name__ == "__main__":

	import sys

	num_args = len(sys.argv) - 1
	args = sys.argv[1:]

	print("{} argument{}:".format(num_args, "s" if num_args != 1 else ""))
	for i, arg in enumerate(args):
		print("{}: {}".format(i + 1, arg))
