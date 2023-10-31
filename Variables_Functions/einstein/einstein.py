def mass(m):
    c = 300000000
    e = m*c**2
    return e

m = int(input("Enter m: "))
result = mass(m)
print(result)