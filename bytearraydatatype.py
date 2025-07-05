# BYTEARRAY :-
      # 1) It is mutable
        # 2) It is used to store binary data
        # # 3) It can be modified after creation
        
# CREATE A BYTEARRAY DATATYPE :-

# from list of integers

# b_ar1 = bytearray([120, 119, 118, 117, 116, 115])
# print(b_ar1)  # bytearray(b'xxwvuts')
# print(type(b_ar1))  # <class 'bytearray'>

# print('-------------------')

# # from bytes literal

# b1 = b"HEllo"
# b_ar2 = bytearray(b1)
# print(b_ar2)  # bytearray(b'HEllo')
# print(type(b_ar2))  # <class 'bytearray'>

# print('-------------------')

# # from string with encoding

# str1 = "HYMA"
# b_ar3 = bytearray(str1, 'utf-8')
# print(b_ar3)  # bytearray(b'HYMA')
# print(type(b_ar3))  # <class 'bytearray'>

# print('-------------------')

# # from range of integers

# b_ar4 = bytearray(4)  
# print(b_ar4)  # bytearray(b'\x00\x00\x00\x00')
# print(type(b_ar4))  # <class 'bytearray'>

# ACCESSING AND MODIFYING BYTEARRAY ELEMENTS:

# b_ar5 = bytearray(b"WOWW......! This is so cool")   
# print(b_ar5[0])  # 87 -> ASCII value of 'W'
# print(b_ar5[-3])  # 111 -> ASCII value of 'o'
# print(b_ar5[0:4])  # bytearray(b'WOWW')

# b_ar5[0] = 65 # (b'AWWW......! This is so cool')

# APPENDING AND EXTENDING BYTEARRAY:

b_ar6 = bytearray(b"HELLO")
# b_ar6.append(87)
# b_ar6.append(90)
# print(b_ar6) # bytearray(b'HELLOWZ')

# b_ar6.extend([97,98,99,100])
# print(b_ar6)  # bytearray(b'HELLOabcd')

# DELETING ELEMENTS FROM BYTEARRAY:

# del b_ar6[0]  # Deletes the first element
# print(b_ar6)  # bytearray(b'ELLOabcd')
# del b_ar6[-1]  # Deletes the last element
# print(b_ar6)  # bytearray(b'ELLOabc')
# del b_ar6[0::] # Deletes all elements
# print(b_ar6)  # bytearray(b'') - Now it's empty
