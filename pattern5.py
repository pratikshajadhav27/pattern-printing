# Outer loop controls the row number (1 to 5)
for i in range(1, 6):
    # Inner loop repeats the current row number 'i' a total of 'i' times
    for j in range(i):
        print(i, end=" ")
    # Move to the next line after each row
    print()