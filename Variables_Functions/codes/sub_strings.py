def main():
    my_string = input("Enter String: ")
    print_substrings(my_string)

def print_substrings(my_string):
    substrings = []
    n = len(my_string)
    for start in range(n):
        for end in range(start+1,n+1):
            substring = my_string[start:end]
            substrings.append(substring)
    print(substrings)
main()