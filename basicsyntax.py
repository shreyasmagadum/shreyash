try:
    result = 10 / 0  # Division by zero
except ZeroDivisionError as e:
    print(f"Error: Division by zero - {e}")
else:
    print("No error occurred.")
finally:
    print("Finally block executed.")