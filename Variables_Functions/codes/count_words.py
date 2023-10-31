def main():
    my_string = input("Enter a string: ")
    result = count_words(my_string)
    print(f"The Number of words in my_string is {result}")

def count_words(my_string):
    list_of_words = []
    for i in my_string.split():
        list_of_words.append(i)
    return len(list_of_words)

main()
