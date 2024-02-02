#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []

    for i in range(list_length):
        sum = 0
        try:
            if num1 < len(my_list_1):
                num1 = my_list_1[i]
            else:
                num1 = 0
            if num2 < len(my_list_2):
                num2 = my_list_2[i]
            else:
                num2 = 0
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
