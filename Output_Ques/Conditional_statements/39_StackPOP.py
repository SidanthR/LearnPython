def Pop(st) :
    
    length = len(st)
    if length == 0:
        print("empty list")    
    else:
        poppedValue = stack[length - 1] 
        st.pop()
        return poppedValue

#  return stack[length-1]  # return 5 and exit the function
#  return None


stack = [3,4,5]
print( Pop(stack) )
print(stack)



# def passbyvalue(var):
#     var = var + 10
#     print(var) #20

# var = 10 #10
# passbyvalue(var)
# print(var)


# def passbyref(var):
#     var[0] = var[0] + 10
#     print(var) #20

# var = [10] #20
# passbyref(var)
# print(var)