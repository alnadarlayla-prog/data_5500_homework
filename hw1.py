import random

# ---------------------------------------------------------------
# Programming Activity 1
# Add up 1/2 + 1/4 + 1/8 + ... for 1000 iterations
# ---------------------------------------------------------------
denominator = 1      # variable for the denominator
total = 0            # variable to track the sum

for i in range(1, 1001):           # starts at 1, goes to 1000
    denominator = denominator * 2  # 2, 4, 8, 16, 32, ...
    total = total + 1 / denominator

print("Activity 1:", total)


# ---------------------------------------------------------------
# Programming Activity 2
# List of 3 favorite colors, loop through and print each
# ---------------------------------------------------------------
colors = ["blue", "green", "purple"]   # replace with your own favorites

print("Activity 2:")
for color in colors:
    print(color)


# ---------------------------------------------------------------
# Programming Activity 3
# Nested loop: print each color, then each character in the color
# ---------------------------------------------------------------
print("Activity 3:")
for color in colors:
    print(color)                # outer loop: one color at a time
    for character in color:
        print(character)        # inner loop: one character at a time


# ---------------------------------------------------------------
# Programming Activity 4
# List of 10 random integers using append() and random.randint()
# ---------------------------------------------------------------
numbers = []                                # empty list

for i in range(10):                         # loop 10 times
    numbers.append(random.randint(1, 100))  # add a random integer from 1 to 100

print("Activity 4:", numbers)


# ---------------------------------------------------------------
# Programming Activity 5
# Using the list from Activity 4, print any two even numbers in a row
# ---------------------------------------------------------------
print("Activity 5:")
for count in range(len(numbers) - 1):   # stop one early so count+1 stays in range
    if numbers[count] % 2 == 0 and numbers[count + 1] % 2 == 0:
        print(numbers[count], numbers[count + 1])


# ---------------------------------------------------------------
# Programming Activity 6
# List of all even numbers from 2 to 100 using list comprehension
# ---------------------------------------------------------------
evens = [n for n in range(2, 101) if n % 2 == 0]

print("Activity 6:", evens)


# ---------------------------------------------------------------
# Programming Activity 7
# Remove leading/trailing spaces from each string using list comprehension
# ---------------------------------------------------------------
stringlist = [" spring", "summer ", "fall ", "winter "]
gapless = [word.strip() for word in stringlist]

print("Activity 7:", gapless)


# ---------------------------------------------------------------
# Front seat problem
# Can a child sit in the front seat of a car? (uses Boolean variables)
# ---------------------------------------------------------------
age = int(input("Enter the child's age: "))
weight = float(input("Enter the child's weight in pounds: "))

# Boolean variables for each criterion
is_12_or_older = age >= 12
is_11_and_over_90 = age == 11 and weight > 90
is_under_11_and_over_100 = age < 11 and weight > 100

if is_12_or_older or is_11_and_over_90 or is_under_11_and_over_100:
    print("The child may sit in the front seat.")
else:
    print("The child may not sit in the front seat.")


# ---------------------------------------------------------------
# Problem 1: Find all prime numbers within a given range using a for loop
# ---------------------------------------------------------------
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

for num in range(start, end + 1):
    if num > 1:                                  # primes must be greater than 1
        is_prime = True
        for divisor in range(2, int(num ** 0.5) + 1):
            if num % divisor == 0:               # divides evenly, so not prime
                is_prime = False
                break
        if is_prime:
            print(num)


# ---------------------------------------------------------------
# Problem 2: Reverse a 3+ digit integer WITHOUT using lists
# ---------------------------------------------------------------
number = int(input("Enter an integer with 3 or more digits: "))

reversed_number = 0

while number > 0:
    digit = number % 10                              # isolate the last digit
    reversed_number = reversed_number * 10 + digit   # add it to the end of the reversed number
    number = number // 10                            # remove the last digit

print("Reversed:", reversed_number)
