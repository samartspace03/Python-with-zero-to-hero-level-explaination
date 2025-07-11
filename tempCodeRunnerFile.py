class Solution:
    def sumOfNum(num):
        return num * (num + 1) // 2
    
num = int(input("enter num: "))
sum = Solution.sumOfNum(num)
print(num, sum)