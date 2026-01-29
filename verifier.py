"""
COP4533 Algorithm Abstraction & Design Programming Assignment 1
Gale Shapely Algorithm & Verifier

Verifier verifier.py

Marco Fernandez
"""
import sys
import input_handler


def read_matching(match_file, n):
    try:
        f = open(match_file, "r")
        match_lines = [line.strip() for line in f if line.strip()]
        f.close()
    except:
        print("INVALID\n")
        print("Reason: Output file could not be opened.")
        sys.exit(0)

    if len(match_lines) != n:
        print("INVALID\n")
        print("Reason: Wrong number of matched lines. Did not equal to " + str(n) + " possible matches.")
        sys.exit(0)

    h_to_s = {}
    s_to_h = {}

    for line in match_lines:
        parts = line.split()
        if len(parts) != 2:
            print("INVALID\n")
            print("Reason: Pair did not contain two values on the line.")
            sys.exit(0)

        try:
            h = int(parts[0])
            s = int(parts[1])
        except:
            print("INVALID\n")
            print("Reason: Non-numeric entity IDs.")
            sys.exit(0)

        if h < 1 or h > n or s < 1 or s > n:
            print("INVALID\n")
            print("Reason: ID out of range.")
            sys.exit(0)

        # for duplicate assignments
        if h in h_to_s or s in s_to_h:
            print("INVALID\n")
            print("Reason: Duplicate hospital or student assignment.")
            sys.exit(0)

        h_to_s[h] = s
        s_to_h[s] = h

    return h_to_s, s_to_h


def build_rank_tables(pref_lists):
    # convert preference lists into rank searches
    ranks = []

    for pref in pref_lists:
        r = {}
        idx = 0
        for x in pref:
            r[x] = idx
            idx += 1
        ranks.append(r)

    return ranks


def check_for_blocking_pairs(n, hosp_prefs, stud_prefs, h_to_s, s_to_h):
    hosp_rank = build_rank_tables(hosp_prefs)
    stud_rank = build_rank_tables(stud_prefs)

    # check every possible hospital and student pair
    for h in range(1, n + 1):
        for s in range(1, n + 1):

            if h_to_s[h] == s:  # skip current match
                continue

            current_student = h_to_s[h]
            current_hospital = s_to_h[s]

            # BLOCKING PAIR - CHECK
            if hosp_rank[h - 1][s] < hosp_rank[h - 1][current_student]:
                if stud_rank[s - 1][h] < stud_rank[s - 1][current_hospital]:
                    print("UNSTABLE\n")
                    print("Blocking Pair: (Hospital: " + str(h) + ", Student: " + str(s) + ")\n")
                    return

    print("VALID STABLE")  # Correct output


def main():
    print("The verifier will check the previously generated output.txt file provided by the input file of your choice")
    filename = input("Type the name of the txt file previously used. \n")
    hospitals, students, n = input_handler.read_input_file(filename)

    print("Running verifier ...")
    print("Verifier results: \n")

    match_file = "output.txt"
    hospital_lists = []
    student_lists = []

    for hospital in hospitals.values():
        hospital_lists.append(hospital["preferences"])

    for student in students.values():
        student_lists.append(student["preferences"])

    hospital_match, student_match = read_matching(match_file, n)

    check_for_blocking_pairs(
        n,
        hospital_lists,
        student_lists,
        hospital_match,
        student_match
    )


if __name__ == "__main__":
    main()
