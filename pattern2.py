# Outer loop runs for 5 rows (i goes from 1 to 5)
for i in range(1, 6):
    # Inner loop prints 'i' number of stars in the current row
    for j in range(i):
        print("*", end=" ")
    # Move to the next line after each row
    print()