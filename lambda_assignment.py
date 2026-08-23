# Lambda Functions and Functional Programming Assignment

# 1. Lambda Functions

# a) Double a given number
double = lambda x: x * 2
print("Double:", double(10))


# b) Find the remainder when one number is divided by another
remainder = lambda x, y: x % y
print("Remainder:", remainder(17, 5))


# c) Check whether a number is divisible by 5
divisible_by_5 = lambda x: x % 5 == 0
print("Divisible by 5:", divisible_by_5(25))


# d) Find the smaller of two numbers
smaller = lambda x, y: x if x < y else y
print("Smaller number:", smaller(15, 8))


# e) Convert Celsius into Fahrenheit
celsius_to_fahrenheit = lambda c: (c * 9 / 5) + 32
print("Fahrenheit:", celsius_to_fahrenheit(25))


# 2. Using map() and lambda

# a) Add 5 to every number
numbers = [10, 20, 30, 40, 50]

added_numbers = list(map(lambda x: x + 5, numbers))

print("After adding 5:", added_numbers)


# b) Convert all names to uppercase
names = ["aparna", "ravi", "priya", "kiran"]

uppercase_names = list(map(lambda name: name.upper(), names))

print("Uppercase names:", uppercase_names)


# 3. Using filter() and lambda

# a) Find ages 18 and above
ages = [12, 18, 25, 15, 30, 10, 22]

adult_ages = list(filter(lambda age: age >= 18, ages))

print("Ages 18 and above:", adult_ages)


# b) Find names having more than 4 characters
names = ["Ram", "Aparna", "Ravi", "Priyanka", "Sai"]

long_names = list(filter(lambda name: len(name) > 4, names))

print("Names with more than 4 characters:", long_names)


# 4. Using sorted() and lambda

students = [
    ("Aparna", 85),
    ("Ravi", 72),
    ("Priya", 95),
    ("Kiran", 65)
]

sorted_students = sorted(
    students,
    key=lambda student: student[1],
    reverse=True
)

print("Students sorted by marks:")
print(sorted_students)
