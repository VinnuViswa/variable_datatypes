# ** WELCOME TO YOUR FIRST TEST ON VARIABLE DATA TYPES**


# 1) Explain the difference between int, float & complex
# 2) What type of data type is string ?
# 3) str1 = "iuhgSDFGHiuejfdSDX"   --> use this string and 
#    form a string with only  capital letters of str1.
# 4) str2 = "123456789"  --> get 642 from str2 by slicing [+ve]
# 5) str3 = "All is well"  --> convert this string to "Well is all"


# 6) l1 =  [[12,  23, 34], ['A', 'C', 'J'], 'Apple', True]
#    use l1 and create a new list [23, 'elppA', c]

# 7) use l1 and get the index of 'J'

# 8) t1 = ('1234', '4567', '09887')
# use t1 and get '7654'

# 9) t2 = (1, 2, 3, 2, 1, 3, 4, 5, 6, 4, 9, 7, 6, 5, 9)
# # get the highest number from t2 and get the count of it too.

# 10) create a nested dictionary 

# 11) create a dictionary from two different lists, using one of the
#     method of list initialization.

# // 12) dict2 = {
# //     "person" :{
# //         "name": "shiv",
# //         "city": "latur",
# //         "salary": 22400
# //         fav_food:{
# //             1: 'dal-rice',
# //             2: 'kesari bhat'
# //         }
# //     }
# // }
# what is the first favourate food of shiv.

# 1) Explain the difference between int, float & complex

# ANSWERS :-

# INTEGER data type:- 
    # Integer is numeric data type.
    # It contains values of negative numbers, positive numbers and zero.
    # Examples :- -3, 5, 9, 0, -232.

# FLOAT data type :-
    # It is also a numeric data type.
    # It contains the value of decimal or fractions.
    # It contains negative and positive numbers.
    # Examples :- 0.3, -59.838.

# COMPLEX data type :-
    # It is numeric data types
    # It is a combination of real and imaginary numbers.
    # Imaginary are represented as with suffix 'j' in python and where j stands for underroot of -1
    # Real numbers are float and integer.
    # Examples :- 3+1j, 3-3j .
    
# 2) What type of data type is string ?

# STRING data type :-
    # String contain sequence of characters.
    # It is Ordered data type
    # It supports indexing
    # It is immutable data type
    # It can be created in single quotes and double quotes
    # Examples :- 'Apple', 'Jayamma'

# 3) str1 = "iuhgSDFGHiuejfdSDX"   --> use this string and 
#    form a string with only  capital letters of str1.

# str1 = "iuhgSDFGHiuejfdSDX"
# s1 = str1[4:9:1] + str1[15::1]
# print(s1)

# 4) str2 = "123456789"  --> get 642 from str2 by slicing [+ve]

# str2 = "123456789"
# s2 = str2[5::-2]
# print(s2)

# 5) str3 = "All is well"  --> convert this string to "Well is all"

# str3 = "All is well"
# s3 = str3.replace('All is well', 'Well is all')
# print(s3)

# 6) l1 =  [[12,  23, 34], ['A', 'C', 'J'], 'Apple', True]
#    use l1 and create a new list [23, 'elppA', c]

# l1 =  [[12,  23, 34], ['A', 'C', 'J'], 'Apple', True]
# l_1 = l1[0][1] 
# l_2 = l1[2][4::-1] 
# l_3 = l1[1][1].lower()
# l_4 = [l_1, l_2, l_3]
# print(l_4)

# 7) use l1 and get the index of 'J'

# print(l1[1][2])

# 8) t1 = ('1234', '4567', '09887')
# use t1 and get '7654'

# t1 = ('1234', '4567', '09887')
# print(t1[1][3::-1])

# 9) t2 = (1, 2, 3, 2, 1, 3, 4, 5, 6, 4, 9, 7, 6, 5, 9)
# # get the highest number from t2 and get the count of it too.

# t2 = (1, 2, 3, 2, 1, 3, 4, 5, 6, 4, 9, 7, 6, 5, 9)
# print(t2[10])
# print(t2.count(9))

# 10) create a nested dictionary 

# students = {
#     "student1": {
#         "name": "Viswa",
#         "age": 22,
#         "marks": {
#             "math": 85,
#             "science": 90
#         }
#     },
#     "student2": {
#         "name": "Jayamma",
#         "age": 17,
#         "marks": {
#             "math": 45,
#             "science": 87
#         }
#     }
# }

# 11) create a dictionary from two different lists, using one of the
#     method of list initialization.

# list_1 = ['Apple', 'Banaana', 'Mango'] 
# list_2 = [49, 30, 100]
# dict_1 = dict(zip(list_1, list_2))
# print(dict_1)

#  12) dict2 = {
#    "person" :{
#        "name": "shiv",
#        "city": "latur",
#        "salary": 22400
#          fav_food:{
#              1: 'dal-rice',
#              2: 'kesari bhat'
#         }
#      }
#  }
# what is the first favourate food of shiv.

# dict2 = {
#     "person"  :{
#     "name": "shiv",
#     "city": "latur",
#     "salary": 22400,
#         'fav_food':{
#             1 : 'dal-rice',
#             2 : 'kesari bhat'
#         }
#     }
#     }
# print(dict2['person']['fav_food'][1])