#!/usr/bin/python3
def uppercase(str):
	for i in range (len(str)):
		if (97 <= ord(str[i]) <= 122):
			str[i] -= 32
			print("{}".format(ord(str[i])))
