# 1. When learning a new language, we first learn to output some message. Here we will start with the famous "Hello World" message.
#Complete the python code to print "Hello World".

print("Hello World")
#output: Hello World

# 2.You are given two variables, a and b. Your task is to print these variables in the following formats:

# With space: Print a and b in a single line, separated by a space, followed by a newline.
# Without newline: Print a and b separated by a space, but do not end the output with a newline.
# With separator: Print a and b separated by a specified separator, followed by a newline.
# Without space: Print a and b in a single line, with no spaces between them, followed by a newline.
#Complete the python code to print the variables a and b in the specified formats.
a = input()
b = input()

print(a, b)
print(a, b, end ='')
separator = "-"
print("\n" + str(a) + separator + str(b))
print(f"{a}{b}")

#3. Given two inputs that are stored in variables a and n, you need to print a, n times in a single line without space between them. Output must have a newline at the end.

#Examples:

#Input: a = "Hello", n = 5
#Output: HelloHelloHelloHelloHello

a = "Hello"
n = 5
print(a*n)# HelloHelloHelloHelloHello what happened we use * operator to multiply the hello for 5 times thats whyhello printed 5 times without space

# 4. Given three inputs that are stored in the variables a, b, and c. You need to print a a times and b b times  in a single line separated by c.

#Examples:

#Input: a = 6, b = 4, c = &
#Output: 666666&4444
#Explanation: 6 printed 6 times and 4 printed 4 times seperated by c = &
a = 6
b = 4
c = '&'

print(str(a)*6 + c + str(b)*4)#666666&4444

#4. You need to perform three separate tasks based on the given input:

#String Input and Print: Take a text input as a string and print it as it is.
#Integer Input and Add: Take an integer input n, add 10 to it, and print the result.
#Float Input and Multiply: Take a floating-point number as input, multiply it by 10, and print the result

str = input("type ur input: ")
print(str)
user_input = int(input("enter num: " ))
print(user_input + 10)
float = float(input("enter ur decimal: "))
print(float * 10)

