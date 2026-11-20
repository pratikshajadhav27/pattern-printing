n = 5

# top half of the diamond (1, 3, 5, 7, 9 stars)
for i in range(1, n + 1):
    # leading spaces so the odd-star rows stay centered
    for s in range(2 * (n - i + 1)):
        print(" ", end="")
    # print 2*i - 1 stars with a space after each
    for j in range(2 * i - 1):
        print("*", end=" ")
    print()

# bottom half of the diamond (7, 5, 3, 1 stars)
for i in range(n - 1, 0, -1):
    # increase leading spaces as stars decrease
    for s in range(2 * (n - i + 1)):
        print(" ", end="")
    # print remaining stars for the lower half
    for j in range(2 * i - 1):
        print("*", end=" ")
    print()