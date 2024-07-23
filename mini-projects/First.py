from re import X


a = "Hello"
print(a)

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = "Hello, World"
print(a[1])

txt = "The Bestthing in a life is free"
if "expensive" not in txt:
    print("False")


b = "Hello, World"
print(b[2:])

a = "Hello, Python"
print(a.lower())

a = "Hello, World"
print(a.replace("H", "J"))

#Split string
a = "Hello, World"
print(a.split(","))

#String conmcenatation
a = "Hello"
b = "World"
c = a + "" + b
print(c)

#F-strings
age = 36
txt = f"My name is Aliya, I am {age}"
print(txt)

price = 59
txt = f"The price is {price} dollars"
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

txt= f"The price is {20*59} dollars"
print(txt)

print(100 + ~3)


#logical not, operator precedence

print(5==4+1)
#Output true

print(not 5 == 5)
#output false

thislist = ["apple", "banana", "cherry"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
print(len(thislist))
#output 3


list1 = ["apple", "banana", "cherry"]
list2 = [1 , 5, 7, 9, 3]
list3 = [True, False, True]

print(list1)
print(list2)
print(list3)



fruits  = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)
        
print(newlist)


#with one sentence
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)
#newlist = [expression for item in iterable if condition == True]


newlist = [x for x in range(10)]
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = ['hello' for x in fruits]
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange"  for x in fruits]
print(newlist)

"""
sort list apphanumerically
"""
#sort ascending
thislist = ["orange", "mango" , "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#sort descending
thislist = ["orange", "mango" , "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

"""
customize sort function
"""

def myfunc(n):
    return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)