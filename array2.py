# write a code to create an array where the user can define the length and its input element in python 
import array as arr
a = arr.array('i', [])
user = int(input("enter the length of array "))
for i  in range (user):
    x = int(input("enter element"))
    a.append(x)
print(a)