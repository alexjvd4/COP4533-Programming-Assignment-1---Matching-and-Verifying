# Marco Fernandez
import random
import time
import verifier
import matplotlib.pyplot as plt

def generate_preferences(n):
    prefs = []
    for _ in range(n):
        arr = list(range(1, n + 1))
        random.shuffle(arr)
        prefs.append(arr)
    return prefs

def run_matching(hosp_prefs, stud_prefs):
    n = len(hosp_prefs)
    h_to_s = {i + 1: None for i in range(n)}
    s_to_h = {i + 1: None for i in range(n)}
    next_proposal = {i + 1: 0 for i in range(n)}
    free_hospitals = list(range(1, n + 1))

    while free_hospitals:
        h = free_hospitals.pop(0)
        if next_proposal[h] >= n:
            continue

        s = hosp_prefs[h - 1][next_proposal[h]]
        next_proposal[h] += 1

        if s_to_h[s] is None:
            h_to_s[h] = s
            s_to_h[s] = h
        else:
            current_h = s_to_h[s]
            if stud_prefs[s - 1].index(h) < stud_prefs[s - 1].index(current_h):
                h_to_s[current_h] = None
                free_hospitals.append(current_h)

                h_to_s[h] = s
                s_to_h[s] = h
            else:
                free_hospitals.append(h)

    return h_to_s, s_to_h

# assignment value parameters
sizes = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

match_times = []
verify_times = []

for n in sizes:
    hosp_prefs = generate_preferences(n)
    stud_prefs = generate_preferences(n)
    start = time.perf_counter()
    h_to_s, s_to_h = run_matching(hosp_prefs, stud_prefs)
    end = time.perf_counter()
    match_times.append(end - start)
    start = time.perf_counter()
    verifier.check_for_blocking_pairs(
        n,
        hosp_prefs,
        stud_prefs,
        h_to_s,
        s_to_h
        )
    end = time.perf_counter()
    verify_times.append(end - start)

plt.plot(sizes, match_times, marker='o', label="Matching Algorithm")
plt.plot(sizes, verify_times, marker='o', label="Verifier")

plt.xlabel("n (number of hospitals/students)")
plt.ylabel("Runtime (seconds)")
plt.title("Scalability of Matching and Verifier Algorithms")
plt.legend()
plt.grid(True)
plt.show()
