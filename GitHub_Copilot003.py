

# Create a list variable of 100 numbers
numbers = [i for i in range(100)]

def get_even_numbers(numbers):
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers

# Call the function with the list of numbers
print(get_even_numbers(numbers))

odd_numbers = [i for i in range(100) if i % 2 != 0]
print(odd_numbers)

#==================================================================================================

# Create a list variable of 100 numbers, but only the even numbers.
# numbers = [i for i in range(100) if i % 2 == 0]


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# A list of 5 people. 
people = [
    Person("John", 36),
    Person("Jane", 23),
    Person("Dave", 54),
    Person("Marry", 12),
    Person("Mike", 78)
]


