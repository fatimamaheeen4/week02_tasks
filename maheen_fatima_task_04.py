# ============================================================
#  BioSkillz CodeStart — Python Foundations | Batch 01
#  TASK 04: Lists & Tuples (Session 04)
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
# 1) My prediction: [3, 1, 2, 5]
print("--- Ex1.1 ---")
nums = [3, 1, 2]
nums.append(5)
print(nums)

# 2) My prediction: [20, 30]   (index 1 up to, not including, 3)
print("--- Ex1.2 ---")
print([10, 20, 30, 40][1:3])

# 3) My prediction: [1, 2, 3]   (b is the SAME list as a, not a copy)
print("--- Ex1.3 ---")
a = [1, 2]
b = a
b.append(3)
print(a)

# 4) My prediction: None   (sort() changes the list but returns None)
print("--- Ex1.4 ---")
x = [5, 2, 8]
print(x.sort())

# 5) My prediction: <class 'tuple'>   (the comma makes it a tuple)
print("--- Ex1.5 ---")
t = (5,)
print(type(t))

# 6) My prediction: 2   (the outer list holds 2 inner lists)
print("--- Ex1.6 ---")
print(len([[1, 2], [3, 4]]))


# ------------------------------------------------------------
# Exercise 2: Find and fix 4 bugs
# ------------------------------------------------------------
print("--- Ex2 ---")
marks = [72, 95, 64]
marks.append(88)               # BUG 1: append() takes only ONE item; use two append() calls (or extend([88, 50]))
marks.append(50)
print("Last:", marks[-1])      # BUG 2: the list has 5 items, so the last index is 4, not 5; marks[-1] is safest

best = sorted(marks)           # BUG 3: marks.sort() returns None; sorted(marks) returns the new sorted list
print("Sorted:", best)

point = (3, 4)
point = (5, point[1])          # BUG 4: tuples are immutable, so point[0] = 5 fails; build a new tuple instead
print("Point:", point)


# ------------------------------------------------------------
# Exercise 3: To-do list manager
# ------------------------------------------------------------
print("--- Ex3: To-do list manager ---")
tasks = []

while True:
    print("1) Add  2) Remove  3) Show  4) Quit")
    choice = input("Choose: ")

    if choice == "1":
        task = input("Task: ")
        tasks.append(task)
    elif choice == "2":
        task = input("Task to remove: ")
        if task in tasks:
            tasks.remove(task)
        else:
            print("That task is not in the list.")
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks yet.")
        else:
            for number, task in enumerate(tasks, start=1):
                print(f"{number}. {task}")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, enter 1-4.")


# ############################################################
#  PART B: TASKS
# ############################################################

# ------------------------------------------------------------
# Task 1: List explorer
# ------------------------------------------------------------
print("--- Task 1 ---")
parts = input("Enter 5 numbers: ").split()
numbers_list = []
for p in parts:
    numbers_list.append(int(p))

total = sum(numbers_list)
print("Sorted  :", sorted(numbers_list))
print("Sum     :", total)
print("Average :", total / len(numbers_list))
print("Largest :", max(numbers_list))
print("Smallest:", min(numbers_list))


# ------------------------------------------------------------
# Task 2: Predict the output
# ------------------------------------------------------------
# 1) My prediction: [1, 2, 3, 1, 2, 3]   (* repeats the list)
print("--- T2.1 ---")
print([1, 2, 3] * 2)

# 2) My prediction: [4, 9, 7, 1]   (insert at index 1)
print("--- T2.2 ---")
x = [4, 7, 1]
x.insert(1, 9)
print(x)

# 3) My prediction: [1, 2, 3]   (remove() deletes only the FIRST 2)
print("--- T2.3 ---")
y = [1, 2, 2, 3]
y.remove(2)
print(y)

# 4) My prediction: [3, 2, 1]
print("--- T2.4 ---")
print(sorted([3, 1, 2], reverse=True))

# 5) My prediction: 2   (unpacking: a=1, b=2, c=3)
print("--- T2.5 ---")
a, b, c = (1, 2, 3)
print(b)

# 6) My prediction: Code Start
print("--- T2.6 ---")
print(" ".join(["Code", "Start"]))


# ------------------------------------------------------------
# Task 3: Find and fix the bugs
# ------------------------------------------------------------
print("--- Task 3 ---")
names = ["ali", "sara", "omar"]
names.append("zara")                 # BUG 1: lists have no add(); the method is append()

for i in range(len(names)):          # BUG 2: len(names) + 1 goes one index too far (IndexError)
    print(names[i].title())

names.remove("sara")                 # BUG 3: the list holds lowercase "sara"; .title() only changed the printed text, so "Sara" isn't found
print("Total:", len(names))          # BUG 4: missing closing parenthesis


# ------------------------------------------------------------
# Task 4: Remove duplicates (without sets)
# ------------------------------------------------------------
print("--- Task 4 ---")
numbers = [3, 7, 3, 9, 7, 1, 3]
unique = []
for n in numbers:
    if n not in unique:
        unique.append(n)
print(unique)   # [3, 7, 9, 1]


# ------------------------------------------------------------
# Task 5: Your field  (Option A: Codons)
# ------------------------------------------------------------
print("--- Task 5: Codons ---")
dna = input("Enter a DNA sequence (e.g. ATGGCCTAA): ").upper().strip()

codons = []
for i in range(0, len(dna) - len(dna) % 3, 3):   # only complete groups of 3
    codons.append(dna[i:i + 3])

print(codons, "->", len(codons), "codons")
if len(dna) % 3 != 0:
    print("Note: the last", len(dna) % 3, "base(s) were ignored (incomplete codon).")
