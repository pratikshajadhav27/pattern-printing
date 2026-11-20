n = 5

# start with full width and shrink downwards
for i in range(n, 0, -1):
    # push the row inward with leading spaces
    for s in range(n - i):
        print(" ", end="")
    # print remaining stars for the row
    for j in range(i):
        print("* ", end="")
    print()