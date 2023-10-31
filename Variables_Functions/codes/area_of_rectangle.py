# Take User input of length and breadth
def area(length,breadth):
    return length*breadth
length, breadth = map(int,input().split())
result = area(length,breadth)
print(f"Area of Rectangle of length {length} and breadth {breadth} is {result}")
