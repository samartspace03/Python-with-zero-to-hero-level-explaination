#1. Given a double value d, typecast it to an integer value and print it.
x = 3.8
print(int(x))
#output is 3 

#2. swaping of num
a, b = 10, 5
print(b,a)
#output is 5 10

#3.PRINT LENGTH OF CHAR IN WORD
name = "samruddhi"
print(len(name))
#so here we usse len fun to get char length so it is 9

#4. Given an input num as a string. You need to typecast into an integer and double it. 
num = "6"
print(int(num)*2)

#5. Given an integer n find the sum of the first n natural number.
#1st way
class Solution:
    def sumOfNum(num):
        return num * (num + 1) // 2
    
num = int(input("enter num: "))
sum = Solution.sumOfNum(num)
print(num, sum)
 
 #2nd way  
num = int(input("enter num: "))
sum = num * (num + 1) // 2
print(sum)


