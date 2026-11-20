rows = 5
cols = 5

# loop through each row of the square
for i in range(rows):
    # loop through each column in the current row
    for j in range(cols):
        # print stars only along the outer border of the square
        if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
            print("*", end=" ")
        else:
            # two spaces keep the inner columns aligned while leaving the center hollow
            print("  ", end="")
    # move to the next line after finishing a row
    print()