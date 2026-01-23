"""
COP4533 Algorithm Abstraction & Design Programming Assignment 1
Gale Shapely Algorithm & Verifier

Main algorithm/program main.py

Alejandro Velez & Marco Fernandez
"""
import input

hospitals = input.hospital_map
students = input.student_map

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

"""
The :hospitals: and :students: maps will hold the matching result of the Gale Shapely algorithm.
Feel free to print them.

print(hospitals)
print(students)
"""
