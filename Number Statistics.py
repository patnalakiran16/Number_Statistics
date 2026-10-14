# Number Statistics

numbers = [12, 7, 24, 15, 8, 31, 42, 19, 6, 11]

even_numbers = []
odd_numbers = []

# Separate even and odd numbers
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

# Find the largest and smallest numbers
largest_number = max(numbers)
smallest_number = min(numbers)

# Print the results
print("Numbers:", numbers)
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
print("Largest number:", largest_number)
print("Smallest number:", smallest_number)
