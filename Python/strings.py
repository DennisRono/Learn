# Creating and accessing strings
name = "Alice"
greeting = "Hello, " + name + "!"
print(greeting)  # Output: Hello, Alice!

# Slicing strings
first_letter = name[0]  # Access the first letter
last_letter = name[-1]  # Access the last letter
substring = name[1:4]  # Extract characters from index 1 to 3 (excluding 4)

# Formatting strings
age = 30
formatted_message = f"{name} is {age} years old."
print(formatted_message)  # Output: Alice is 30 years old.
