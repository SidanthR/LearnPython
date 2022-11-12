# print ("*")
# print ("*")
# print ("*")
# print ("*")
# print ("*")

for i in range(10):
    print ("*")

for i in [0,1,2,3,4,5,6,7,8,9]:
    print ("i = : ", i)
x = 10 

# for times in [x]:
#     print ( f'5 * {x} = {5 * x}' )
#     # print ("5 * ",times, " =times ", 5 *times) 
 

# print ("starting") 
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)
  
# print ("ending") 

# for x in "banana":
#   print(x)

# ----------

# print ("starting") 
# seq = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,1000]

# for x in seq:
#     print(x)
#     if x == 10:
#         break
#         print ("ending") 
#         print ("ending") 
#         print ("ending") 
#         print ("ending") 
#         print ("ending") 
#     print("ending IF block")

# print ("Real ending") 

# # ----------

# break example 
fruits = ["apple", "banana", "cherry", "lichi", "pineapple"]
# for x in fruits:
#   if x == "pineapple":
#     break # get out of the loop
#   print(x)

if "pineappe"  in fruits:
    print("found it")
else:
    print("not found")

# # continue example 
# fruits = ["apple", "banana", "cherry", "lichi", "pineapple"]
# for x in fruits:
#   print("hello")
#   if x == "banana":
#     continue #skip this iteration and move to next iteration
#   print(x)



# #   problem 1 
# s = 'geeksforgeeks'
# # Using for loop 
# for letter in s: 
    
#     print(letter) 
#     # break the loop as soon it sees 'e' 
#     # or 's' 
#     if letter == 'e' or letter == 's': 
#         break #out of the loop
    
# print("Out of for loop") 
# print() 

# output
# g
# e
# Out of for loop
# 



# #   problem 2 
# s = 'geeksforgeeks'
# # Using for loop 
# for letter in s: 
    
#     print(letter) 
#     # break the loop as soon it sees 'e' 
#     # or 's' 
#     if letter == 'e' or letter == 's': 
#         continue
#     print("not skipped")
    
# print("Out of for loop") 
# print() 


# output
# g
# e
# e
# k
# s
# f
# o 
# r 
# g
# e
# e
# k 
# s

# output
# g
# e
# e
# k
# s
# f
# o 
# r 
# g
# e
# e
# k 
# s

# FOR ELSE CONCEPT

# for x in range(6):
#   print(x)
# else:
#   print("Finally finished!")
#   print("Still in loop !")

# Note: The else block will NOT be executed if the loop is stopped by a break statement.
# for x in range(6):
#      if x == 3: break
#      print(x)
# else:
#      print("Finally finished!")

# Nested for LOOPS
from msvcrt import open_osfhandle


# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]

# for x in adj:
#   for y in fruits:
#     print(x, y)

# print("*", end=" ")
# print("*", end=" ")
# print("*", end=" ")
# print("*", end=" ")
# print("*", end=" ")

    
# for x in range(5):
#      print("*", end=" ")
     
# print("*", end=" ")
# print("*", end=" ")
# print("*", end=" ")
# print("*", end=" ")
# print("*", end=" ")
# print("")
# print("*", end=" ")
# print("*", end=" ")
# print("*", end=" ")
# print("*", end=" ")
# print("*", end=" ")
# print("")
# print("*", end=" ")
# print("*", end=" ")
# print("*", end=" ")
# print("*", end=" ")
# print("*", end=" ")
# print("")
# print("*", end=" ")
# print("*", end=" ")
# print("*", end=" ")
# print("*", end=" ")
# print("*", end=" ")
# print("")
# print("*", end=" ")
# print("*", end=" ")
# print("*", end=" ")
# print("*", end=" ")
# print("*", end=" ")

# for x in range(5):
#      print("*", end=" ")

# for x in range(5): #outer loop (row)
#      for y in range(5): #inner loop (column)
#           print("*", end=" ")
#      print("\n") 
     
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

print(True) # 1 or > 0
print(False) #0
x = True
if 1-1:
     print("always true")
else: 
     print("Will never run")
