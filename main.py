# 1) Creating a new file in python

# Here you find the class list
with open("students.txt", "w") as file1:
    file1.write("This is the first line of code")
 
# Here you find all of the names' second letter
with open("2nd_Letter.txt", "w") as file2:
    file2.write("This is the first line of code")

# Here you find all of the full names that have more than 12 letters
with open("FullNamesOver12_Letters.txt", "w") as file3:
    file3.write("This is the first line of code")

# The individual scores along the mean and median scores
with open("Scores_Only.txt", "w") as file4:
    file4.write("This is the first line of code")

# 2) Adding a list of names to file
names = [
    "Layla Adebutu Oladunni",
    "Alessandro Baldassari",
    "Marlee Carballo",
    "Tao Carboni Joaqui",
    "Joseph Culmer",
    "Rafael Di Iorio Andrade Ferreira",
    "Maisie Fletcher",
    "Oliver Gerling",
    "Selma Grafstrom",
    "Bram Gunneweg",
    "Bayne Higgins",
    "Lida Mann",
    "Oliver Manning",
    "Aaron Paul Maunders",
    "Letlotlo Mosotho",
    "Amelia Osborne",
    "Benjamin Perry",
    "Tara Rennie",
    "Isabella Sinodinos",
    "Leila Skinner",
    "Sofia Stucchi Dutto",
    "Harry Voke",
    "Jolie White",
    "Ken Wildtrotter"
]
names_str = "\n".join(names)  # Join the names into a single string, with each name on a new line

with open("students.txt", "w") as file1:
    file1.write(names_str +"\n")


# 6) Get the user to add a new name to the file
new_line = input("Enter the First and Last name of the new student joinig the class: ")
with open("students.txt", "a") as file1:
        file1.write(new_line + "\n")


# 5) Print out every full name which is over 13 letters
with open("students.txt") as file1:
    with open("FullNamesOver12_Letters.txt", "w") as file3:
        for line in file1:
            if len(line.strip()) > 12:  
                file3.write(f"{line.strip()}\n")


# 4) Print out the second letter in everyone's name
with open("students.txt") as file1:
    with open("2nd_Letter.txt", "w") as file2:
        for line in file1:
            if len(line) > 1:
                file2.write(line[1] + "\n")


# 7) Add a random test score for each student after a comma (eg. Devonte the 3rd Jr, 21%)
import random
def add_random_score(name):
    score = random.randint(1, 100)
    return f"{name}, {score}%"

with open("students.txt", "r") as file1:
    lines = file1.readlines()

with open("students+test_scores.txt", "w") as file2:
    for line in lines:
        name = line.split(",", 1)[0]  # Extract the name (before the comma)
        updated_line = add_random_score(name.strip())  # Add the random score
        file2.write(updated_line + "\n")

# 8) Output a list of only the scores and find the mean and median
import numpy as np

with open('students+test_scores.txt', 'r') as file:
    data = file.readlines()

scores = []

for entry in data:
    _, score = entry.split(",")  # Ignore the name and extract the score
    score = score.strip().replace('%', '')  # Remove the '%' symbol
    score = int(score)  # Convert score to integer
    scores.append(score)

mean = np.mean(scores)
median = np.median(scores)

with open('Scores_Only.txt', 'w') as file4:
    for score in scores:
        file4.write(f"{score}%\n")

    file4.write(f"\nMean: {mean}%\n")
    file4.write(f"Median: {median}%\n")


# 9) Ask the user for a name and output the score of that person ("If name in line" type code)
new_line = input("Enter a name from this class to see their score: ")
with open("students+test_scores.txt", "r") as file:
    found = False
    for line in file:
        name, score = line.strip().split(",")
        print(f"{name}'s score is: {score}")
        found = True
        break

    if not found:
        print("Name not found in the list.")



# 10) Ask the user for a specific name and delete that whole line
name_to_delete = input("Enter a name to delete from the list: ")

with open("students+test_scores.txt", "r") as file:
    lines = file.readlines()

with open("students_test_scores.txt", "w") as file:
    for line in lines:
        if line.strip().split(",")[0].lower() != name_to_delete.lower():
            file.write(line)

print(f"{name_to_delete} has been deleted from the list (if they existed).")

# 3) Loop through the lines and output each one
with open('students.txt', 'r') as file:
    for line in file:
        print(line.strip())

with open('2nd_Letter.txt', 'r') as file:
    for line in file:
        print(line.strip())

with open('FullNamesOver12_Letters.txt', 'r') as file:
    for line in file:
        print(line.strip())

with open('students+test_scores.txt', 'r') as file:
    for line in file:
        print(line.strip())

with open('Scores_Only.txt', 'r') as file:
    for line in file:
        print(line.strip())