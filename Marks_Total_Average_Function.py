def calculate_total(marks):
    total = sum(marks)
    return total

def calculate_average(total, n):
    average = total / n
    return average

n = int(input("Enter number of subjects: "))

marks = []

for i in range(n):
    mark = float(input("Enter marks: "))
    marks.append(mark)

total = calculate_total(marks)
average = calculate_average(total, n)

print("Total Marks:", total)
print("Average Marks:", average)