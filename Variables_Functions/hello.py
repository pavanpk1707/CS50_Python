# Ask User for their name and Remove whitespace from str and capitalize user's name
name = input("What's Your Name: ").strip().title()

# Say hello to user
print("Hello,",name,sep = " ",end=" ")
print("Good Morning")  

# f-Strings
print(f"Hello, {name}")