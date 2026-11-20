# Outer loop starts from 5 and decreases down to 1
for i in range(5, 0, -1):
    # Inner loop prints 'i' stars for the current row
    for j in range(i):
        print("*", end=" ")
    # Move to the next line after each row
    print()