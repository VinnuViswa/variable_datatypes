# SET DATA TYPE 

# what is a set datatype ?
    # A set is a collection of unique elements.

# What is mean by unique ?
    # unique means no duplicate.
    
# 1, 4, 2, 8, 9, 1 ,4

# How to create a set ?

# 1)  {}

# Create Empty Set 
# set1 = {1}
# print(set1)
# print(type(set1))

# Create a Set 

# set2 = {1, 2, 3, 4, 5, 6}
# print(set2)
# print(type(set2))

# Set does remove duplicates automatically, 
# it does not maintain duplicates.
# set3 = {1, 2, 3, 1, 5, 4, 3}
# print(set3)
# print(type(set3))

# set contains only those datatypes which are immutable.
# set4 = {1, 2.5, 6+7j, "Apple", True, (1, 2, 3), (5, 9, 7, 8)}
# print(set4)
# print(type(set4))

# Set is an unordered data type.
# Set does not support indexing
# set elements are placed randomly

# set5 = {34, 2, 90, 67, True}
# print(set5)

# Create a set with the help of set()

# set6 = set('APPLE')
# print(set6)

# set7 = set([12, 23, 34, 45])
# print(set7)

# set8 = set(('A', 'm', 'G', 9, 6, True))
# print(set8)

# set9 = set({1:1, 2:4, 3:9, 4:16})
# print(set9)

# set10 = set({1:1, 2:4, 3:9, 4:16}.values())
# print(set10)

# s1 = set()
# print(s1)
# print(type(s1))

###########################


#  How to check wether the element is a part of set or not

# set1 = {12, 23, 34, 45, 56, 78}
# print(78 in set1)
# print(90 in set1)

# ADD & REMOVE ELEMENTS FROM SET

# ADD

# set2 = {100, 200, 300, 400, 200, 100}
# set2.add(1000)
# print(set2)
# set2.add("A")
# print(set2)

# Adding of multiple elements in set using update()

# set2.update("APPLE")
# print(set2)
# set2.update([20, 30 ,40])
# set2.update((9, 8, 7))
# set2.update({1, 2, 3})
# set2.update({1:1, 2:2, 3:3})
# print(set2)

# REMOVE

# set2.remove(100)
# set2.remove(500)  # KeyError: 500
# set2.remove(200)
# print(set2)

# set2.clear()
# print(set2)
# print(type(set2))

# set3 = {}
# print(set3)
# print(type(set3))

# set4 = {'a', 'c', 'f', 'l', 'm', 'k'}
# print(set4.pop())

set1 = {12, 23, 34, 45}
set2 = {12, 90, 67, 45}

# UNION OPERATION :-

# set3 = set1 | set2
# print(set3)
# print(type(set3))

# INTERSECTION :-

# set4 = set1 & set2
# print(set4)
# print(type(set4))

# DIFFERENCE :-

# set5 = set1 - set2
# set6 = set2 - set1
# print(set5)
# print(set6)

# SYMMETRIC DIFFERENCE

# set7 = set1 ^ set2
# print(set7)

###################################

# SOME OTHER OPERATIONS ON SETS :-

set1 = {100, 200, 300, 400, 500}
set2 = {400, 500, 600, 700, 800}

#union
# s = set1 | set2  # 100, 200 ,300, 400, 500, 600, 700, 800
# # intersection
# set1 & set2 # 400, 500
# # Differecnce
# set1 - set2 # 100, 200, 300
# set2 - set1 # 600, 700, 800
# # symmetric difference
# set1 ^ set2 # 100, 200, 300, 600, 700, 800

# isdisjoint()

# print(set1.isdisjoint(set2))
# print(set2.isdisjoint(set1))

# set3 = {'A', 'B', 'C'}
# set4 = {'a', 'b', 'c'}

# print(set3.isdisjoint(set4))

# x.difference_update(y)

# set1.difference_update(set2)
# print(set1)

# set2.difference_update(set1)
# print(set2)

# x.intersection_update(y)

# set1.intersection_update(set2)
# print(set1)

# set2.intersection_update(set1)
# print(set2)

# isSubset & isSuperset

set5 = {'A', 'B', 'C'}
set6 = {'A', 'B', 'C', 'D', "E", 'F'}

# print(set6.issubset(set5))
# print(set5.issubset(set6))
# print(set6.issuperset(set5))
# print((set5.issuperset(set6)))

# x.symmetric_difference_update(y)

set7 = {1, 2, 3}
set8 = {3, 4, 5}

set7-set8 # 1,2
set8-set7 # 4,5
set7^set8 # 1,2,4,5

# set7.symmetric_difference_update(set8)
# set8.symmetric_difference_update(set7)
# print(set7)
# print(set8)