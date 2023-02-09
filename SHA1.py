import hashlib
 
# initialize a string
str = "www.MyTecBits.com"
 
# encode the string
encoded_str = str.encode()
 
# create a sha1 hash object initialized with the encoded string
obj = hashlib.sha1(encoded_str)
 
# convert the hash object to a hexadecimal value
hexa= obj.hexdigest()
 
# print
print(hexa)
