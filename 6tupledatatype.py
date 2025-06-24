# TUPLE DATA TYPE :-

    # Intialization :-
    
# 1) with the help of ()

# tup1 = ()
# print(tup1)
# print(type(tup1))

# tup2 = (1, "Bujji", True, [12, 23, 34], (90, 80, "Thorn"))
# print(tup2)
# print(type(tup2))

# 2) with the help of tuple() function built in method :-

# tup3 = tuple('APPLE')
# print(tup3)
# print(type(tup3)) # ('A', 'P', 'P', 'L', 'E')

# tup4 = tuple([12, True, 'Python', [12, 32, 43]])
# print(tup4)
# print(type(tup4))

# tup5 = tuple(('E', 'A', "k", "M"))
# print(tup5)
# print(type(tup5))

# tup6 = tuple({12, 23, 34, 56})
# print(tup6)
# print(type(tup6))


###################################

# tup1 = (100, 200, 300, 400, 500, 600, 700)

# INDEXING :-
    # 1) Positive indexing
# print(tup1[3])
# print(tup1[6])
# print(tup1[1])
# print(tup1[5])

    # 2) Negative indexing
# print(tup1[-4])
# print(tup1[-6])
# print(tup1[-3])

# tup2 = ("LATHA", True, [6, 7, 8, "KIRAN"], (2.3, 4.5, 1.1, ['SAMI', "Z"]), False)

# print(tup2[4])
# print(tup2[2])
# print(tup2[2][1])
# print(tup2[2][3][2])
# print(tup2[0][2])
# print(tup2[3][1])

# print(tup2[-2][-1][-1])

##############

# SLICING

# tup3 = (12, True, "AKHILA", ["J", "K", "L", "SURESH"], ((("PLUTO"), "NEPTUNE"),"MARS" ))
# print(tup3[3][3][2::]) # RESH
# print(tup3[2][2::-1]) # HKA
# print(tup3[4][0][0][-1::-1]) # OTULP

#################
# IN BUILT METHODS :-

tup4 = (1, 2, 3, 2, 1, 4, 5, 6, 7, 5, 5, 5, 8, 9, 0, 2, 4)

# COUNT :-

# print(tup4.count(5))
# print(tup4.count(2))
# print(tup4.count('Z'))

# Index()

# print(tup4.index(5))
# print(tup4.index(0))
# print(tup4.index('z'))

########################

# CONCATINATION :-

# t1 = (12, 23, 34)
# t2 = (67, 78, 89)

# print(t1 + t2)
# t3 = t1 + t2
# print(t3)

# REPETATION :-

# t =(1,2 ,3)
# print(t * 2)

# UNPACKING :-

x, y, z, m = (10, 20 , 30 ,40)
print(x)
print(y)
print(z)
print(m)