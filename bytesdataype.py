# BYTES :-
    # 1) It is a sequence of integers
    # 2) It is immutable
    # 3) 0-255
    # 4) It is used to store binary data
    
# Creating a byte datatype 
    # With the help of byte literal : -

# b1 = b'Hello World'
# print(b1)  # b'Hello World' b is prefix for creating  byte literals
# print(type(b1))  # <class 'bytes'>  

# print('-------------------')

#      # with the help of byte function :-
# b2 = bytes([65, 66, 67, 68, 69])
# print(b2)  # b'ABCDE'
# print(type(b2))  # <class 'bytes'>

# print('-------------------')

# # with the help of bytes() function with a string
# # Note: The string must be encoded to bytes, typically using UTF-8 encoding.

# b3 = bytes('Hello', 'utf-8')
# print(b3)  # b'Hello'
# print(type(b3))  # <class 'bytes'>

# print('-------------------')

#       # with the help of bytes() function with a range of integers
#       # The range should be between 0 and 255.
      
# b4 = bytes(range(97, 105))  
# print(b4)  # b'abcdefghi'
# print(type(b4))  # <class 'bytes'>


# INDEXING UPON BYTES DATATYPE :-
      # Indexing will give you the ASCII value of the character at that index.

# b5 = b'PYTHON IS GREAT'
# print(b5[0])  # 80 -> ASCII value of 'P'
# print(b5[3]) 
# print(b5[-2])  # 65 -> ASCII value of 'A'

# print('-------------------')

# SLICING UPON BYTES DATATYPE :-

# print(b5[0:6])  # b'PYTHON'

########################################################

# MODIFICATION UPON BYTES DATATYPE :-
    # Bytes are immutable, meaning you cannot change their content after creation.
# b6 = b'Hillo'
# b6[1] == 69
# print(b6)

############################################

# b7 = b"GOOBYE" # bytes datatype
# print(b7)  # b'GOOBYE'
# str1 = b7.decode('utf-8')  # Decoding bytes to string
# print(str1)  # 'GOOBYE'

########################################################

# b8 = b"HELLO WORLD, HOW ARE YOU?"
# print(b8.count(b'L'))  # Count occurrences of 'L' in bytes
# print(b8.count(b'H'))  # Count occurrences of 'H' in bytes

#############################################

# b9 = b"kfldkjhldsfdslfjhfkjdsfljdsf"  
# print(b9.find(b'f'))
# print(b9.rfind(b'f'))