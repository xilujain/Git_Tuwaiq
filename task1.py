# number of rows
rows = 5

# print stars
for i in range(rows+1):
    for j in range(i):
        print("*", end=" ")
    print(" ")
# print stars reverse
for i in range(rows-1, 0, -1):
    for j in range(1, i+1):
        print("*", end=" ")
    print(" ")

# print new line
print(" ")

#print stars in one loop
i = 1
while i <= rows:
    j = 1
    while j <= i:
        print("*", end=" ")
        j = j + 1
    i = i + 1
    print(" ")