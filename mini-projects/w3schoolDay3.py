#Tuples
"""tuple items are ordered, unchangeable, and follow duplicate values.
Tuple items are indexed, the first item has index[0], second item has index[1] etc
"""
#allow duplicates
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#tuple lenght
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#create tuple, comma
thistuple = ("apple",)
print(type(thistuple))

#data types
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
print(tuple1)
print(tuple2)
print(tuple3)

#The tuple() Constructor
thistuple = tuple(("apple", "banana", "cherry")) #note tje double round-brackets
print(thistuple)

#access tuple items
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#negative
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

#range
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "mango")
print(thistuple[2:5])
#Note: The search will start at index 2 (included) and end at index 5 (not included).

#negative indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "mango")
print(thistuple[-4:-1])

#check if item
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
     print("Yes, it is here")
     
#change tuple values
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#add items
thistuple = ("apple", "banana", "cherry")
y = ("orange", )
thistuple += y
print(thistuple)
"""
Note: When creating a tuple with only one item, 
remember to include a comma after the item, otherwise it will not be identified as a tuple.
"""
#remove items
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

#unpacking tuple
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

#Using asterisk*
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

#loop tuple
thistuple = ("apple", "banana","cherry")
for x in thistuple:
    print(x)
    
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i]) 
  
thistuple = ("apple", "banana","cherry")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1
    
#join two tuples
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1+tuple2
print(tuple3)

#multiply tuples
fuits = ("banana", "apple", "banana")
mytuple = fruits * 2
print(mytuple)