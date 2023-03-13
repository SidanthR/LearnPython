animals = {
    "Cats" : 1,
    "Dogs" : 1,
}

a = 1
a += 1 # a = a + 1;

a = ['Cat', 'cat', 'Dog', 'Dog']
def manip(f1):
    ani = {}
    for index in f1:
        if index in ani:
            ani[index] += 1
        else:
            ani[index] = 1
    return(ani)
ret = manip(a)
print (ret)
print(len(ret))

# (inner first) 
 
# * / % //
# + -
