"""#__list of programs: LIST CREATION
1. WAP Create List of Numbers with Given Range - Python

"""
r1 = 0
r2 = 20
li =list(range(r1,r2))
print(li)
"""2. WAP Ways to create a dictionary of Lists - Python
---1 general fun
----2 using zip
-3: defaultdict automatically creates a default value for keys that don’t exist, making it ideal for building a dictionary of lists dynamically.
---4.setdefault() method simplifies handling missing keys by initializing a default list if the key doesn’t exist.
"""
d = {}
d["1"] = [1,2]
d["2"] = ["mango","lichi"]
print(d) #'1': [1, 2], '2': ['mango', 'lichi']}

k = [1,2,3]
val = ["mogra","lily","merrygold"]
d = dict(zip(k,val))
print(d)

from collections import defaultdict

# Initialize a defaultdict with list as the default type
d = defaultdict(list)

# Add values to the dictionary
d[1].append("Apple")
d[2].append("Banana")
d[3].append("Carrot")

print(d)

li = [("Fruits", "Apple"), ("Fruits", "Banana"), ("Vegetables", "Carrot")]

# Initialize an empty dictionary
d = {}

# Use setdefault to populate the dictionary
for k, item in li:
    d.setdefault(k, []).append(item)

print(d)

"""3. WAP Create a List of Tuples in Python

"""
a = ("sam","kranti","salu")
b =(1,2,3)
c = ("to", "mein", "or")
d = list(zip(a,b,c))
print(d)

"""4.wap How to create list of dictionary in Python

"""
a = []

# Using a loop to create a list of dictionaries
for i in range(3):
    a.append({"name": f"Person {i+1}", "age": 20 + i})
print(a)

"""5.Python - Create List of Size n

"""

n = 6
a = [0]*n
print(a)
"""6. Create a List of Strings in Python
"""
# Converting a tuple to a list using the list() function
b = list(("geeks", "for", "geeks"))

print(b)#['geeks', 'for', 'geeks']

"""7. Create a List of Tuples with Numbers and Their Cubes - Python
"""
a = [1,2,3,4,5]

d = [(n, n**3) for n in a ]
print(d) # [(1, 1), (2, 8), (3, 27), (4, 64), (5, 125)]

"""2.Python List Add/Append Programs
1.Perform Append at Beginning of List - Python
1. append():	                                                      2. extend()
Purpose	Adds a single element to the end of the list.:       	Adds multiple elements from an iterable to the end of the list.

"""
list = ["sam","santosh","kamble"]
list.insert(0, "1")
print(list)#['1', 'sam', 'santosh', 'kamble']

"""2. How to Append Multiple Items to a List in Python

"""
# Initializing a list
a = [1, 2, 3]

# Appending multiple items
a.extend([4, 5, 6])
print(a)

"""3. Python List Removal Programs
1] Ways to remove duplicates from list in Python
"""
a = [1, 2, 2, 3, 4, 4, 5]

# Remove duplicates by converting to a set
a = list(set(a))  # set() to remove duplicates from the list.

print(a)

"""2]remove element from list
"""
a = [10, 20, 30, 40, 50]
a.remove(30)
print(a)
"""3]Remove all the occurrences of an element from a list in Python
"""# Function to remove all occurrences of a given item from a list
def remove_items(test_list, item):
    # Count how many times the item appears in the list
    c = test_list.count(item)
    # Loop through the count and remove the item that many times
    for i in range(c):
        test_list.remove(item)
    # Return the updated list after all occurrences are removed
    return test_list
  
# Driver code to test the function
if __name__ == "__main__":
    # Initialize the original list
    test_list = [1, 3, 4, 6, 5, 1]
    
    # Define the item to be removed
    item = 1
    
    # Print the original list
    print("The original list is :" + str(test_list))

    # Call the remove_items function to remove all occurrences of 'item'
    res = remove_items(test_list, item)

    # Print the updated list after removal
    print("The list after performing the remove operation is :" + str(res))
    
 #remove specific item   
a = ['a', 'b', 'c']
a.remove("b")
print(a)
    
"""4]Remove all values from a list present in another list - Python

""" 
a = [1, 2, 3, 4, 5]
b = [2, 4]

# Using list comprehension to remove values of 'b' from 'a'
result = [item for item in a if item not in b]

# Output the result
print(result)   

""" 5] remove duplicates : dict.fromkeys() -->creates a dictionary with keys from the list, automatically removing duplicates because dictionary keys are unique. 
"""
a = [1, 2, 2, 3, 4, 4, 5]

b = list(dict.fromkeys(a))
print(b)

"""3. LIST COUNT PROBLEMS 
1) Count occurrences of an element in a list in Python

"""
a = input("enter list: ").split()
x = input("enter item : ")
d = a.count(x)
print(f"{x}")

