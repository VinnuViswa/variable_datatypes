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

b_ar5 = bytearray(b"WOWW......! This is so cool")   
print(b_ar5[0])  # 87 -> ASCII value of 'W'
