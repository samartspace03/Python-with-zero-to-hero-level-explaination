"""
    This module talks about Strings in Python. String in Python is immutable (cannot be edited). You have learnt about separators in Python. Let's start String with first question given below:
1 WAP:
Given name of a person, the task is to welcome the person by printing the name with "Welcome". If name is "John", you should print "Welcome John"
    """
str = input("enter: ")
print("Welcome " + str)

"""2. WAP:

Whooaah! Your are now familiar with String slicing. Let's have one more question to make it crystal clear for you with some conditional statements.

Given two strings a and b. The task is to make a new string where the string with longer length should be in between and the one with shorter length should be outside on front and end. New string should be like shorter+longer+short


"""
a = input()
b = input()
if len(a) > len(b):
    print(b + a + b)
else:
    print(a + b + a)
    
def combo_string(a, b):
    if len(a) > len(b):
        return b + a + b
    else:
        return a + b + a
a = input("a: ")
b = input("b: ")
print(
combo_string(a,b))

"""WAP:
    Python has a lot of string methods that can be used to manipulate the strings like converting to lowercase, capitalizing, trimming the spaces and so on.
    
    7 Useful String Functions in Python 
1.  Capitalize
2. Count
3. Find
4. Lower
5. Upper
6. Replace
7. Join

In this question, we'll take a look at inbuilt string methods like title(), swapcase(), find(), strip().
You'll be given a string str and x, you'll perform various operations on them.
 """
str = input("enter a string: ")
x = input("enter x : ")
print(str.title())
print(str.swapcase)
print(str.find(x))
print(str.strip('-'))
#1.capitalize()---->
sentence_1 = "mY name is YUVRAJ"
sentence_2 = "MY name is Ansul"

# Convert case using capitalize()
capitalized_string = sentence_1.capitalize()
print("Sentence 1 output -> ", capitalized_string)
capitalized_string = sentence_2.capitalize()
print("Sentence 2 output -> ", capitalized_string)

#2.count()-->
message = ('GDS KA BOOTCAMP KRLO HO JAYEGA')

# number of occurrence of 'G'
print('Number of occurrence of G:', message.count('G'))

#3. lower()
message = ' COMPUTER SCIENCE PORTAL'

# convert message to lowercase
print(message.lower())
#4. replace 
text = 'subway surfer'

# replace s with t
replaced_text = text.replace('s', 't')
print(replaced_text)

#5. join
text = ['Anshul', 'is', 'my', 'only', 'friend']

# join elements of text with space
print(' '.join(text))

"""4.WAP: 

Given a string S, the task is to determine whether the string starts and ends with the characters 'gfg' (case insensitive). In order to complete this task, you need to utilize the string functions S.lower(), S.upper(), S.startswith('string2'), and S.endswith('string2'). By using these functions, you can check if the given string S meets the specified conditions of starting and ending with 'gfg'.
"""
s = 'GfGeeksforGeeKsGFG'
print(s.lower().startswith('gfg') and s.lower().endswith('gfg'))



"""
5.WAP: Given a string s which may contain lowercase and uppercase characters. The task is to remove all duplicate characters from the string and find the resultant string. The order of remaining characters in the output should be same as in the original string.
"""
def remove_duplicates(s):                # Define a function that takes a string `s` as input
    result = ""                          # Initialize an empty string to store the final result without duplicates
    
    for ch in s:                         # Loop through each character `ch` in the input string
        found = False                    # Assume `ch` is not found in result yet
        for r in result:                 # Loop through each character `r` in the current result string
            if ch == r:                  # If current character `ch` is already in result
                found = True             # Mark as found
                break                    # No need to check further, break the inner loop
        if not found:                    # If character was not found in result
            result += ch                # Append the character to result string
            
    return result                        # Return the final string with duplicates removed

# Example
s = "engineering"                        # Input string to test the function
print(remove_duplicates(s))  

# Call the function and print result => Output: "enginr"

"""6.WAP: Write a Python program to Given a string s, you need to reverse it.


"""
str = input("enter string: ")
print(str[::-1])

