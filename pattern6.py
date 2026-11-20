n = 5

# Outer loop runs for each row from 1 to n
for i in range(1, n + 1):
    # Print leading spaces to align stars to the right
    for s in range(n - i):
        print("  ", end="")
    # Print stars for the current row
    for j in range(i):
        print("* ", end="")
    # Move to the next line
    print()
    