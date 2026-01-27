"""
COP4533 Algorithm Abstraction & Design Programming Assignment 1
Gale Shapely Algorithm & Verifier

Main algorithm/program main.py

Alejandro Velez & Marco Fernandez
"""
import input
import verifier
import sys 

hospitals = input.hospital_map
students = input.student_map

if hospitals and students:
    print("Gale Shapely Algorithm initiating ...")
    for h_id, hospital in hospitals.items():
        if hospital["pair"] is None:
            for student in hospital["preferences"]:
                if students[student]["pair"] is None:
                    hospital["pair"] = student
                    students[student]["pair"] = h_id
                    break
                elif students[student]["preferences"].index(students[student]["pair"]) > students[student][
                    "preferences"].index(h_id):
                    hospitals[students[student]["pair"]] = None
                    hospital["pair"] = student
                    students[student]["pair"] = h_id
                    break

    print("Gale Shapely Algorithm successfully implemented!\n")

    # Output Handler: Algorithm results are loaded to output.txt
    with open("output.txt", "w") as f:
        for hospital in hospitals:
            f.write(str(hospital) + " " + str(hospitals[hospital]["pair"]) + "\n")

    print("Matching results located in output.txt")


    if len(sys.argv) != 2:
        print("INVALID")
        sys.exit(0)

    match_file = sys.argv[1]
    hospital_lists = []
    student_lists = []

    for hospital in hospitals.values():
        hospital_lists.append(hospital["preferences"])

    for student in students.values():
        student_lists.append(student["preferences"])

    n,  = input.size, 
    hospital_match, student_match = verifier.read_matching(match_file, n)

    verifier.check_for_blocking_pairs(
        n,
        hospital_lists,
        student_lists,
        hospital_match,
        student_match
    )

