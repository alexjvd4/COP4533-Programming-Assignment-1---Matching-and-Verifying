"""
COP4533 Algorithm Abstraction & Design Programming Assignment 1
Gale Shapely Algorithm & Verifier

Input Handler input.py

Alejandro Velez & Marco Fernandez
"""


def create_priority_map(f, length):
    """
    Creates a priority map for either the hospitals or the applicants/students

    Key is the hospital/student beginning at index 0
    Value is the list of preferences, highest priority beginning at index 0

    :str_line: A single string representing the priority list with spaces
    :length: An integer representing the length of the priority list
    :is_hospital: A boolean declaring if we are dealing with hospital or applicant priorities

    """
    priority_map = {}
    for i in range(length):
        str_line = f.readline().strip()
        priority_map[i] = list(map(int, str_line.split()))

    return priority_map


print("Type the name of the txt file to use as input priority lists.")
filename = input("Some filenames in the codebase are input.txt, empty.txt, one-one input.txt \n")

with open(filename, "r") as f:
    line = f.readline()
    size = int(line)
    hospital_map = create_priority_map(f, size)
    student_map = create_priority_map(f, size)
