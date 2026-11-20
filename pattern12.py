n = 5

# top half of the butterfly
for i in range(1, n + 1):
    # left wing stars with space after each
    for j in range(i):
        print("*", end=" ")
    # spaces in the middle shrink as wings grow outward
    for s in range(4 * (n - i)):
        print(" ", end="")
    # right wing stars
    for j in range(i):
        print("*", end=" ")
    print()

# bottom half of the butterfly (4 rows so the middle row isn't doubled)
for i in range(n - 1, 0, -1):
    # left wing stars
    for j in range(i):
        print("*", end=" ")
    # middle spaces grow back as wings narrow down
    for s in range(4 * (n - i)):
        print(" ", end="")
    # right wing stars
    for j in range(i):
        print("*", end=" ")
    print()