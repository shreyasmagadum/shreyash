number = input("Enter a number: ")
is_palindrome = True

# Loop through half of the number's length
for i in range(len(number) // 2):
    if number[i] != number[-i - 1]:
        is_palindrome = False
        break

if is_palindrome:
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")
32.
Display
Prime
Numbers
from

1
to
50:
for num in range(1, 51):
    if num > 1:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)
33.
write
a
program
to
display
fibanocci
series
upto
15
using
loops
a, b = 0, 1
print(a)
for _ in range(14):
    print(b)
    a, b = b, a + b
34.
Display
Factorial
of
a
Number
using
Loops:
number = int(input("Enter a number: "))
factorial = 1

for i in range(1, number + 1):
    factorial = factorial * i

print(f"Factorial of {number} is {factorial}.")
35.
Implement
a
program
to
print
the
pattern:
1
1
2
1
2
3
1
2
3
4
1
2
3
4
5
rows = 5

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
36
Write
a
program
to
generate
a
pattern:
1
2
2
3
3
3
4
4
4
4
5
5
5
5
5
rows = 5

for i in range(1, rows + 1):
    for j in range(i):
        print(i, end=" ")
    print()
37.
Write
a
program
to
generate
a
pattern:

rows = 5

for i in range(1, rows + 1):
    for j in range(i):
        print(*, end=" ")
    print()
Python
break
statement
The
break is commonly
used in the
cases
where
we
need
to
break
the
loop
for a given condition.The syntax of the break statement in Python is given below.
Syntax
break;
example
38.
for i in range(1, 10):
    if (i == 6):
        break;
    print(i)
Python
continue
Statement
Python
continue
keyword is used
to
skip
the
remaining
statements
of
the
current
loop and go
to
the
next
iteration.In
Python, loops
repeat
processes
on
their
own in an
efficient
way.However, there
might
be
occasions
when
we
wish
to
leave
the
current
loop
entirely, skip
iteration, or dismiss
the
condition
controlling
the
loop.
Syntax
continue
example
39.
for i in range(1, 10):
    if (i == 3):
        continue;
    print(i)
