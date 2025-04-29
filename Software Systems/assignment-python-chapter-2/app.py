# Chapter 2.1 and 2.2 Variables
import math
students_count = 1000
rating = 4.99
is_published = True
course_name = "Python Programming"
print(students_count)
print(rating, is_published, course_name)
print("." * 10)

# Chapter 2.3 Strings
course = "Phyton Programming"
print(len(course))
print(course[0])
print(course[-1])
print(course[0:3])
print(course[0:])
print(course[:3])
print(course[:])
print("." * 10)

# Chapter 2.4 Escape Sequences
# \"
course = "Python \"Programming"
print(course)
# \'
course = "Python \"Programming"
print(course)
# \\
course = "Python \"Programming"
print(course)
print("." * 10)

# Chapter 2.5 Formatted Strings
first = "Sean"
last = "Humpherys"
full = f"{len(first)} + {2 + 2}"
print(full)
print("." * 10)

# Chapter 2.6 String Methods
print("Chapter 2.6 String Methods")
course = " python programming"
print(course.upper())
print(course.lower())
print(course.title())
print(course.rstrip())
print(course.find("Pro"))
print(course.replace("p", "j"))
print("pro" in course)
print("swift" not in course)
print("." * 10)

# Chapter 2.7 Numbers"
print("Chapters 2.7 Numbers")
x = 1  # integer
x = 1.1  # float number with decimals
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)
print(10 % 3)  # modulous or mod
print(10 ** 3)  # exponent

x = 10
x = x + 3
print(x)
x = 10
x += 3  # augmented operator add
print(x)

y = 20
y -= 3  # augmented operator subtract
print(y)

z = 30
z *= 3  # augmented operator mu;tiply
print(z)

# Chapter 2.8 Working with Numbers
print("Chapter 2.8 Working with Numbers")

print(round(2.9))
print(abs(-2.0))
print(math.ceil(2.2))
print("." * 10)

# Chapter 2.9 Type Conversion
x = input("Enter a value for x: ")
y = int(x) + 1
print(f"x: {x}, {y}")
print("." * 10)

rate = input("Enter interest rate,e.g. 0.5: ")
rate = float(rate)  # may reuse the same variable
# CRITICAL KNOWLEDGE
# three different ways to output a number with text
print(f"Borrower does not qualify at {rate}")  # string interpolation
print("Borrower does not qualify at ", rate)
print("Borrower does not qualify at " + str(rate))
print()
# Dr. Humphreys likes string interpolation the best!

# Displaying decimals in Strings
grams = 15.125
print(f"Weight is {grams}")  # no formatting
print(f"Weight is {grams: .2f}")  # two decimals, f means float
print(f"Weight is {grams: .4f}")  # four decimals
print(f"Weight is {grams: .0f}")  # zero decimals

# Printable receipt
# Declare a string variable called card_number
card_number = "xxx8974"

# Declare a string variable called date and use an escape sequence for the slashes
date = "9\\7\\2020"

# Declare a float number variable called cookies_cost and assign a value
cookies_cost = 3.15

# Declare a float number variable called chips_cost and assign a value
chips_cost = 4.58

# Declare a float number variable called salsa_cost and assign a value
salsa_cost = 5.10

# Declare a float number variable called total_cost and assign a value
total_cost = cookies_cost + chips_cost + salsa_cost

# Print the receipt
print("Receipt")
print(f"Card Number: {card_number}")
print(f"Date: {date}")
print(f"Cookies: ${cookies_cost: .2f}")
print(f"Chips: ${chips_cost: .2f}")
print(f"Salsa: ${salsa_cost: .2f}")
print(f"Total: ${total_cost: .2f}")
