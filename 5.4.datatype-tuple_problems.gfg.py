""" 1.  | Print unique rows in a given boolean matrix using Set with tuples
"""
def uniquerows(input): # Function to print unique rows in a given boolean matrix
    # convert each row (list) into tuple
    # we are mapping tuple function on each row of
    # input matrix
    input = map(tuple, input)
    result = set(input) # put all rows in set
    for row in list(result):
        print(row)
        
if __name__ == "__main__":
    input =  [[1,0,0,1],
              [1,1,0,0],
              [1,0,1,0],
              [1,1,0,0]]
    uniquerows(input)  
    
"""2.Python Dictionary to find mirror characters in a string

"""
# function to mirror characters of a string

def mirrorChars(input,k):

    # create dictionary
    original = 'abcdefghijklmnopqrstuvwxyz'
    reverse = 'zyxwvutsrqponmlkjihgfedcba'
    dictChars = dict(zip(original,reverse))

    # separate out string after length k to change
    # characters in mirror
    prefix = input[0:k-1]
    suffix = input[k-1:]
    mirror = ''

    # change into mirror
    for i in range(0,len(suffix)):
         mirror = mirror + dictChars[suffix[i]]

    # concat prefix and mirrored part
    print (prefix+mirror)
         
# Driver program
if __name__ == "__main__":
    input = 'paradox'
    k = 3
    mirrorChars(input,k)
    
'''3. Generate Two Output Strings Depending upon Occurrence of Character in Input String  '''  
s = "hello"

d = {} 

# Single pass over input string to count frequencies
for char in s:
    d[char] = d.get(char, 0) + 1

# Separate characters into two lists
a = [char for char, count in d.items() if count == 1]
b = [char for char, count in d.items() if count > 1]

print(''.join(sorted(a)))
print(''.join(sorted(b)))


"""4. Removing consecutive duplicates from a list

"""
s = ["a", "a", "b", "b", "c"]

# Remove consecutive duplicates
res = [key for key, _ in groupby(s)]
print(res)

''' 5.Convert a List of Characters into a String - Python

'''
a = ['P', 'y', 't', 'h', 'o', 'n']

# Convert list of characters to string
s = ''.join(a)

print(s)

'''6. Remove empty tuples from a list - Python

'''
a = [(1, 2), (), (3, 4), (), (5,)]

res = list(filter(None, a))
print(res)

'''7. Reversing a Tuple
'''
t = (9,0,7,8)
a = t[::-1] 
print(a)

'''8. Convert a list of Tuples into Dictionary 
'''
a = [("a", 1), ("b", 2), ("c", 3)]

res = dict(a)

print(res)

"""9. Python | Count occurrences of an element in a Tuple

"""  
def countEle(tup, element):
    count = 0
    
    for x in tup:
        if(x == element):
            count = count + 1
    return count
tup = (1, 1, 3, 6,8,9,3,4 , 1)
enq = 1
enq2 = 3
print(countEle(tup, enq))
print(countEle(tup, enq2))




        
           