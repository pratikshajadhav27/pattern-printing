# Outer loop controls the number of rows (1 to 5)
for i in range(1, 6):
    # Inner loop prints numbers starting from 1 up to current row number 'i'
    for j in range(1, i + 1):
        print(j, end=" ")
    # Move to the next line after each row
    print()