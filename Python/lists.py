# Creating and accessing lists
numbers = [1, 2, 3, 4, 5]
first_number = numbers[0]
last_number = numbers[-1]

# Modifying lists
numbers.append(6)  # Add to the end
numbers.insert(2, 3.5)  # Insert at a specific index

# Removing elements
numbers.remove(3.5)  # Remove the first occurrence of 3.5
del numbers[1]  # Remove the element at index 1

# Iterating over lists
for number in numbers:
    print(number)
