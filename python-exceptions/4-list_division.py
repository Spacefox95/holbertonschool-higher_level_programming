#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
	new_list = []

	for i in range(list_length):
		sum = 0
		try:
			num1 = my_list_1[i]
			num2 = my_list_2[i]
			sum = num1 / num2
		except ZeroDivisionError:
			print("division by 0")
		except TypeError:
			print("wrong type")
		except IndexError:
			print("out of range")
		finally:
			new_list.append(sum)
	return new_list