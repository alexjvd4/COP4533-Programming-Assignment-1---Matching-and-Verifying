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
        priority_map[i + 1] = {"preferences": list(map(int, str_line.split())), "pair": None}
    return priority_map


print("Type the name of the txt file to use as input priority lists.")
filename = input("Some filenames in the codebase are input.txt, empty.txt, one-one input.txt \n")

with open(filename, "r") as f:
    line = f.readline()
    size = int(line)
    hospital_map = create_priority_map(f, size)
    student_map = create_priority_map(f, size)
