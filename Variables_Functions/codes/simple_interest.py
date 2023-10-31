def main():
    principal_amount = int(input("Enter principal amount: "))
    interest = float(input("Enter Interest Rate: "))
    time_period = int(input("Enter Time Period: "))
    result = Simple_Interest(principal_amount,interest,time_period)
    print(f"Simple Interest is {result}")

def Simple_Interest(amount,interest,time_period):
    interest = float((amount * interest * time_period)/100)
    return f"{interest:.2f}"

main()