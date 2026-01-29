"""
COP4533 Algorithm Abstraction & Design Programming Assignment 1
Gale Shapely Algorithm & Verifier

Input Handler input_handler.py

Alejandro Velez
"""
import sys


def create_priority_map(f, length):
    """
    Creates a priority map for either the hospitals or the applicants/students.

    Key is the hospital/student beginning at hospital/student 1. Value is a map of with thekey being a list of
    preferences, highest priority beginning at index 0, and the value being who/what it's paired with.

    :param f: The opened input file
    :param length: An integer representing the length of the priority list
    :return: A priority map including all priority lists and empty pairs of all entities of the same category
    """
    priority_map = {}
    for i in range(length):
        str_line = f.readline().strip()
        if str_line != '':
            try:
                priority_list = list(map(int, str_line.split()))
            except:
                print("ERROR: Non-numeric ID in priority list for selector " + str(i + 1))
                sys.exit(0)
            priority_list_len = len(priority_list)
            if priority_list_len != length:
                print("ERROR: Priority list length of selector " + str(
                    i + 1) + " does match the amount of options available.")
                sys.exit(0)
            elif len(set(map(int, str_line.split()))) != priority_list_len:
                print("ERROR: Priority list elements of selector " + str(i + 1) + " are non-unique.")
                sys.exit(0)
            elif not all(0 <= p <= length for p in priority_list):
                print("ERROR: Invalid selector ID in priority list for selector " + str(i + 1))
                sys.exit(0)
            priority_map[i + 1] = {"preferences": priority_list, "pair": None}
        else:
            print("ERROR: Not enough input records.")
            sys.exit(0)
    return priority_map


def read_input_file(filename):
    """
    Reads the input file and returns two priority maps for the Gale Shapely algorithm as well as their equal size.

    :param filename: An input filename string
    :return: Hospital priority map, student priority map, the number of entities in each map
    """
    hospital_map = {}
    student_map = {}
    with open(filename, "r") as f:
        line = f.readline()
        if line != '':
            size = int(line)
            print("\nLoading hospital priorities ...")
            hospital_map = create_priority_map(f, size)
            print("Loading student priorities ...\n")
            student_map = create_priority_map(f, size)
            if f.readline() != '':
                print("ERROR: Too many input records.")
                sys.exit(0)
        else:
            print("ERROR: Empty input file.")
            sys.exit(0)

    return hospital_map, student_map, size
