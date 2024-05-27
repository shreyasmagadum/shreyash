year_to_check = 2024

if (year_to_check % 4 == 0 and year_to_check % 100 != 0) or (year_to_check % 400 == 0):
    print(f"{year_to_check} is a leap year.")
else:
    print(f"{year_to_check} is not a leap year.")