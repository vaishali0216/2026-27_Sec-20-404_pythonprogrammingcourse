rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

A = []
B = []

print("Enter elements of Matrix A:")
for i in range(rows):
    row = []
    for j in range(cols):
        value = int(input("Enter element: "))
        row.append(value)
    A.append(row)

print("Enter elements of Matrix B:")
for i in range(rows):
    row = []
    for j in range(cols):
        value = int(input("Enter element: "))
        row.append(value)
    B.append(row)

addition = []
subtraction = []
multiplication = []

for i in range(rows):
    add_row = []
    sub_row = []
    mul_row = []

    for j in range(cols):
        add_row.append(A[i][j] + B[i][j])
        sub_row.append(A[i][j] - B[i][j])

    addition.append(add_row)
    subtraction.append(sub_row)

for i in range(rows):
    mul_row = []
    for j in range(cols):
        total = 0
        for k in range(cols):
            total = total + A[i][k] * B[k][j]
        mul_row.append(total)
    multiplication.append(mul_row)

print("Matrix A:", A)
print("Matrix B:", B)
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)