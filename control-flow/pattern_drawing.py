size = int(input("Enter the size of the pattern:"))

counter = 1

while counter <= size:
    for num in range(1, size + 1):
        print("*",end="")
    print("\n")
    counter += 1