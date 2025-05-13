# Importing array
# There are multiple ways to import array
from array import array
integer_array = array('i', [1, 2, 3, 4, 5])
print(integer_array)
print(integer_array[1])

# Basic operation in array
# Append function
integer_array.append(6)
print(integer_array)
# Extend Function
a = [7,8,9]
integer_array.extend(a)
print(integer_array)
# Insert Function
integer_array.insert(0, 0)
print(integer_array)
# Pop function
integer_array.pop(2)
print(integer_array)