def print_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

print_details(
    name="Vaishali",
    age=18,
    course="B.Tech",
    college="NRI University"
)