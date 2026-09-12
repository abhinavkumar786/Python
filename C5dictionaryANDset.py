marks = {
    "Abhinav": 100,
    "Rohan": 98,
    "Abhinav": 100,
}
print(len(marks))
# 2
# empty dictionary marks = {}--> it will print{}
print(marks,type(marks))

# 1. It is unordered.
# 2. It is mutable.
# 3. It is indexed.
# 4. Cannot contain duplicate keys

# first see what is print(f"")done

# if you write marks[0]-->error
# intead write marks["Abhinav"] because this key is present in the dictionary

print(marks["Abhinav"])
# 100

# DICT METHODS,, dict are mutable

print(marks.items())
# dict_items([('Abhinav', 100), ('Rohan', 98)]):

print(marks.keys())
# dict_keys(['Abhinav', 'Rohan'])

print(marks.values())
# dict_values([100, 98])

marks.update({"Abhinav":99,"Renuka":90})
print(marks)

# it can only change the values not the keys, it can also add new key values pairs

# print(marks.get("Abhi"))
# diff??
print(marks.get("Abhinav"))
print(marks["Abhinav"])

# print(marks.get("Abhinav2")) -->print None 
# print(marks("Abhinav2"))-->returns an error
# chatgpt pop,pop item
# read handbook


#SETS---->>>>


s = {1,5,5,32,"abhinav"}
#we cant repeat any value in the set and order is not maintained otherwise use list
print(s,type(s))

# we can also use other datatypes


# output:{32,1,5}
# empty set: s = set(), dont use s = {} as it will create an empty dictionary

# SET METHODS

s.add(566)

print(s,type(s))
print(len(s))
# there is no way to change items in sets?

s.remove(1)
print(s)
# print(s.pop()) returns the element removed
s.pop()
print(s)
# print(s.pop()) ?? printing the set and returning the value
s.clear()
# print(s)-->set() empty


a = {0,1,2,3,4,5}
d = {0,7,8,9,10}
print(a.union(d))


print(a.intersection(d))
# set{},{0}
print(a-d)
# subtract and give remaining elements of first set

# chatgpt subset....???


# ❌ Immutable: frozenset
# set is mutable, but frozenset is its immutable version.

marks = {
    "Math": 85,
    "English": 78,
    "Science": 92,
    "Computer": 95
}

for subject, mark in marks.items():
    print(subject, ":", mark)

total = sum(marks.values())
average = total / len(marks)

print("Total marks:", total)
print("Average marks:", average)




