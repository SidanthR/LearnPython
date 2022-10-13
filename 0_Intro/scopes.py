globle_scope = 1000 #global scope
# print(g)

# local_var = 100   #global scope

def PRINT():
    local_var = 200   #local scope
    print(local_var)
    print(local_var)
    print(local_var)

print(globle_scope)
PRINT()