"""
7.WAP:Given a string s, you need to check if it is palindrome or not.

A palidrome is a string that reads the same from front and back.

SET reverse_string = empty string

FOR i from length of S - 1 down to 0 DO
    reverse_string = reverse_string + S[i]
END FOR

IF reverse_string is equal to S THEN
    PRINT "Palindrome"
ELSE
    PRINT "Not a Palindrome"
END IF

END

"""


str1 = input("enter a string: ")         # Take input from the user
reverse_string = ""                      # Initialize empty string for reversed version

# Reverse the string manually
for i in range(len(str1) - 1, -1, -1):    # Loop from last index to 0
    reverse_string = reverse_string + str1[i]  # Append characters in reverse order

# Check once after reversing is complete
if str1 == reverse_string:
    print("Palindrome")
else:
    print("Not palindrome")
    
    
""""
8.WAP: Given a list of words, S followed by two specific words, word1 and word2, the task is to find the minimum distance between the indices of these two words in the list.

Note: word1 and word2 are both in the list, and there can be multiple occurrences of words in the list.

"""
S = input("Enter words separated by space: ").split()
word1 = input("Enter word1: ")
word2 = input("Enter word2: ")

min_distance = len(S)         # Initialize with max possible distance
index1 = -1                   # Latest position of word1
index2 = -1                   # Latest position of word2

# Loop over the list to track positions
for i in range(len(S)):
    if S[i] == word1:
        index1 = i            # Update latest index of word1
    elif S[i] == word2:
        index2 = i            # Update latest index of word2

    # If both indices are found, update min_distance
    if index1 != -1 and index2 != -1:
        distance = abs(index1 - index2)
        if distance < min_distance:
            min_distance = distance

print("Minimum Distance:", min_distance)

""""
9. WAP: Given an n-digit large number n in form of string, check whether it is divisible by 7 or not. Return 1 if divisible by 7, otherwise 0.



"""
n = int(input("enter num: "))
if n // 7:
    print(1)
else:
    print(0)

""""sumary_line

10. WAP: Program to find Smallest and Largest Word in a String


"""
str = input("enter a sring: ")
words = str.split()
smallest = min(words, key=len)
largest = max(words, key=len)
print("Smallest Word:", smallest)   
print("Largest Word:", largest)

""" 
11.WAP Given two strings s1 and s2 consisting of only lowercase English letters and of equal length, check if these two strings are isomorphic to each other.
If the characters in s1 can be changed to get s2, then two strings, s1 and s2 are isomorphic. A character must be completely swapped out for another character while maintaining the order of the characters. A character may map to itself, but no two characters may map to the same character.

Input: s1 = "aab", s2 = "xxy"
Output: true
Explanation: Each character in s1 can be consistently mapped to a unique character in s2 (a → x, b → y).
Function areIsomorphic(s1, s2):
    If length of s1 is not equal to length of s2:
        Return False

    Create empty dictionary map_s1_to_s2
    Create empty set used_characters_in_s2

    For each index i from 0 to length of s1 - 1:
        char1 = s1[i]
        char2 = s2[i]

        If char1 is in map_s1_to_s2:
            If map_s1_to_s2[char1] is not equal to char2:
                Return False
        Else:
            If char2 is already in used_characters_in_s2:
                Return False
            Add mapping: map_s1_to_s2[char1] = char2
            Add char2 to used_characters_in_s2

    Return True

"""

        
def areIsomorphic(s1, s2):
    if len(s1) != len(s2):
        return False

    map_s1_to_s2 = {}
    used_characters_in_s2 = set()

    for i in range(len(s1)):
        char1 = s1[i]
        char2 = s2[i]

        if char1 in map_s1_to_s2:
            if map_s1_to_s2[char1] != char2:
                return False
        else:
            if char2 in used_characters_in_s2:
                return False
            map_s1_to_s2[char1] = char2
            used_characters_in_s2.add(char2)

    return True

# Input and function call
s1 = input("Enter 1st string: ")
s2 = input("Enter 2nd string: ")
print("Isomorphic:", areIsomorphic(s1, s2))

