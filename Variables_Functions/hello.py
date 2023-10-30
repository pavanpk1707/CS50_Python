# Ask User for their name and Remove whitespace from str and capitalize user's name
name = input("What's Your Name: ").strip().title()

# Say hello to user
print("Hello,",name,sep = " ",end=" ")
print("Good Morning")  


# Split user's name into first name and last name
first_name,last_name = name.split()

# f-Strings
print(f"Hello your last name is, {last_name}")
