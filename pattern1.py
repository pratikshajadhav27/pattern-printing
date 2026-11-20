# Outer loop controls the total number of rows (4 rows)
for i in range(4):
    # Inner loop prints 4 stars in each row with a space between them
    for j in range(4):
        print("*", end=" ")
    # Move to the next line after completing one row
    print()