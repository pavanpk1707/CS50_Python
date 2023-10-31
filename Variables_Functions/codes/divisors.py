def divisors(number):
    divisors = []
    for i in range(1,number+1):
        if (number % i == 0):
            divisors.append(i)
    return divisors


number = int(input("Enter a number: "))
result = divisors(number)

print(f"The divisors of {number} are {' '.join(map(str,result))}")
   
