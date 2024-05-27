def is_palindrome(string):
    return string == string[::-1]

result = is_palindrome("radar")
print("Is Palindrome:", result)