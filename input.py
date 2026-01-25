"""
COP4533 Algorithm Abstraction & Design Programming Assignment 1
Gale Shapely Algorithm & Verifier

Input Handler input.py

Alejandro Velez
"""


def create_priority_map(f, length):
    """
    Creates a priority map for either the hospitals or the applicants/students.

    Key is the hospital/student beginning at hospital/student 1. Value is a map of with thekey being a list of
    preferences, highest priority beginning at index 0, and the value being who/what it's paired with.

    :f: The opened input file
    :length: An integer representing the length of the priority list

    """
    priority_map = {}
    for i in range(length):
        str_line = f.readline().strip()
        if str_line != '':
            try:
                priority_list = list(map(int, str_line.split()))
            except ValueError:
                raise ValueError("ERROR: Non-numeric ID in priority list for selector " + str(i + 1))
            priority_list_len = len(priority_list)
            if priority_list_len != length:
                raise ValueError("ERROR: Priority list length of selector " + str(
                    i + 1) + " does match the amount of options available.")
            elif len(set(map(int, str_line.split()))) != priority_list_len:
                raise ValueError("ERROR: Priority list elements of selector " + str(i + 1) + " are non-unique.")
            elif not all(0 <= p <= length for p in priority_list):
                raise ValueError("ERROR: Invalid selector ID in priority list for selector " + str(i + 1))
            priority_map[i + 1] = {"preferences": priority_list, "pair": None}
        else:
            raise ValueError("ERROR: Not enough input records.")
    return priority_map


print("Type the name of the txt file to use as input priority lists.")
filename = input("Some filenames in the codebase are input.txt, empty.txt, one-one input.txt \n")

with open(filename, "r") as f:
    line = f.readline()
    if line != '':
        size = int(line)
        print("\nLoading hospital priorities ...")
        hospital_map = create_priority_map(f, size)
        print("Loading student priorities ...\n")
        student_map = create_priority_map(f, size)
        if f.readline() != '':
            raise ValueError("ERROR: Too many input records.")
    else:
        raise ValueError("ERROR: Empty input file.")
