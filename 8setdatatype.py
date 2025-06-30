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

set9 = set({1:1, 2:4, 3:9, 4:16})
print(set9)

set10 = set({1:1, 2:4, 3:9, 4:16}.values())
print(set10)