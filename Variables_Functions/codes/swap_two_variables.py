def swap(a,b):
    a,b = b,a
    return a,b
a = int(input("Enter a: "))
b = int(input("Enter b: "))
a,b = swap(a,b)
print(f"a is {a}")
print(f"b is {b}")