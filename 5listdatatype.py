# LIST DATA TYPE:-

name = 'Kumar'
age = 32
city = 'Hyderabad'
isGraduate = True
height = 5.9

#########
# collection Data types:-

    # 1) List

# Why we needed a list data type:-
    # Because in real time situations we need to store 
    # Multiple values in a single variable.
    
# What  type of Data type is list:-
    # List is a collection data type.
    
    # List is a mutable data type. --> Can be modified
    
    # List is an collection of ordered elements. ---> It supports Indexing
    
    # List is a heterogeneous datatype. --> The elements of list can be of multiple types.
    

# How to create a list / Initialize a list:-
    # witht the help of []
# list_1  = []
# print(list_1)
# print(type(list_1))    #<class 'list'>

# list_2 = [1, 2, 3, 4]
# print(list_2)
# print(type(list_2))

# list_3 = [12, 23.5, 8+9j, 'python', True]
# print(list_3)
# print(type(list_3))

    # with tthe help of list()
    
# list_4 = list([12, 'F', 6.5])
# print(list_4)
# print(type(list_4))

# list_5 = list((False, 78, 900, 'Battle'))
# print(list_5)
# print(type(list_5))

# list_6 = list({100, 200, 300})
# print(list_6)
# print(type(list_6))

# list_7 = list('APPLE')
# print(list_7)
# print(type(list_7))
###################################

# ACCSSING EEMENTS FROM LIST 

# l1 = ['Amol', True, 78, -900.5, [12, 34, 90]]
# print(l1)
# Access 'Amol' from l1
# print(l1[0])
# print(l1[1])
# print(l1[4])
# print(l1[-2])
# print(l1[-5])

# SLICING ON LIST

# list_alpha = [45, 90, 76, 88, 100, 22, 85, 11]

# # [88, 100, 22]
# print(list_alpha[3:6:1])
# print(list_alpha[-5:-2:1])

# # [76, 90, 45]
# print(list_alpha[2::-1])

# # 85, 100, 76
# print(list_alpha[-2:-7:-2])

# # 45, 88, 85
# print(list_alpha[0::3])


##############################################

# BUILT IN METHODS OF LIST:-

list1 = [12, 23, 34, 45, 56]

# append()
# list1.append(67)
# list1.append(False)
# list1.append('jam')
# # list1.append(90, 89) #TypeError: list.append() takes exactly one argument (2 given)
# print(list1)

########
# extend()
# list1.extend([100, 200, 300, 400])
# print(list1)

# list1.extend(True, False, 0, 1) #TypeError: list.extend() takes exactly one argument (4 given)
# list1.extend((True, False, 0, 1))
# print(list1)

# list1.extend({1.2, 2.3, 3.4})
# print(list1)

# list1.extend('APPLE')
# print(list1)

####################
list1 = [12, 23, 34, 45, 56]

# insert()

# list1.insert(0,6)
# list1.insert(3, 100)
# list1.insert(-4, 500)

# print(list1)

############################################
list1 = [12, 23, 34, 45, 56]

# remove()

# list1.remove(23)
# # list1.remove(120)  #ValueError: list.remove(x): x not in list
# list1.remove(56)
# print(list1)


list1 = [12, 23, 34, 45, 56]

# pop()
# list1.pop(3)
# print(list1.pop())
# print(list1)

# list1.clear()
# print(list1)

#################################################333

# list2 = ['apple', 23, 67, True, 1, [10, 2, 3, 4], 'apple', 67, 1, 'apple']

# print(list2)

# print(list2.index('apple'))
# print(list2.index(67))

# print(list2.rindex(67))
# print(list2.find(1))

#count()

# print(list2.count('apple'))
# print(list2.count(1))


#############################################

list3 = [12, 5, 9, 2, 1, 90, 56, 100, 45]
#sort()
# list3.sort()  # for ascending
# list3.sort(reverse=True)   # for descending
# print(list3)


# list4 = ['T', 'i', 'J', 'A', 'B', 'l', 'q', 'r']
# list4.sort(reverse=True)
# print(list4)


# copy()
# list5 = [0, 9, 8, 7, 6, 5]
# lis6= list5.copy()
# print(lis6)

# print(id(list5))
# print(id(lis6))

l1 = [1, 2, 3]
l2 = [5, 6, 7]

# list concatination
# print(l1 + l2)

# list repetation
# l3 = [12, 21, 23]
# print(l3 * 4)


################################

# l5 = [12, 23, 34]
# a, b, c = l5
# print(a)
# print(b)
# print(c)