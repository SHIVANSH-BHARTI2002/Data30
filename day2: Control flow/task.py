n = int(input("Enter number: "))

# Table using for loop
print("Table of %i using for loop:\n" % n)
for i in range(1, 11):
    print("%i x %i = %i" % (n, i, n * i))

# Table using while loop
print("\nTable of %i using while loop:\n" % n)
i = 1
while True:
    print("%i x %i = %i" % (n, i, n * i))
    i += 1
    if i > 10:
        break
