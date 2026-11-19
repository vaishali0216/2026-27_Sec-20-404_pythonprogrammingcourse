def simple_interest(p, r=5, t=2):
    si = (p * r * t) / 100
    return si

p = float(input("Enter principal amount: "))

si = simple_interest(p)

print("Principal Amount:", p)
print("Rate of Interest: 5%")
print("Time Period: 2 years")
print("Simple Interest:", si)