""""11. Two strings are called k-anagrams if both of the below conditions are true.
1. Both have same number of characters.
2. Two strings can become anagram by changing at most k characters in a string.

🔠 What Are Anagrams?
Two strings are anagrams if:

They have the same characters with the same frequency, but the order of characters can differ.

🔹 Example:

"listen" and "silent" → ✅ They are anagrams.

"hello" and "holle" → ✅ They are anagrams.


Function areKAnagrams(str1, str2, k):
    If length of str1 != length of str2:
        Return False
    
    freq1 = frequency count of characters in str1
    freq2 = frequency count of characters in str2

    diff = 0
    For each character c in freq1:
        If freq1[c] > freq2.get(c, 0):
            diff += freq1[c] - freq2.get(c, 0)

    If diff <= k:
        Return True
    Else:
        Return False

"""
str1 = input("str1: ")
str2 = input("str2: ")
k = int(input("Enter value of k: "))  # Taking k as input
diff = 0  # Global variable won't work inside function directly

def count(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return freq

def areAnagrams(str1, str2, k):
    if len(str1) != len(str2):
        return False  # Not same length means can't be k-anagrams

    freq1 = count(str1)
    freq2 = count(str2)

    diff = 0  # Declare diff inside function

    for c in freq1:
        if freq1[c] > freq2.get(c, 0):
            diff += freq1[c] - freq2.get(c, 0)

    # If total characters to be changed is less than or equal to k
    if diff <= k:
        return True
    else:
        return False  # Typo was here: 'retrun' → 'return'

# Call the function and print the result
if areAnagrams(str1, str2, k):
    print("Yes, they are k-anagrams")
else:
    print("No, they are not k-anagrams")
 # type: ignore
  
"""13.WAP
Given a string s, check if it is a "Panagram" or not. Return true if the string is a Panagram, else return false.

A "Panagram" is a sentence containing every letter in the English Alphabet either in lowercase or Uppercase.
"""        
s = input("enter a string: ")
def panagram(s):
     alphabet = "abcdefghijklmnopqrstuvwxyz"    # All lowercase English letters to check against

     s = s.lower()     # Convert input string to lowercase to make the check case-insensitive

     for char in alphabet:    # Iterate through each character in the alphabet

         if char not in s:        # If any character from alphabet is not in the string, it's not a pangram

             return False
         return True    # If all characters are found, return True

print(panagram(s))     
         
""" 14. Given a string s and a string dictionary d, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

Function isSubsequence(word, s):
    i ← 0
    j ← 0
    while i < length of word and j < length of s:
        if word[i] == s[j]:
            i ← i + 1
        j ← j + 1
    return i == length of word

Function findLongestWord(s, d):
    result ← ""
    for word in d:
        if isSubsequence(word, s):
            if length of word > length of result:
                result ← word
            else if length of word == length of result and word < result:
                result ← word
    return result

""" 

               

# Input the dictionary as a list of words
d = input("Enter dictionary words separated by space: ").split()

# Input the main string
s = input("Enter string: ")

# Function to check if word is a subsequence of s
def subSeq(word, s):
    i, j = 0, 0
    while i < len(word) and j < len(s):
        if word[i] == s[j]:
            i += 1
        j += 1
    return i == len(word)

# Function to find the longest word in dictionary d that is a subsequence of s
def longestWord(s, d):
    result = ""
    for word in d:
        if subSeq(word, s):
            if len(word) > len(result):
                result = word
            elif len(word) == len(result) and word < result:
                result = word
    return result

# Print the result
print(longestWord(s, d))

    




           
"""15. Given two strings s1 and s2. Return true if the string s2 can be obtained by rotating (in any direction) string s1 by exactly 2 places, otherwise, false.

Note: Both rotations should be performed in same direction chosen initially.

Examples:

Input: s1 = "amazon", s2 = "azonam"
Output: true
Explanation: "amazon" can be rotated anti-clockwise by two places, which will make it as "azonam"

FUNCTION isRotated(s1, s2):
    IF length of s1 is not equal to length of s2:
        RETURN False

    clockwise = last 2 characters of s1 + first (length - 2) characters of s1
    anticlockwise = substring from index 2 to end of s1 + first 2 characters of s1

    IF s2 == clockwise OR s2 == anticlockwise:
        RETURN True
    ELSE:
        RETURN False


"""
s1 = input("str1: ")
s2 = input("str2: ")
def isRotate(s1, s2):
    if len(s1) != len(s2):
        return False
    ck = s1[-2:] + s1[:-2]
    anticlockwise = s1[2:] + s1[:2]
    if s2 == ck or s2 == anticlockwise:
        return True
    else:
        return False
print(isRotate(s1, s2))
    


"""16.Given a string s consisting of lowercase english alphabets, the task is to find the number of distinct subsequences of the string

FUNCTION countDistinctSubsequences(s):
    n = length of s
    CREATE array dp of size n + 1
    dp[0] = 1   // Empty string has 1 subsequence (empty)

    CREATE dictionary last_occurrence

    FOR i FROM 1 TO n:
        dp[i] = 2 * dp[i - 1]   // Every subsequence can either include or exclude s[i-1]

        char = s[i - 1]

        IF char has occurred before:
            // Subtract the count before its previous occurrence
            dp[i] = dp[i] - dp[last_occurrence[char] - 1]

        UPDATE last_occurrence[char] = i

    RETURN dp[n]

"""


s = input("Enter string: ")

def countSubSeq(s):
    n = len(s)
    
    # dp[i] will store the number of distinct subsequences using first i characters
    dp = [0] * (n + 1)
    dp[0] = 1  # Base case: empty string has 1 subsequence (empty one)

    last_occur = {}  # Dictionary to store last occurrence of each character

    for i in range(1, n + 1):
        char = s[i - 1]

        # Every subsequence without s[i-1] + every subsequence with s[i-1]
        dp[i] = 2 * dp[i - 1]

        # If the character has appeared before, subtract the overcount
        if char in last_occur:
            # Subtract the count before its last occurrence
            dp[i] -= dp[last_occur[char] - 1]

        # Update last seen position of the character
        last_occur[char] = i

    return dp[n]

print("Number of distinct subsequences:", countSubSeq(s))

       
"""
17. s = input("Enter string: ")

Given two binary strings s1 and s2 consisting of only 0s and 1s. Find the resultant string after adding the two Binary Strings.

"""
s1 = input()
s2 = input()
result = bin(int(s1, 2) + int(s2, 2))[2:]
print(result)
 
"""18. Given a string s, return the length of the longest palindromic subsequence.

A subsequence is a sequence that can be derived from the given sequence by deleting some or no elements without changing the order of the remaining elements.

A palindromic sequence is a sequence that reads the same forward and backward.

Examples:

Input: s = "bbabcbcab"
Output: 7
Explanation: Subsequence "babcbab" is the longest subsequence which is also a palindrome.
"""   







   
"""19. Given a string s, find the length of the longest substring without repeating characters.

Examples:

Input: s = "geeksforgeeks"
Output: 7
Explanation: Longest substring is "eksforg".


function longestUniqueSubstringLength(s):
    create a set to store characters
    max_length = 0
    start = 0

    for end from 0 to length of s - 1:
        while s[end] is in set:
            remove s[start] from set
            start = start + 1

        add s[end] to set
        max_length = max(max_length, end - start + 1)

    return max_length

"""
s = input("Enter string: ")

def longestUniqueSubstring(s):
    char_set = set()  # Use an actual set for faster lookup
    max_len = 0
    start = 0

    for end in range(len(s)):
        while s[end] in char_set:
            char_set.remove(s[start])  # Remove the character at 'start' from set
            start += 1  # Move the window forward

        char_set.add(s[end])  # Add current character to the set
        max_len = max(max_len, end - start + 1)  # Update max length

    return max_len

print("Length of longest unique substring:", longestUniqueSubstring(s))
       

"""20. Given a string s consisting only lowercase alphabets and an integer k. Find the count of all substrings of length k which have exactly k-1 distinct characters.

Examples:

Input: s = "abcc", k = 2
Output: 1
Explaination: Possible substring of length k = 2 are,
ab : 2 distinct characters
bc : 2 distinct characters
cc : 1 distinct characters
Only one valid substring so, count is equal to 1
"""
s = input("string s consisting only lowercase alphabet: ")
k = int(input("enter k: "))

def countKMinus1DistinctSubstrings(s, k):
    count = 0

    for i in range(len(s) - k + 1):  # Slide a window of length k
        substr = s[i:i+k]  # Get substring of length k
        unique_chars = set(substr)  # Get unique characters in substring

        if len(unique_chars) == k - 1:
            count += 1

    return count

print("Count:", countKMinus1DistinctSubstrings(s, k))
    


"""21. Given two strings A and B, you need to find the last occurrence ( 1 based indexing) of string B in string A.


Example 1:

Input:
A = abcdefghijklghifghsd
B = ghi
Output:
13
Explanation:
ghi occurs at position 13 for the
last time in string A.
"""
A = input("str: ")
B = input("str: ")
last_index = A.rfind(B)

# Convert to 1-based index if found
if last_index != -1:
    print(last_index + 1)
else:
    print(-1) 



"""22. Given a string S which only contains lowercase alphabets. Find the length of the longest substring of S such that the characters in it can be rearranged to form a palindrome.


Example 1:

Input:
S = "aabe"
Output:
3
Explanation:
The substring "aab" can be rearranged to
"aba" which is the longest palindrome
possible for this String.
"""
def longest_palindromic_rearrangeable_substring(s):
    from collections import defaultdict

    # Initialize
    mask = 0  # Current bitmask (parity of character frequencies)
    seen = {0: -1}  # Mask seen at index -1 (before starting)
    max_len = 0

    for i, ch in enumerate(s):
        # Toggle bit for current character
        bit = ord(ch) - ord('a')
        mask ^= (1 << bit)

        # Case 1: same mask seen before (all even counts)
        if mask in seen:
            max_len = max(max_len, i - seen[mask])
        else:
            seen[mask] = i

        # Case 2: try all masks with one bit flipped (one odd count)
        for j in range(26):
            temp_mask = mask ^ (1 << j)
            if temp_mask in seen:
                max_len = max(max_len, i - seen[temp_mask])

    return max_len

# Example usage
s = input("Enter string: ")
print("Length of longest rearrangeable palindrome substring:", longest_palindromic_rearrangeable_substring(s))








"""23. Given a string s consisting of opening and closing parenthesis '(' and ')'. Find the length of the longest valid parenthesis substring.

A parenthesis string is valid if:

For every opening parenthesis, there is a closing parenthesis.
The closing parenthesis must be after its opening parenthesis.
Examples :

Input: s = "((()"
Output: 2
Explanation: The longest valid parenthesis substring is "()"
"""

def longestValidParentheses(s):
    stack = [-1]  # Base index for calculating length
    max_len = 0

    for i, ch in enumerate(s):
        if ch == '(':
            stack.append(i)  # Push index of '('
        else:
            stack.pop()  # Try to match with last '('
            if not stack:
                stack.append(i)  # Set new base index
            else:
                # Valid substring from top index + 1 to current index
                max_len = max(max_len, i - stack[-1])

    return max_len

# Example usage
s = input("Enter string of parentheses: ")
print("Length of longest valid parentheses substring:", longestValidParentheses(s))



"""24. Given a string str of length N which consists of only 0, 1 or 2s, count the number of substring which have equal number of 0s, 1s and 2s.
 

Example 1:

Input: str = “0102010”
Output: 2
Explanation: Substring str[2, 4] = “102” and
substring str[4, 6] = “201” has equal number
of 0, 1 and 2 
"""
def count_equal_012_substrings(s):
    from collections import defaultdict

    # Initialize counts and hash map
    count_0 = count_1 = count_2 = 0
    result = 0
    hash_map = defaultdict(int)
    hash_map[(0, 0)] = 1  # to count substrings from beginning

    for ch in s:
        if ch == '0':
            count_0 += 1
        elif ch == '1':
            count_1 += 1
        elif ch == '2':
            count_2 += 1

        # Calculate the difference
        diff_0_1 = count_0 - count_1
        diff_0_2 = count_0 - count_2

        # If this diff pair has been seen before, add its frequency
        result += hash_map[(diff_0_1, diff_0_2)]

        # Increment the frequency of this diff pair
        hash_map[(diff_0_1, diff_0_2)] += 1

    return result

# Example
s = "102201"
print(count_equal_012_substrings(s))  # Output: 2
