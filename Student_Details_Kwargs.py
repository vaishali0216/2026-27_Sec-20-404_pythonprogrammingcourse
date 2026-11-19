def student_details(**kwargs):
    print("Student Details:")

    for key, value in kwargs.items():
        print(key, ":", value)


student_details(
    name="Vaishali",
    roll_no=26000404,
    department="CSE",
    college="NRI University"
)