A = input("str: ")
B = input("str: ")
last_index = A.rfind(B)

# Convert to 1-based index if found
if last_index != -1:
    print(last_index + 1)
else:
    print(-1) 