from codecs import ascii_decode
from ctypes.wintypes import LARGE_INTEGER


b = "Hello, World!"
# slice string_NAME[start:stop], excluding the stop
print(b[2:5])

print(b[:5])

print(b[2:])

print(b[-5:-2])

asc = ord('a')
print(asc)


def myupper(str):
    newStr = ""
    for letter in str: 
        x = ord(letter)
        if x in [97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123]:
                newStr += letter.upper()
        else:
                newStr += letter
        print(newStr)    
    print(newStr)    

myupper("Hello World");