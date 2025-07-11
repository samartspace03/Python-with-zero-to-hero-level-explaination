#python VARIABLES
#In Python, a variable is like a container or a box that stores some value.

#🧠 Think of it like this:
#water_bottle = water
#SO SAME in DATA : a = [mango, banana, grapes]
#Just like you store water in a bottle and label it "Water", in Python you store data in a variable and give it a name.

pencil = "Apsara, Natraj , Doms"
notebook = "Maths"
bottle = "Water"

print("My fav pencils are", pencil)
print("Notebook is for", notebook)
print("I drink", bottle)

#Variable Name: Like a label or a tag on a box.

#Value: What is stored inside the box.

#Use: Variables help us remember and use values again and again.
#Example: Mobile Recharge

user_name = "Samruddhi"
balance = 250
recharge_amount = 149

balance = balance - recharge_amount

print("Hello", user_name)
print("Remaining balance:", balance)

# output: Hello Samruddhi \n Remaining balance: 101
#Rules for Naming Variables:
#1. To use variables effectively, we must follow Python’s naming rules:

#2. Variable names can only contain letters, digits and underscores (_).
#3. A variable name cannot start with a digit.
#4. Variable names are case-sensitive (myVar and myvar are different).
#5.Avoid using Python keywords (e.g., if, else, for) as variable names.

#TYPE CASTING 
#Type Casting a Variable
#Type casting refers to the process of converting the value of one data type into another.
s = "10"  # Initially a string
n = int(s)  # Cast string to integer
cnt = 5
f = float(cnt)  # Cast integer to float
age = 25
s2 = str(age)  # Cast integer to string

# Display results
print(n)  
print(f)  
print(s2)

#GET TYPE OF VAR
f = 3.14
print(type(f)) #<class 'float'>

#OBJECT REFERENCE IN PY
x = 5
y = x
print(y)
#Python variables hold references to objects, not the actual objects themselves.
#Reassigning a variable does not affect other variables referencing the same object unless explicitly updated.
x = 5
y = 'geek'
y = 'comp'
print(y)# so here what happened previous y value got as garbage value and comp as new updated one print as y

# delete a var using del() fun
x = 6
print(x)
del x
print(x)
#del x removes the variable x from memory.
#After deletion, trying to access the variable x results in a NameError, indicating that the variable no longer exists.
