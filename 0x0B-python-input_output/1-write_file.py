#!/usr/bin/python3

"""writes to file"""

def write_file(file="", text=""):
    """a function to write to afile and
    return number of characters written"""

    with open(filename, "w", encoding="utf=8") as f:
        return f.write(text)
