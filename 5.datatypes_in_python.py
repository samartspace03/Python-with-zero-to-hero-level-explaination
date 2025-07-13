""" 
DATA TYPES IN PYTHON:


Numeric - int, float, complex
Sequence Type - string, list, tuple
Mapping Type - dict
Boolean - bool
Set Type - set, frozenset
Binary Types - bytes, bytearray, memoryview



"""

# --------------------------
# 1. Numeric Types
# --------------------------

# int: Whole number (e.g., number of customers)
num_customers = 45

# float: Decimal number (e.g., price of an item)
product_price = 299.99

# complex: Number with real and imaginary parts (e.g., used in electrical engineering)
impedance = 3 + 5j

# --------------------------
# 2. Sequence Types
# --------------------------

# str: Textual data (e.g., customer name)
customer_name = "Samruddhi"

# list: Ordered and mutable (e.g., shopping cart items)
cart_items = ["milk", "bread", "eggs"]

# tuple: Ordered and immutable (e.g., GPS coordinates)
location = (19.0760, 72.8777)

# --------------------------
# 3. Mapping Type
# --------------------------

# dict: Key-value pair (e.g., customer profile)
customer = {
    "name": "Samruddhi",
    "age": 21,
    "email": "sam@example.com"
}

# --------------------------
# 4. Boolean Type
# --------------------------

# bool: True or False (e.g., login status)
is_logged_in = True

# --------------------------
# 5. Set Types
# --------------------------

# set: Unique unordered values (e.g., skills in resume)
skills = {"Python", "SQL", "Data Analysis"}

# frozenset: Immutable set (e.g., constant tags)
config_tags = frozenset(["beta", "v1.0", "release"])

# --------------------------
# 6. Binary Types
# --------------------------

# bytes: Immutable binary data (e.g., raw file data)
data = b"Hello"

# bytearray: Mutable binary data (e.g., image bytes)
arr = bytearray([65, 66, 67])  # A, B, C in ASCII

# memoryview: Memory-efficient access to binary data
mv = memoryview(bytearray(b"Hello"))
