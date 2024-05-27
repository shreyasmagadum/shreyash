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