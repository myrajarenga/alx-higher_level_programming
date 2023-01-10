#!/usr/bin/python3

"""Prints alist frm a class"""


class MyList(list):
    """define aclass inheriting from alist"""
    def print_sorted(self):
        print(sorted(self))
