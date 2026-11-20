n = 5

# Outer loop controls the rows from 1 to n
for i in range(1, n + 1):
    # Print leading spaces to center the pyramid
    for s in range(n - i):
        print(" ", end="")
    # Print 'i' stars separated by a space to form a centered pyramid
    for j in range(i):
        print("* ", end="")
    # Move to the next line
    print()