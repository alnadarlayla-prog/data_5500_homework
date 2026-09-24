"""
HW2 Layla Abdulmohsin Sep 23 2026
"""


# 2.3 
grade = 91
if grade >= 90:
    print(f"Congratulations! Your grade of {grade} earns you an A in this course")


# 2.4 AI disclaimer: it was used to get the right order of operations, like which number comes before the operator, it was used after my own code was written
print("\n2.4 Arithmetic")
print("27.5 + 2  =", 27.5 + 2)     # addition
print("27.5 - 2  =", 27.5 - 2)     # subtraction
print("27.5 * 2  =", 27.5 * 2)     # multiplication
print("27.5 / 2  =", 27.5 / 2)     # true division
print("27.5 // 2 =", 27.5 // 2)    
print("27.5 ** 2 =", 27.5 ** 2)    


# 2.5 AI disclaimer: it was used to help me on line 28
print("\n2.5 Circle")
radius = 2
pi = 3.14159
diameter = 2 * radius
circumference = 2 * pi * radius
area = pi * radius ** 2
print("Diameter:", diameter)
print("Circumference:", circumference)
print("Area:", area)


# 2.6 
print("\n2.6 Odd or even")
integer = 7                      
if integer % 2 == 0:             # even numbers will leave a remainder of 0 when divided by 2
    print(integer, "is even")
if integer % 2 != 0:             # if not this means otherwise the number is odd
    print(integer, "is odd")


# 2.7 
print("\n2.7 Multiples")
if 1024 % 4 == 0:
    print("1024 is a multiple of 4")
else:
    print("1024 is not a multiple of 4")

if 2 % 10 == 0:
    print("2 is a multiple of 10")
else:
    print("2 is not a multiple of 10")


# 2.8 
print("\n2.8 Squares and cubes")
print("number\tsquare\tcube")
for number in range(6):
    print(f"{number}\t{number ** 2}\t{number ** 3}")
    
# 3.4 
print("\n3.4 Rows of @")
for row in range(2):                # outer loop: 2 rows
    for column in range(7):         # inner loop: 7 symbols per row
        print('@', end='')          
    print()                         # move to the next line after each row is printed on screeen


# 3.9 AI disclaimer, it was used to help on the aggregation part in lines 80-83
print("\n3.9 Separating the digits")
text = input("Enter a number 7 to 10 digits: ")

if len(text) < 7 or len(text) > 10 or not text.isdigit():
    print("Please enter an integer with 7 to 10 digits.")
else:
    number = int(text)                   # convert the input string to an integer
    divisor = 10 ** (len(text) - 1)      # place value of the leftmost digit
    while divisor > 0:
        print(number // divisor)         # // picks off the leftmost digit
        number = number % divisor        # % removes that digit
        divisor = divisor // 10          # move to the next place value


# 3.11 
print("\n3.11 Miles per gallon")
total_miles = 0
total_gallons = 0

gallons = float(input("Enter the gallons used (-1 to end): "))
while gallons != -1:                     # -1 is the sentinel value
    miles = float(input("Enter the miles driven: "))
    print(f"The miles/gallon for this tank was {miles / gallons:.6f}")
    total_miles += miles
    total_gallons += gallons
    gallons = float(input("Enter the gallons used (-1 to end): "))

if total_gallons > 0:                    # only report if at least one tank was entered
    print(f"The overall average miles/gallon was {total_miles / total_gallons:.6f}")


# 3.12 
print("\n3.12 Palindromes")
text = input("Enter a five-digit integer: ")

if len(text) != 5 or not text.isdigit():
    print("Please enter exactly five digits.")
else:
    is_palindrome = True
    # compare the first character with the last and so on
    for i in range(len(text) // 2):
        if text[i] != text[len(text) - 1 - i]:
            is_palindrome = False
    if is_palindrome:
        print(text, "is a palindrome")
    else:
        print(text, "is not a palindrome")


# 3.14 AI disclaimer the comments took my a very long time to get right so it helped with checking the rows accurately. 
#
# Approximations are truncated (not rounded) to 2 or 3 decimal places before checking.
# ANSWERS (number of terms used):
#   3.14  first appears at iteration 119 and appears twice in a row at iteration 628
#         (iterations 627 and 628).
#   3.141 first appears at iteration 1688 and appears twice in a row at iteration 2455
#         (iterations 2454 and 2455).
print("\n3.14 Approximating pi")
print("terms\tapproximation")

pi_approx = 0
sign = 1                                
previous_2 = 0                         
previous_3 = 0                         
found_314 = False
found_3141 = False

for terms in range(1, 3001):
    pi_approx += sign * 4 / (2 * terms - 1)     # add the next term: 4/1, 4/3, 4/5, ...
    sign = -sign

    print(f"{terms}\t{pi_approx}")

    current_2 = int(pi_approx * 100) / 100      # truncate to 2 decimals
    current_3 = int(pi_approx * 1000) / 1000    # truncate to 3 decimals

    if not found_314 and current_2 == 3.14 and previous_2 == 3.14:
        print(f"3.14 twice in a row at iteration {terms}")
        found_314 = True
    if not found_3141 and current_3 == 3.141 and previous_3 == 3.141:
        print(f"3.141 twice in a row at iteration {terms}")
        found_3141 = True

    previous_2 = current_2
    previous_3 = current_3

    if found_314 and found_3141:                # nothing else, so stop early
        break
