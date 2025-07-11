#🔢 1. Arithmetic Operators (+, -, *, /, //, %, **)
#Used to perform basic math operations.

#📦 Real-life Example:
#Imagine you’re buying fruits 🍎🍌:


apple_price = 10
banana_price = 5
total = apple_price + banana_price  # total = 15
#🧾 Example:


print(5 + 3)   # 8
print(10 - 2)  # 8
print(4 * 2)   # 8
print(16 / 2)  # 8.0
print(17 // 2) # 8 (floor division)
print(17 % 2)  # 1 (remainder)
print(2 ** 3)  # 8 (power)
#🟰 2. Assignment Operators (=, +=, -=, *=, etc.)
#Used to assign values to variables.

#📦 Real-life Example:
#Saving money daily 💰:


savings = 100
savings += 50  # Add 50 to savings
# Now savings = 150
#🤝 3. Comparison Operators (==, !=, >, <, >=, <=)
#Used to compare values.

#📦 Real-life Example:
#Checking age for driving license 🚗:


age = 18
print(age >= 18)  # True → allowed to drive
#🧠 4. Logical Operators (and, or, not)
#Used to combine conditional statements.

#📦 Real-life Example:
#ATM pin and card check 🏦:


card_inserted = True
correct_pin = True
print(card_inserted and correct_pin)  # True → Allow transaction
#🧱 5. Identity Operators (is, is not)
#Check if two variables refer to the same object.

#📦 Real-life Example:
#Two empty glasses:


a = []
b = []
print(a is b)      # False (different glasses)
print(a is not b)  # True
#📦 6. Membership Operators (in, not in)
#Used to check if a value exists in a sequence (like list, string).

#📦 Real-life Example:
#Checking if item is in your shopping list 🛒:


shopping_list = ['milk', 'bread', 'eggs']
print('milk' in shopping_list)      # True
print('butter' not in shopping_list)

# 🧾 Bitwise Operators Summary:

#Operator	Name	Example (a=5, b=3)	Result	Binary Explanation
#&	AND	a & b	1	0101 & 0011 = 0001
#`	`	OR	`a	b`
#^	XOR (exclusive)	a ^ b	6	0101 ^ 0011 = 0110
#~	NOT	~a	-6	~0101 = -(0101+1) = -6
#<<	Left Shift	a << 1	10	0101 << 1 = 1010 (shift left, ×2)
#>>	Right Shift	a >> 1	2	0101 >> 1 = 0010 (shift right, ÷2)