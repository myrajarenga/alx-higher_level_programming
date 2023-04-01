#!/usr/bin/python3

def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers using recursion.
    """
    length = len(list_of_integers)
    if length == 0:
        return None
    mid_index = length // 2
    mid_value = list_of_integers[mid_index]
    if length == 1:
        return mid_value
    elif length == 2:
        return max(list_of_integers)
    elif mid_value < list_of_integers[mid_index-1]:
        return find_peak(list_of_integers[:mid_index])
    elif mid_value < list_of_integers[mid_index+1]:
        return find_peak(list_of_integers[mid_index+1:])
    else:
        return mid_value
