# here is the tutorial which is showing how should you print the text and many more stuff stay tuned 
#1. at first we'll learn how to print any sentence or word in python so for that you've to use PRINT("SENTENCE") function
print("Hello, Guys Today is my 1st day and I'm starting this tutorial to learn python from begineer to advanced level to become an expert")

print("I'm going to cover all the topics which are required to learn python and I'll try")

#2. taking input from user : so u've to use input() function 

# you've to remember 1 thing 
#🔑 Difference Between input() and int(input()) in Python
#1. input(): takes input as a string, no matter what the user enters.
# Example:

age = input("Enter your age: ")
print(type(age))  # Output: <class 'str'>

#2. int(input()):
#Converts the input to an integer using int().
#Useful when you expect numerical input and want to perform calculations.
# Example:


age = int(input("Enter your age: "))
print(age + 1)  # Correctly adds 1 to the age#⚠️ Note: If the user enters a non-numeric value like "abc" in int(input()), it will raise a ValueError

# u can take input from user  and use split() method : We are taking multiple input from the user in a single line, splitting the values entered by the user into separate variables for each value using the split() method.


# Example:
user_input = int(input("how many items u want in ur list: "))
items = list[input("Enter items separated by comma: ").split(',')]
print(items)
# output : how many items u want in ur list: 5   
#Enter items separated by comma: 1, 2,3,4,5
#list[['1', ' 2', '3', '4', '5']] output completed 


#1st way : parsing strings is a common task when working with text data. String parsing involves splitting a string into smaller segments based on a specific delimiter or pattern
# Example:
text = "I am looking hot."
words = text.split() # Split the text into words
print(words) # output : ['I', 'am', 'looking', 'hot.']

# 2nd way : To take input like 1 2 3 4 and convert it into a list [1, 2, 3, 4], you can use this code in Python:

user_input = input("Enter numbers separated by space: ")  # e.g., 1 2 3 4
numbers = list(map(int, user_input.split()))
print(numbers)
#🔍 Explanation:
#1. input()--> gets the input as a string: "1 2 3 4"

#2. .split() --> splits it by spaces → ['1', '2', '3', '4']

#3.map(int, ...) --->converts each string to an integer → [1, 2, 3, 4]

#4. list() ---> converts the map object to a list.

# Take Multiple Input in Python'
a, b = input("enter two values: ").split()
print("number of fruits: ", a)
print("number of flower: ", b)

# Find DataType of Input in Python
# You can use the type() function to find the data type of the input in Python.
# Example:
user_input = input("Enter your name: ")
print(type(user_input))

a = 10
print(type(a))# Output: <class 'int'>
b = 2.4
c = ("joker", "ball")
d = ["so", "if", "to"]
e = {'boy': 2 }
print(type(b))# Output: <class 'float'>
print (type(c))# Output: <class 'tuple'>
print(type(d))# Output: <class 'list'>
print(type(e))# Output: <class 'dict'>


# output formatting 
#1. use format(), 2. use end and separator method 3. use f- string 4. use %
#examples:
#1. use format()
name = "John"
age = 30
print("My name is {} and I am {} years old.".format(name, age))
#output : My name is John and I am 30 years old.

#2. use end and separator method    
print("My name is", end=" ")
print("John", end=" ")
print("and I am", end=" ")
print("30 years old.", sep=" ")
#output : My name is John and I am 30 years old.

#3. use f- string
name = "John"
age = 30
print(f"My name is {name} and I am {age} years old.")
#output : My name is John and I am 30 years old.'
#4. use %
name = "John"
age = 30
print("My name is %s and I am %d years old." % (name, age))
#op: My name is John and I am 30 years old.