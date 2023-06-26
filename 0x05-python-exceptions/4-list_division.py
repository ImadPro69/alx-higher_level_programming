#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            quotient = 0
            if i < len(my_list_1) and i < len(my_list_2):
                if type(my_list_1[i]) not in [int, float] or type(my_list_2[i]) not in [int, float]:
                    raise TypeError("wrong type")
                if my_list_2[i] == 0:
                    raise ZeroDivisionError("division by 0")
                quotient = my_list_1[i] / my_list_2[i]
            else:
                raise IndexError("out of range")
            result.append(quotient)
        except ZeroDivisionError:
            result.append(0)
            print("division by 0")
        except TypeError:
            result.append(0)
            print("wrong type")
        except IndexError:
            result.append(0)
            print("out of range")
    return result

