def main():
    hello()
    name = input("What's your name? ")
    hello(name)
    age = int(input("Enter Age: "))
    days = number_of_days(age)
    print(f"Number of days lived {days}")

def number_of_days(age):
    days = age*365
    return days

def hello(name = "Pk"):
    print(f"Hello {name}")

main()
