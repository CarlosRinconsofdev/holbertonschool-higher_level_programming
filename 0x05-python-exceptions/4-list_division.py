#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    new = 0
    for i in range(list_length):
        try:
            new = (my_list_1[i] / my_list_2[i])
        except TypeError:
            new = 0
            print("wrong type")
        except ZeroDivisionError:
            new = 0
            print("division by 0")
        except IndexError:
            new = 0
            print("out of range")
        finally:
            new_list.append(new)
    return new_list
