# Write a program to display Pascal’s triangle

n = int(input("Enter the number of rows for Pascal's Triangle:"))

triangle = []
for i in range(n):
    row = []
    for j in range(i + 1):
        if j == 0 or j == i:
            row.append(1) #First and last element of each row is 1
        else:
            # Sum of the two elements directly above
            element = triangle[i - 1][j - 1] + triangle[i - 1][j]
            row.append(element)
    triangle.append(row)


for row in triangle:
    print(''.join(map(str, row)))