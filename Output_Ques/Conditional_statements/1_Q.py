# @resource ; https://cbsepython.in/mcqs-on-flow-of-control-conditional-statements/

# Q4
list1 = [3 , 2 , 5 , 6 , 0 , 7, 9]
sum = 0
sum1 = 0

for elem in list1:
    if (elem % 2 == 0):
        sum = sum + elem
        continue
    if (elem % 3 == 0):
        sum1 = sum1 + elem

print(sum , end=" ")
print(sum1)


# Q13
x = 3

if x == 0:
    print ("Am I here?", end = ' ')
elif x == 3:
    print("Or here?", end = ' ')
else :
    pass

print ("Or over here?")