"""2) count positive element in list and negative also
""" 
a = [10, -20, 30, -40, 50, -60, 0, 8]

# Counts the positive numbers
pos = 0

# Counts the negative numbers
neg = 0

# Iterate through the list
for n in a:
    if n > 0:
        pos += 1
    elif n < 0:
        neg += 1

print(pos)
print(neg) 

"""3)count unique element in a list"""
items = input("Enter elements separated by space: ").split()
unique_items = []
count = 0

for item in items:
    if item not in unique_items:
        count += 1
        unique_items.append(item)

print("Unique count:", count)
print("Unique items:", unique_items)


# taking an input list
input_list = [1, 2, 2, 5, 8, 4, 4, 8]

# taking an input list
l1 = []

# taking an counter
count = 0

# traversing the array
for item in input_list:
    if item not in l1:
        count += 1
        l1.append(item)

# printing the output
print("No of unique items are:", count)

"""4) Count Occurance of Substring in a List of Strings - Python

"""
x = ["hello", "world", "hi", "hello world"]

# Count the number of strings in the new list using len()
count = len([y for y in x if "hello" in y])
print(count)       

""" 4. Python List Checking and Verification Programs
1)
Check if element exists in list in Python

"""
a = [1,2,3,4,5,3]

if 2 in a:
    print("present")
else:
    print("false")  

"""2)Check if a list is empty or not in Python

"""     
i = []
if not i:
    print("empty")
else:
    
    print("not empty")     
    
i = []
if len(i) == 0:
    print("empty")
else:
    print("no empty") 
     
"""   3)
Check if two lists are identical in Python

"""  
a = [1,2,3]
b = [1,2,3]
if a == b:
    
    print("yes, both are same")  
else:
    print("no")  
    
"""
4) Check if a List is Sorted or not - Python

"""        
a = [1,2,3,4,5]
b = [5,3,2,4,1]
print(a == sorted(a))  
print(b == sorted(b)) 

""" 5) Check if all the values in a list that are greater than a given value - Python

""" 
  
    
a = [10, 20, 30]
b = 5 # threshold

res = all(x > b for x in a)
print(res)   
    
"""1>
How To Find the Length of a List in Python

""" 
a = [1,2,3,4,5,6,7,8]
d = len(a)  
print(d)    
    
"""2> Python Program to Find Largest Number in a List
"""   
a = [1,2,3,4,5,6,7]
d = max(a)
print(d) 

"""3)Python Program swap Number in a List

"""
a = [10, 20, 30,40, 70]
a[0], a[4] = a[4], a[0]
print(a)

'''4) reverse list
'''
a = [1, 2, 3, 4, 5]

# Reverse the list in-place
a.reverse()
print(a)

"""5)sum
"""
a = [10, 20, 30, 40, 50]
res = sum(a)
print(res)

"""6)merge list
"""
a = [1, 2, 3]
b = [4, 5, 6]

# Merge the two lists and assign
# the result to a new list
c = a + b
print(c)

"""7)sort
"""
a = [5, 1, 5, 6]

# Sort modifies the given list
a.sort()
print(a)

"""sorted list
"""
a = [5, 6, 3, 8, 2, 1, 7, 1]
b = [8, 2, 1] # sublist

res = str(b)[1:-1] in str(a)[1:-1]

print(res)

"""WAP You are given a list that contains integers. You need to print the elements of the list with a space between them.
"""

# 
    
         
def listTraversal(arr):
    # Print all elements in the list separated by a space
    print(*arr, sep=' ', end='')

# Take user input: space-separated integers
arr = list(map(int, input("Enter list elements separated by space: ").split()))

# Call the function
listTraversal(arr)
   
"""WAP You are given a list that contains integers. You need to return the sum of the list.


"""    
list = [1,2,3]
a = sum(list)
print(a)

"""You are given a list that contains integers. You need to decrement each element of the list by 1 and return the list
"""
arr = [2,3,4,5]
s = [x - 1 for x in arr]
print(s)

"""Given an unsorted array arr containing both positive and negative numbers. Your task is to rearrange the array and convert it into an array of alternate positive and negative numbers without changing the relative order.
"""
def rearrange_alternate_pos_neg(arr):
    # Separate positive and negative numbers with relative order
    pos = [x for x in arr if x >= 0]
    neg = [x for x in arr if x < 0]

    result = []
    i = j = 0

    # Start alternating with positive
    while i < len(pos) and j < len(neg):
        result.append(pos[i])
        result.append(neg[j])
        i += 1
        j += 1

    # Append remaining elements from pos or neg
    result.extend(pos[i:])
    result.extend(neg[j:])

    return result

# Example usage
arr = list(map(int, input("Enter elements: ").split()))
res = rearrange_alternate_pos_neg(arr)
print("Rearranged array:", *res)