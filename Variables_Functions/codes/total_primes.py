def main():
    S,E = map(int,input("Enter S and E: ").split())
    print(total_prime(S,E))

def is_prime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

def total_prime(S,E):
    count_primes = 0
    primes = []
    for i in range(S,E+1):
        if is_prime(i):
            count_primes += 1
            primes.append(i)
    print(primes)
    return count_primes

main()