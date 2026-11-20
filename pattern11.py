n = 5

# outer loop for each row from 1 to n
for i in range(1, n + 1):
    # inner loop runs up to the current row number 'i'
    for j in range(1, i + 1):
        # star on the first column, diagonal edge (j == i), and bottom row
        if j == 1 or j == i or i == n:
            print("*", end=" ")
        else:
            # extra spaces inside keep the triangle hollow
            print("  ", end="")
    # move to the next line after each row
    print()