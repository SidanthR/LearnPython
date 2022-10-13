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
    counter = 0
    for letter in str: 
        x = ord(letter)
        if x in [97,98,99,100,123]:
                str[counter] = letter.upper()
        counter += 1

myupper("Hello World");