Creating
Strings:
Strings in Python
can
be
created
using
single
quotes(') or double quotes ("). You can also use triple quotes (''' or """) for multi-line strings.
40.
single_quoted_string = 'Hello, World!'
double_quoted_string = "Hello, Python!"
multi_line_string = '''This is a
                           multi-line
                                    string.'''   
Accessing Characters:
You can access individual characters or substrings of a string using indexing and slicing.
41.
my_string = "Python"

print(my_string[0])  # Output: 'P'
print(my_stri1ng[1])  
print(my_string[2])  
print(my_string[3])  
print(my_string[-1])  # Output: 'n'
print(my_string[2:5])  # Output: 'tho'

String Concatenation:
Strings can be concatenated using the + operator or by using the str.join() me2thod.
42.
str1 = "Hello"
str2 = "World"

concat_string = str1 + ", " + str2
print(concat_string)  # Output: 'Hello, World'

joined_string = "-".join([str1, str2])
print(joined_string)  # Output: 'Hello-World'

String Formatting:
Python provides several ways to format strings, including using the % operator, the str.format() method, and f-strings (formatted string literals).
43.
name = "Alice"
age = 30

formatted_string = f"Name: {name}, Age: {age}"
print(formatted_string)  # Output: 'Name: Alice, Age: 30'

String Methods:
The str class provides numerous methods for manipulating strings, such as upper(), lower(), replace(), split(), strip(), find(), startswith(), endswith(), and many mo4.re..
44.
my_string = "   Hello, World!   "

print(my_string.upper())  # Output: '   HELLO, WORLD!   '
print(my_string.strip())  # Output: 'Hello, World!'

words = my_string.split(",")
print(words)  # Output: ['   Hello', ' World!   ']

Conversion:
str.capitalize(): Returns a copy of the string with the first character capitalized.
str.lower(): Returns a copy of the string converted to lowercase.
str.upper(): Returns a copy of the string converted to uppercase.
str.title(): Returns a titlecased version of the string (each word's first letter capitalized).
str.swapcase(): Returns a copy of the string with uppercase characters converted to lowercase and vice versa.
str.casefold(): Returns a lowercase version of the string suitable for case-insensitive comparisons.
Checking and Manipulating Content:
str.isalnum(): Returns True if all characters in the string are alphanumeric.
str.isalpha(): Returns True if all characters in the string are alphabetic.
str.isnumeric(): Returns True if all characters in the string are numeric.
str.isdigit(): Returns True if all characters in the string are digits.
str.islower(): Returns True if all characters in the string are lowercase.
str.isupper(): Returns True if all characters in the string are uppercase.
str.isspace(): Returns True if all characters in the string are whitespace.
str.strip(): Returns a copy of the string with leading and trailing whitespace removed.
str.rstrip(): Returns a copy of the string with trailing whitespace removed.
str.lstrip(): Returns a copy of the string with leading whitespace removed.
str.replace(old, new): Returns a copy of the string with occurrences of 'old' replaced by 'new'.
str.split(separator): Returns a list of substrings separated by 'separator'.
str.join(iterable): Joins elements of an iterable (like a list) with the string as a separator.
Finding and Checking Substrings:
str.startswith(prefix): Returns True if the string starts with 'prefix'.
str.endswith(suffix): Returns True if the string ends with 'suffix'.
str.find(substring): Returns the lowest index of 'substring' in the string (-1 if not found).
str.rfind(substring): Returns the highest index of 'substring' in the string (-1 if not found).
str.count(substring): Returns the number of non-overlapping occurrences of 'substring' in the string.
Character Manipulation:
str.strip(chars): Returns a copy of the string with leading and trailing characters in 'chars' removed.
str.lstrip(chars): Returns a copy of the string with leading characters in 'chars' removed.
str.rstrip(chars): Returns a copy of the string with trailing characters in 'chars' removed.
Formatting and Padding:
str.format(*args, **kwargs): Formats the string with placeholders.
str.ljust(width): Returns a left-justified version of the string in a field of given width.
str.rjust(width): Returns a right-justified version of the string in a field of given width.
str.center(width): Returns a centered version of the string in a field of given width.
str.zfill(width): Returns a copy of the string left-padded with zeros to a total width of 'width'.
Encoding and Decoding:
str.encode(encoding): Returns the encoded version of the string using the specified encoding.
str.decode(encoding): Returns the decoded version of the string using the specified encoding.
Miscellaneous:
str.len(): Returns the length of the string.
str.join(iterable): Joins elements of an iterable (like a list) with the string as a separator.
str.maketrans(x, y): Returns a translation table mapping characters in 'x' to characters in 'y'.
str.translate(translation_table): Translates the string using a translation table.
Lists:
Lists are ordered, mutable (modifiable), and can contain elements of differe55nt data types.
45.# Create a list
my_list = [1, 2, 3, 'apple', 'banana', True]

# Access elements
print(my_list[0])  # Output: 1
print(my_list[-1])  # Output: True

# Modify elements
my_list[3] = 'cherry'
print(my_list)  # Output: [1, 2, 3, 'cherry', 'banana', True]

# Append and remove elements
my_list.append('orange')
print(my_list)  # Output: [1, 2, 3, 'cherry', 'banana', True, 'orange']

my_list.remove('banana')
print(my_list)  # Output: [1, 2, 3, 'cherry', True, 'orange']
Tuples:
Tuples are ordered, immutable (unchangeable), and can contain elements of different d6.6ata types.
46.
# Create a tuple
my_tuple = (1, 2, 3, 'apple', 'banana')

# Access elements
print(my_tuple[0])  # Output: 1
print(my_tuple[-1])  # Output: 'banana'

# Cannot modify elements
# my_tuple[3] = 'cherry'  # This will raise a TypeError

# Concatenate tuples
new_tuple = my_tuple + ('cherry', 'orange')
print(new_tuple)  # Output: (1, 2, 3, 'apple', 'banana', 'cherry', 'orange')
Sets:
Sets are unordered, mutable (modifiable), and contain unique elements 7(no duplicates).
47.
# Create a set
my_set = {1, 2, 3, 'apple', 'banana', 'apple'}

# Access elements (Note: Sets are unordered, so indexing is not supported)
# print(my_set[0])  # This will raise a TypeError

# Add and remove elements
my_set.add('cherry')
print(my_set)  # Output: {1, 2, 3, 'cherry', 'banana', 'apple'}

my_set.remove('banana')
print(my_set)  # Output: {1, 2, 3, 'cherry', 'apple'}

# Set operations
set1 = {1, 2, 3}
set2 = {2, 3, 4}

print(set1.union(set2))  # Output: {1, 2, 3, 4}
print(set1.intersection(set2))  # Output: {2, 3}
Dictionaries:
Dictionaries are unordered, mutable (modifiable), and store data in key-value pairs (keys mu8st be unique)..
48.
[
Built-in Math Functions:
Python provides several built-in math functions that can be used without importing any module. Here are some of the commonly used ones:
1.abs(x): Returns the absolute value of a number x.
49.
num = -5
abs_num = abs(num)
print(abs_num)  # Output: 5

2.max(iterable): Returns the maximum value from an iterable
50.
numbers = [3, 7, 2, 9, 5]
max_num = max(numbers)
print(max_num)  # Output: 9
3.min(iterable): Returns the minimum value from an iterable.
51.
numbers = [3, 7, 2, 9, 5]
min_num = min(numbers)
print(min_num)  # Output: 2
4.pow(x, y): Returns x raised to the power of y.
52.
result = pow(2, 3)
print(result)  # Output: 8
5.round(x, n): Rounds the number x to n decimal places.
53.
num = 3.14159
rounded_num = round(num, 2)
print(rounded_num)  # Output: 3.14
The Math Module:
The math module in Python provides more advanced mathematical functions and constants. To use functions from 
the math module, you need to import it first:
import math
1.math.sqrt(x): Returns the square root of x.
54.
import math

result = math.sqrt(25)
print(result)  # Output: 5.0
2.math.factorial(x): Returns the factorial of x.
55.
import math

result = math.factorial(5)
print(result)  # Output: 120
3.math.sin(x), math.cos(x), math.tan(x): Returns the sine, cosine, and tangent of an angle in radians.
56.
import math

angle = math.pi / 4
sin_val = math.sin(angle)
cos_val = math.cos(angle)
tan_val = math.tan(angle)

print(sin_val, cos_val, tan_val) 
4.math.log(x, base): Returns the logarithm of x with the specified base.
57.
import math

result = math.log(100, 10)
print(result)  # Output: 2.0
5.math.pi, math.e: Constants representing π and Euler's number (e).
58.
import math

print(math.pi)  # Output: 3.141592653589793
print(math.e)   # Output: 2.718281828459045
Modules
A function or Modules is a block of code which only runs when it is called.You can pass data, known as parameters, into a function.A function can return data as a result.
Simplification: A module often concentrates on one comparatively small area of the overall problem instead of the full task. We will have a more manageable design problem to think about if we are only concentrating on one module. Program development is now simpler and much less vulnerable to mistakes.
Flexibility: Modules are frequently used to establish conceptual separations between various problem areas. It is less likely that changes to one module would influence other portions of the program if modules are constructed in a fashion that reduces interconnectedness. (We might even be capable of editing a module despite being familiar with the program beyond it.) It increases the likelihood that a group of numerous developers will be able to collaborate on a big project.
Reusability: Functions created in a particular module may be readily accessed by different sections of the assignment (through a suitably established api). As a result, duplicate code is no longer necessary.
Scope: Modules often declare a distinct namespace to prevent identifier clashes in various parts of a program.
Creating a Module:
Save the following code in a file named mymodule.py.
59.
def greet(name):
    print(f"Hello, {name}!")
greet("Alice")
Using the Module:
Import the module using the import statement in another Python script. main.py
60.
import mymodule as mm

mm.greet("Bob")
61.Display "Hello, World!" using a method:
def say_hello():
    print("Hello, World!")

say_hello()
62.Calculate the square of a number using a method:
def square(num):
    return num ** 2

result = square(5)
print("Square:", result)
63.Calculate the sum of two numbers using a method:
def add_numbers(a, b):
    return a + b

result = add_numbers(3, 7)
print("Sum:", result)
64.Calculate the factorial of a number using a recursive method:
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

result = factorial(5)
print("Factorial:", result)
65.Check if a given string is a palindrome using a method:
def is_palindrome(string):
    return string == string[::-1]

result = is_palindrome("radar")
print("Is Palindrome:", result)
66.Generate the Fibonacci series up to a given number of terms using a method:
def is_palindrome(string):
def fibonacci(n):
    fib_series = [0, 1]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series

result = fibonacci(10)
print("Fibonacci Series:", result)
67.Sort an array of integers in ascending order using a method:
def sort_array(arr):
    return sorted(arr)

numbers = [3, 6, 1, 9, 4, 8]
sorted_numbers = sort_array(numbers)
print("Sorted Array:", sorted_numbers)
68.Reverse a given string using a method:
def reverse_string(string):
    return string[::-1]

result = reverse_string("Hello, World!")
print("Reversed String:", result)
69.Reverse a given number using a method:
def reverse_number(num):
    return int(str(num)[::-1])

result = reverse_number(12345)
print("Reversed Number:", result)
70.Return multiple values (minimum and maximum) using a method:
def min_max(arr):
    return min(arr), max(arr)

numbers = [3, 6, 1, 9, 4, 8]
min_val, max_val = min_max(numbers)
print("Minimum Value:", min_val)
print("Maximum Value:", max_val)
71.Check Even or Odd:
def is_even(num):
    return num % 2 == 0

print(is_even(4))
print(is_even(7))
72.Sum of List:
def is_even(num):
    return num % 2 == 0

print(is_even(4))
print(is_even(7))
73.Check Prime Number:
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

print(is_prime(29))
74.Convert Celsius to Fahrenheit:
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

print(celsius_to_fahrenheit(0))
74.Generate Multiplication Table:
def multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

multiplication_table(5)
75.Merge Two Lists:
def merge_lists(lst1, lst2):
    return lst1 + lst2

print(merge_lists([1, 2, 3], [4, 5, 6]))
75.Merge Two Lists:
def merge_lists(lst1, lst2):
    return lst1 + lst2

print(merge_lists([1, 2, 3], [4, 5, 6]))
76.Check Substring::
def is_substring(s1, s2):
    return s1 in s2

print(is_substring("hello", "hello world"))
Built-in Modules:
Python comes with several built-in modules that provide various functionalities.
77.math Module:
import math

print(math.sqrt(16))  # Output: 4.0
78.random Module:
import random

print(random.randint(1, 10))  # Output: Random integer between 1 and 10

79.datetime Module:
import datetime

current_date = datetime.date.today()
print(current_date)  # Output: Today's date in yyyy-mm-dd format
80.os Module:
import os

print(os.getcwd())  # Output: Current working directory
Exception handling
Exception handling in Python allows you to gracefully manage and respond to runtime errors and exceptional situations that may occur during program execution. It involves using try, except, else, and finally blocks to handle exceptions and prevent your program from crashing.
81.Basic Syntax:
try:
    result = 10 / 0  # Division by zero
except ZeroDivisionError as e:
    print(f"Error: Division by zero - {e}")
else:
    print("No error occurred.")
finally:
    print("Finally block executed.")
82.Multiple Except Blocks:
try:
    num = int(input("Enter a number: "))
    result = 10 / num  # Division by user input
except ZeroDivisionError:
    print("Error: Division by zero")
except ValueError:
    print("Error: Invalid input. Please enter a number.")
else:
    print("No error occurred.")
finally:
    print("Finally block executed.")
83.Raising Custom Exceptions:
try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative.")
except ValueError as e:
    print(f"Error: {e}")
else:
    print("No error occurred.")
finally:
    print("Finally block executed.")
Object-Oriented Programming (OOP)
Object-Oriented Programming (OOP) is a programming paradigm that uses objects and classes to model real-world entities and their interactions. In Python, OOP allows you to create reusable and modular code by organizing data and functions into objects. Let's dive into OOP concepts in Python with examples.
84.Class Definition:
A class is a blueprint for creating objects. It defines attributes (variables) and methods (functions) that all objects of the class will have.
The __init__ method is a special method called when an object is instantiated from a class. It initializes the object's attributes.
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.brand} {self.model} ({self.year})")

    def start_engine(self):
        print("Engine started.")
84.Object Creation:
Objects are instances of a class. You can create multiple objects from the same class, each with its own set of attributes and methods.
car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 2018)

car1.display_info()  # Output: Toyota Camry (2020)
car2.display_info()  # Output: Honda Civic (2018)

car1.start_engine()  # Output: Engine started.

85.Class Methods and Instance Methods:
Class methods are defined using @classmethod decorator and take the class itself (cls) as the first parameter.
Instance methods take the instance (self) as the first parameter and can access instance attributes and perform actions on them.
class Circle:
    pi = 3.14  # Class attribute

    def __init__(self, radius):
        self.radius = radius  # Instance attribute

    @classmethod
    def set_pi(cls, new_pi):
        cls.pi = new_pi

    def calculate_area(self):
        return self.pi * (self.radius ** 2)

Circle.set_pi(3.14159)

circle1 = Circle(5)
print(circle1.calculate_area())  # Output: 78.53975
86.Inheritance:
Inheritance allows one class (subclass) to inherit attributes and methods from another class (superclass). It promotes code reuse and supports the "is-a" relationship.
Polymorphism:
Polymorphism allows objects to take on multiple forms, enabling different classes to be treated as instances of a common superclass. It promotes code reusability and flexibility.
class Animal:

    def pp(self):
        print("i am super class")                         
    def speak(self):
        pass  # Abstract method

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

dog = Dog()
cat = Cat()
dog.pp()
cat.pp()
print(dog.speak())  # Output: Woof!
print(cat.speak())  # Output: Meow!
87.Define a class "Person" with attributes such as name, age, and address print the values of different objects.
class Person:
88.Implement a class "Student" with attributes for name, roll number, and marks print the values of different objects.

class Student:
89.Create a class "Rectangle" with methods to calculate area and perimeter print the values of different objects.
File Handling
The key function for working with files in Python is the open() function.The open() function takes two parameters; filename, and mode.There are four different methods (modes) for opening a file:
"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists
In addition you can specify if the file should be handled as binary or text mode
"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)
81.Opening a File:
You can open a file using the open() function. The syntax is:
Writing to a File:
Writing Example with 'with':
file = open('sample.txt', 'w')
file.write('Hello, World!\n')
file.write('This is a new line.')
file.close()

with open('sample.txt', 'w') as file:
    file.write('with Hello, World!\n')
    file.write('with This is a new line.')
82.Reading from a File:
Reading Entire File:
Reading Line by Line:
Reading Example with 'with':
#Reading Entire File:
file = open('sample.txt', 'r')
content = file.read()
print(content)
file.close()

print()

#Reading Line by Line:
file = open('sample.txt', 'r')
for line in file:
    print(line.strip())
    print()# strip() removes trailing newline characters
file.close()

#using with
with open('sample.txt', 'r') as file:
    content = file.read()
    print(content)
82.Appending to a File:
#Reading Entire File:
file = open('sample.txt', 'r')
content = file.read()
print(content)
file.close()

print()

#Reading Line by Line:
file = open('sample.txt', 'r')
for line in file:
    print(line.strip())
    print()# strip() removes trailing newline characters
file.close()

#using with
with open('sample.txt', 'r') as file:
    content = file.read()
    print(content)
