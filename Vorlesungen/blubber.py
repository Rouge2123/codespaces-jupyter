import random
from faker import Faker
from nltk import nltk

# Create an instance of the Faker class
fake = Faker()
print(fake.name())

# List to store student information
students = []

# Generate fake data for 10 students
for _ in range(10):
    student = {
        "name": fake.name(),
        "age": random.randint(18, 25),
        "major": random.choice(["Computer Science", "Mathematics", "Physics"]),
        "gpa": round(random.uniform(2.0, 4.0), 2),
        "is_international": random.choice([True, False])
    }
    students.append(student)

# Accessing and printing student information for student in students:
for student in students:
    full_name = student["name"]
    first_name = full_name.split()[0]
    last_name = full_name.split()[1]
    print(first_name, last_name)
    print("Age:", student["age"])
    print("Major:", student["major"])
    print("GPA:", student["gpa"])
    print("Is International Student:", student["is_international"])
    print()

# Put all first names of students in a list
first_names = []
for student in students:
    full_name = student["name"]
    first_name = full_name.split()[0]
    first_names.append(first_name)

print(first_names)

# Put all first names of students in a set
first_names = set()

# Cache to store already calculated Fibonacci numbers
fibonacci_cache = {}

def fibonacci_of(n):
    # Check if the result is already in the cache
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    
    # Calculate the Fibonacci number
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = fibonacci_of(n-1) + fibonacci_of(n-2)
    
    # Store the result in the cache
    fibonacci_cache[n] = result
    
    return result

print(fibonacci_of(6))
print(fibonacci_cache)