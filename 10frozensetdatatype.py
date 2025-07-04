# What type of datatype is frozenset?
    # Exactly like set datatype but immutable
    # Ut can be used as key in dictionary
    # It is hashable
    # It is unordered
    # It is randomly placed
    # It does not support indexing
    # It does not support slicing
    # only unique elements are allowed
    
    
# How to create a frozenset?

# 1) Using frozenset() constructor
# f_set1 = frozenset()
# print(f_set1)  # frozenset()
# print(type(f_set1))  # <class 'frozenset'>  

# f_set2 = frozenset("APPLE")
# print(f_set2)  # frozenset({'A', 'E', 'L', 'P'})
# print(type(f_set2))  # <class 'frozenset'>  

# print('---------------------------')

# f_set2= frozenset([12, 23, 34, 45, 55, 67, 21, 12, 23, 34])
# print(f_set2)  # frozenset({34, 12, 67, 45, 21, 23, 55})
# print(type(f_set2))  # <class 'frozenset'>

# print('---------------------------')

# f_set3 = frozenset((90, 89, 67, 'A', True, 1))
# print(f_set3)  # frozenset({True, 1, 67, 89, 90, 'A'})
# print(type(f_set3))  # <class 'frozenset'>  

# print('---------------------------')    

# f_set4 = frozenset({1.2, "w", False, 5+6j})
# print(f_set4)  # frozenset({1.2, (5+6j), False, 'w'})
# print(type(f_set4))  # <class 'frozenset'>  

# MEMBERSHIP

# f_set5 = frozenset({12, 23, 34, 45, 55, 67, 21, 54, 45, 67, 89, 90})
# print(21 in f_set5)  # True

f_1 = frozenset({12, 34, 56, 43, 21, 89, 90, 66, 58})
f_2 = frozenset([55, 23, 12, 89, 99, 55, 34, 43, 100])

# UNION

# f_3 = f_1 | f_2
# print(f_3)  # frozenset({100, 12, 21, 23, 34, 43, 55, 56, 58, 66, 89, 90, 99})
# print(type(f_3))  # <class 'frozenset'>

# INTERSECTION

f_4 = f_1 & f_2
print(f_4)  # frozenset({12, 34, 43, 89})
print(type(f_4))  # <class 'frozenset'>

# DIFFERENCE

# f_5 = f_1 - f_2
# print(f_5)  # frozenset({66, 12, 21, 56, 58, 90})
# print(type(f_5))  # <class 'frozenset'> 

# f_6 = f_2 - f_1
# print(f_6)  # frozenset({100, 23, 55, 99})
# print(type(f_6))  # <class 'frozenset'> 

# SYMMETRIC DIFFERENCE

# f_7 = f_1 ^ f_2
# print(f_7)  # frozenset({100, 12, 21, 23, 34, 43, 55, 56, 58, 66, 89, 90, 99})
# print(type(f_7))  # <class 'frozenset'> 

# x.difference(y)
# print(f_1.difference(f_2))

# x.intersection(y)
# print(f_1.intersection(f_2))

# x.symmetric_difference(y)
# print(f_1.symmetric_difference(f_2))  # frozenset({100, 12, 21, 23, 34, 43, 55, 56, 58, 66, 89, 90, 99})

# x.isdisjoint(y)
# print(f_1.isdisjoint(f_2))  # False

# x.issubset(y)
# print(f_1.issubset(f_2))  # False
# print(f_2.issubset(f_1))  # False

# x.issuperset(y)
# print(f_1.issuperset(f_2))  # False
# print(f_2.issuperset(f_1))  # False

#############################

# dict1 = {
#     frozenset("ALMOND") : "Dryfruit",
#     "Origin" : "India",
#     "Price" : 1000
# }
# print(dict1)  # {frozenset({'A', 'D', 'L', 'M', 'N', 'O'}): 'Dryfruit', 'Origin': 'India', 'Price': 1000}