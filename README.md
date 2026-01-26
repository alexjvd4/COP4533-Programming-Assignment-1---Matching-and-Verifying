# COP4533-Programming-Assignment-1---Matching-and-Verifying
Employs the Gale Shaply algorithm for a hospital-student matching problem. Has a verifier to check if proposed matching is stable.

Authors:
Alejandro Velez 28126838
Marco Fernandez 96258471


Instructions:
 - Run `git clone https://github.com/alexjvd4/COP4533-Programming-Assignment-1---Matching-and-Verifying.git` in your preferred directory
 - Sample input .txt files are provided such as `input.txt`, `one-one input.txt`, `empty.txt`
     - Add any input .txt files you would like in the main folder `\COP4533-Programming-Assignment-1---Matching-and-Verifying`
 - Run `python main.py` to start the program and begin the algorithm
 - The `output.txt` file will be generated in the same folder `\COP4533-Programming-Assignment-1---Matching-and-Verifying` containing the matching results

Input/Output Format: 
 -  Input will start with an integer n, corresponding to the number of hospitals and students. The next n lines are used to list hospital preferences, then are followed with n lines that list the student preferences. Each line will end up being a permutation of the numbers 1 throught whatever n is.
     - The matching algorithm will output n lines, one per hospital, in the "i j" format. i and j entail that          hospital i is matched with student j.
     - The verifier will print "VALID STABLE" if there is a correct matching, "INVALID", or "UNSTABLE" if the             matching is not correct, and will also list the reason (blocking pairs exist).

Task B - How to Run the Verifier and Assumptions:
 - According to assignment guidelines, the verifier (a) Checks validity: each hospital and each student is matched to exactly one partner, with no duplicates. And (b) checks stability: confirms there is no blocking pair.
 - With that being said, in order to run the verifier, provide the preference input file and the matching output to the verifier. After analyzing, the verifier will report whether it is "VALID STABLE", "INVALID", or "UNSTABLE".
     - ASSUMPTIONS:
       - n hospitals is equal to n students
       - Preference lists do not contain duplicate entries
       - Hospital/Student index ranges from 1 to n.
      
Task C - Graph & Solution:
(still need to do)
