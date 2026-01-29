# COP4533-Programming-Assignment-1---Matching-and-Verifying
Employs the Gale Shapely algorithm for a hospital-student matching problem. Has a verifier to check if proposed matching is stable. Includes the Task C graph generation utilizing matplotlib if needed.

Authors:

Alejandro Velez 28126838

Marco Fernandez 96258471

Instructions:
 - Run `git clone https://github.com/alexjvd4/COP4533-Programming-Assignment-1---Matching-and-Verifying.git` in your preferred directory
   
   Task A - Gale Shapely Algorithm Instructions:
    - Sample input .txt files are provided such as `input.txt`, `one-one input.txt`, `empty.txt`
        - Add any input .txt files you would like in the main folder `\COP4533-Programming-Assignment-1---Matching-and-Verifying`
    - Run `python main.py`
    - Provide the input filename
    - The `output.txt` file will be generated in the same folder `\COP4533-Programming-Assignment-1---Matching-and-Verifying` containing the matching results
  
   Task B - Verifier Instructions:
    - Run `python verifier.py`
    - Provide the same input file name used to generate `output.txt` so the correct priority lists can be used
    - The verifier will only use `output.txt` to cross check with the input priority lists
    - The verifier will print `VALID STABLE` if there is a correct matching, `INVALID`, or `UNSTABLE` if the matching is not correct, and will also list the reason (blocking pairs exist).
  
   Task C - Scalability & Graph Instructions (If needs generation):
    - If `matplotlib` is not already installed, run `python -m pip install matplotlib` in the main directory `\COP4533-Programming-Assignment-1---Matching-and-Verifying`
    - Run `python scaling.py`
    - The graph showing the relationship between the Verifier and the Algorithm will be displayed shortly. The screenshot and interpretation are provided below.

In the below graph, you will see that the verifier’s runtime increases much more rapidly than the matching algorithm. As n grows, you can see a steeper curve on the scalability graph. Since the verifier checks all possible hospital and student pairs for blocking pairs, it causes the runtime to grow faster than the matching algorithm’s process.

<img width="788" height="677" alt="Screenshot 2026-01-29 121333" src="https://github.com/user-attachments/assets/98a1cd1c-78ce-4322-ae30-ff5dee28961e" />



