import os
from sys import argv

def main():
	
	arg = argv[1:]
	if (len(arg) < 1):
		print("Please provide a link!")
		return
	elif(len(arg) > 3):
		print("Expected less arguments!")
		return

	call = "..\libs\youtube-dl "

	while(arg):
		call += arg[0] + " "
		arg = arg[1:]

	os.system(call)

main()