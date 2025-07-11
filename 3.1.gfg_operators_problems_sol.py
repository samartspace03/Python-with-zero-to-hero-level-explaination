#1. You are given two integer variables x and y. You need to perform the following operations:

#p = x + y : Addition
#q = x - y : Subtraction
#r = x * y :Multiplication
#s = x / y : Division
#t = x % y : Modulo

x = int(input("enter x: "))
y = int(input("enter y : "))
p = x + y
print(p)
q = x - y
print(q)
r = x * y
print(r)
s = x / y 
print(s)
t = x % y
print(t)

#2. Logical operators and, or, not are used in condition checking. Like a and b checks if both a and b are True. First a is checked then b is checked. a or b checks if either of a or b is True. If one is True; it doesn't check for the other. not a complements the boolean value of a.
#Note: 0 and empty string are False and all other values are True.
#In this question you basically need to do
#a and b
#a or b
#not a

a = 0
b = 2
p = a and b
print(p)
q = a or b
print(q)
r = not a
print(r)

#3. Given three positive integers a, b and c. Your task is to perform some bitwise operations on them as given below:
#1. d = a ^ a
#2. e = c ^ b
#3. f = a & b
#4. g = c | (a ^ a)
#5. e = ~ e
a = 7
b = 6
c = 9

d = a ^ a
e = c ^ b
f = a & b
g = c | (a ^ a)
e = ~ e
print(d,e,f,g,e)

#4. Given an integer N. FInd an integer K for which N%K is the largest ( 1 <= K < N).
   
    
def find_max_remainder_k(N):
    max_remainder = -1
    best_k = -1

    for K in range(1, N):
        remainder = N % K
        if remainder > max_remainder:
            max_remainder = remainder
            best_k = K

    return best_k

# Example usage
N = int(input("Enter N: "))
print("K with max N%K is:", find_max_remainder_k(N))

#5.Given an integer n. Write a program to return the last digit of the number.

def last_digit(num):
    return num %10 #% 10 gives the last digit.
num =int(input())
print("num: ", last_digit(num))

#6. Given an integer n find the sum of the first n natural number.

n = int(input("enter num: "))
sum = n * (n + 1) // 2
print(sum)

#7.Given two numbers a and b. The task is to find the GCD of  a and b.
#The GCD of two numbers is the largest number that can divide both a and b perfectly

a = int(input("enter a: "))
b = int(input("enter b: "))
# Function to calculate the Greatest Common Divisor (GCD) of two numbers
def gcd(a, b):
    # Use the Euclidean algorithm:
    # Keep looping until b becomes 0
    while b != 0:
        # In each iteration:
        # 1. Set 'a' to the current value of 'b'
        # 2. Set 'b' to the remainder of 'a' divided by 'b'
        a, b = b, a % b
    # When b becomes 0, 'a' holds the GCD
    return a

# Example usage:
# Replace 'a' and 'b' with actual numbers, e.g., a = 48, b = 18
result = gcd(a, b)  # Call the gcd function and store the result
print(result)


#8. Given two numbers a and b. The task is to find out their LCM.
#The LCM of two numbers is the smallest positive number that is divisible by both.
#START

#1. Input two numbers: A and B
#2. Set max_num = maximum of A and B  → (because LCM must be ≥ max(A, B))
#3. WHILE True:
  #   a. IF max_num is divisible by both A and B:
   #        i. LCM found → PRINT max_num
    #       ii. BREAK the loop
     #b. ELSE:
      #     i. Increment max_num by 1
#4. END


a = int(input("enter a: "))
b = int(input("enter b : "))
lcm = max(a,b) # Because LCM is always greater than or equal to the max of the two
while True: # Run an infinite loop to find the LCM

    if lcm % a == 0 and lcm % b == 0:    # Check if current lcm is divisible by both a and b

        print(lcm)        # If divisible by both, it is the LCM

        break# Exit the loop once LCM is found
    else:         # If not divisible by both, try the next number

        lcm+= 1
        
#9. You are given a 3-digit number n, Find whether it is an Armstrong number or not.

#An Armstrong number of three digits is a number such that the sum of the cubes of its digits is equal to the number itself. 371 is an Armstrong number since 33 + 73 + 13 = 371  

#start

#1.INPUT number n
#2.SET original = n
#3.SET sum = 0

#4.WHILE n is not 0:
   # a. digit = n % 10        → (get last digit)
   # b. sum = sum + (digit)^3 → (add cube of digit)
    #c. n = n // 10           → (remove last digit)

#5.iF sum == original:
   #  PRINT "Armstrong Number"
  #ELSE:
 #    PRINT "Not an Armstrong Number"

#TOP
      
n = int(input("enter 3 digit num : "))
sum_original = n# Save original number
sum = 0# To store sum of cubes

while n != 0:# Loop to extract digits and calculate cube sum

    last_digit = n % 10#get last digit
    sum = sum + (last_digit)** 3 # checks sums of cube of that num is = to each item of that cube num
    n = n // 10#reomove last digit
    
if sum == sum_original:
        print("it is armstrong num.")
else:
        print("it is not armstrong num.")
        
        
# 10. Given a positive integer n. Your task is to return the count of set bits.

n = int(input("enter + num: "))

binary = bin(n)[2:]  # bin() returns '0b...' so [2:] skips '0b'

# Step 3: Count the number of 1s in the binary representation
count = binary.count('1')
print(count)
  #11. evaluate formulae 
a = int(input("enter a: "))
b = int(input("enter b: ")) 
c = int(input("enter c: "))
d = int(input("enter d: "))
result = (((a + b)// c) + d )
print(result)

#12. Given three integers a, d and n. Where a is the first term, d is the common difference of an A.P.  Calculate the nth term of A.P. 
#he nth term is given by an = a + (n-1)d
a = int(input("enter a: "))
d = int(input("enter d: "))
n = int(input("enter n: "))
arithmetic_prog = a + ( n - 1) * d
print(arithmetic_prog)
    
    
#13. Given three integers, a, r and n. Where a is the first term, r is the common ratio of a G.P. and r is equal to 2.  Calculate the nth term of GP.

#nth term is given by an = a * r(n-1),
a = int(input("enter a: "))
n= int(input("enter n : "))
r= int(input("enter r: "))
geometric_prog = a * r **(n - 1)
print(geometric_prog)

