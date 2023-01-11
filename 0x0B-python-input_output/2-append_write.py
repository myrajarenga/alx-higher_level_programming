#!/usr/bin/python3

"""appends characters to a file"""

def append_write(file="", text=""):
    """a function to append a text to afile"""

    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
