# Import library "statistics" that adds functions statistics.mean and statistics.median
import statistics as stat

# Define List = "ls" and variable A
ls = []
A = 0

# Adds input to list. Stops if input = 0
while True:
    A = int(input("Enter a number:"))
    if A == 0:
        break  # Stops the loop if value of A is 0 (zero)
    else:
        ls.append(A)  # adds value of A to list "ls"

    ls.sort()  # Sorts list

print("Average :", round(stat.mean(ls), 2))  # Print mean

print("Median :", round(stat.median(ls), 2))  # Print median

ls.sort(reverse=True)  # Sorts in descending order, then prints
print("Descending :", *ls)
