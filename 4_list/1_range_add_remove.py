# Range of index list_NAME[start:stop], excluding the stop
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:5])

# print(thislist[:4])

# print(thislist[2:])

# print(thislist[-4:-1])

# thislist = ["apple", "banana", "cherry"]
# thislist.remove('banana') # thislist[1,2] = "";
# print(thislist)


# #copying list
# l1 = [1, 2, 3]
# l2 = l1;  # pass by reference 
# print (l1, l2)

# l1.insert(3,10)
# print (l1, l2)

# l2.insert(4,20)
# print (l1, l2)

#right way to copy (use copy())
l3 = [1, 2, 3]
l4 = l3.copy();

print(l3,l4)

l3.insert(3, 10);
print(l3,l4)

l4.insert(3, 20);
print(l3,l4)

