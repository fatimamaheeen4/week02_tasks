# ============================================================
#  BioSkillz CodeStart — Python Foundations | Batch 01
#  TASK 03: Loops (Session 03)
# ============================================================
#
#  Name            : Maheen Fatima
#  GitHub username :
#  Date            : 27 November 2026
# ============================================================


# ############################################################
#  PART A: SESSION EXERCISES (from the slides)
# ############################################################

# ------------------------------------------------------------
# Exercise 1: Predict the output
# ------------------------------------------------------------
# 1) My prediction: Hi 0 / Hi 1 / Hi 2 (three separate lines)
print("--- Ex1.1 ---")
for i in range(3):
    print("Hi", i)

# 2) My prediction: 12   (2 + 4 + 6)
print("--- Ex1.2 ---")
x = 0
for i in range(1, 4):
    x += i * 2
print(x)

# 3) My prediction: 321   (counts down 3, 2, 1 with no spaces)
print("--- Ex1.3 ---")
for i in range(3, 0, -1):
    print(i, end="")
print()

# 4) My prediction: co   (loop stops when it reaches "d")
print("--- Ex1.4 ---")
for ch in "code":
    if ch == "d":
        break
    print(ch, end="")
print()

# 5) My prediction: 1 2 4 5   (0 and 3 are skipped by continue)
print("--- Ex1.5 ---")
for i in range(6):
    if i % 3 == 0:
        continue
    print(i, end=" ")
print()

# 6) My prediction: 2 5 8   (start 2, step 3, stop before 10)
print("--- Ex1.6 ---")
for i in range(2, 10, 3):
    print(i, end=" ")
print()


# ------------------------------------------------------------
# Exercise 2: Find and fix 4 bugs
# ------------------------------------------------------------
print("--- Ex2 ---")
count = 1
while count <= 5:          # BUG 1: missing colon ":" (the only one that gives an error)
    print(count)
    count += 1             # BUG 2: count never changed, so infinite loop; add count += 1

total = 0                  # BUG 3: total = 0 was inside the loop and reset every time; move it before the loop
for i in range(1, 6):      # BUG 4: range(1, 5) stops at 4; use range(1, 6) to include 5
    total += i
print("Sum of 1 to 5:", total)


# ------------------------------------------------------------
# Exercise 3: Number guessing game
# ------------------------------------------------------------
print("--- Ex3: Guessing game ---")
import random

secret = random.randint(1, 10)
tries = 0

while True:
    guess = int(input("Guess (1-10): "))
    tries += 1
    if guess > secret:
        print("Too high")
    elif guess < secret:
        print("Too low")
    else:
        print("Correct! You took", tries, "tries")
        break


# ############################################################
#  PART B: TASKS
# ############################################################

# ------------------------------------------------------------
# Task 1: Multiplication table
# ------------------------------------------------------------
print("--- Task 1 ---")
number = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")


# ------------------------------------------------------------
# Task 2: Predict the output
# ------------------------------------------------------------
# 1) My prediction: 1 4 9
print("--- T2.1 ---")
for i in range(1, 4):
    print(i * i, end=" ")
print()

# 2) My prediction: 18   (0 + 3 + 6 + 9)
print("--- T2.2 ---")
total = 0
for i in range(0, 10, 3):
    total += i
print(total)

# 3) My prediction: 3 / 2 / 1 (separate lines)
print("--- T2.3 ---")
n = 3
while n > 0:
    print(n)
    n -= 1

# 4) My prediction: lp   (both "o" letters are skipped by continue)
print("--- T2.4 ---")
for ch in "loop":
    if ch == "o":
        continue
    print(ch, end="")
print()

# 5) My prediction: 10   (outer loop runs 5 times x inner loop 2 times)
print("--- T2.5 ---")
count = 0
for i in range(5):
    for j in range(2):
        count += 1
print(count)

# 6) My prediction: 5 3 1
print("--- T2.6 ---")
for i in range(5, 0, -2):
    print(i, end=" ")
print()


# ------------------------------------------------------------
# Task 3: Find and fix the bugs
# ------------------------------------------------------------
print("--- Task 3 ---")
total = 0
for i in range(1, 11):          # BUG 1: missing colon; BUG 2: range(1, 10) leaves out 10, so use range(1, 11)
    if i % 2 == 0:              # BUG 3: "=" is assignment; comparison needs "=="
        total += i
print("Sum of even numbers 1-10:", total)

count = 10
while count > 0:
    print(count)
    count -= 1                  # BUG 4: count never decreased, so infinite loop; add count -= 1


# ------------------------------------------------------------
# Task 4: Character counter
# ------------------------------------------------------------
print("--- Task 4 ---")
sentence = input("Sentence: ")
vowels = 0
digits = 0
spaces = 0

for ch in sentence.lower():
    if ch in "aeiou":
        vowels += 1
    elif ch.isdigit():
        digits += 1
    elif ch == " ":
        spaces += 1

print("Vowels:", vowels)
print("Digits:", digits)
print("Spaces:", spaces)


# ------------------------------------------------------------
# Task 5: Your field  (Option A: GC content)
# ------------------------------------------------------------
print("--- Task 5: GC content ---")
dna = input("Enter a DNA sequence (e.g. ATGCGCAT): ").upper().strip()

gc_count = 0
for base in dna:
    if base == "G" or base == "C":
        gc_count += 1

if len(dna) > 0:
    gc_content = gc_count / len(dna) * 100
    print(f"GC content: {gc_content:.1f}%")
else:
    print("No sequence entered.")
