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