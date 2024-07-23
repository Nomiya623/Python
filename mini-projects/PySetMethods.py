#add
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)

#clear
fruits = {"apple", "banana", "cherry"}
fruits.clear()
print(fruits)

#copy
fruits = {"apple", "banana", "cherry"}
x = fruits.copy()
print(x)

#difference
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z= x.difference(y)
print(z)

#difference_update
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference_update(y)
print(x)

#discard
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)

#intersection
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)

#intersection_update
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)


#isdisjoint()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
z = x.isdisjoint(y)
print(z)

#issubset()
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
print(z)

#issuperset
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z)

#pop
fruits = {"apple", "banana", "cherry"}
fruits.pop()
print(fruits)

#remove()
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)

#symmetric_difference()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)

"""
Remove the items that are present in both sets, AND insert the items that is not present in both sets:
"""
#symmetric_difference_update()

#union
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.union(y)
print(z)

#update
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.update(y)
print(z)
