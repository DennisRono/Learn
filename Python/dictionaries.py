# Creating and accessing dictionaries
person = {'name': 'Bob', 'age': 30, 'city': 'New York'}
name = person['name']
age = person.get('age')  # Safer way to access, returns None if key not found

# Adding and removing items
person['occupation'] = 'Software Engineer'
del person['city']

# Iterating over key-value pairs
for key, value in person.items():
    print(f"{key}: {value}")
