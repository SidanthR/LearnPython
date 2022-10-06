# @ref_youtube : youtube.com/watch?v=kqtD5dpn9C8
# @author : sidanth 
# @sites for learning : 
# 1. https://www.w3schools.com/python/default.asp
# 2. https://www.learnpython.org/
# 3. https://www.geeksforgeeks.org/python-programming-language/?ref=shm


# First  = input("enter 1st no to sum: ")
# Second  = input("enter 2st no to sum: ");
# Sum = float(First) + float(Second)
#  print("Sum: " + str(Sum))


# course = "Python for Noob"
# print(course.find("o"))
# print("python" in course)


# *operator

# print(10 +  3)
# print(10 -  3)
# print(10 /  3) #float result
# print(10 // 3) #int result 
# print(10 *  3)
# print(10 ** 3) # power
# print(10 %  3) #remainder

# * arthimatic operator ( < , <=,  >, >=, ==, !=)
# * logical operator (and or not)

# # * if -elif condition
# temperator = 46
# if temperator > 30: # 
#     print("it's a hot day")
#     print("Drink plenty of water")
# elif temperator > 20: #(20, 30]
#     print("it's a nice day")
# elif temperator > 10: #(10, 20]
#     print("it's bit a cold day")
# print("DONE")

# # * exercise Weight
# weight = float(input("Weight: ") )
# choice = input( "(K)Kg or (L)Lbs: ")

# if choice.lower() == 'k':
#     print("weigth is pounds(lbs): " + str(weight * 2.205) )
# else:
#     print("weigth is kg: " + str(weight / 2.205) )

# # * while loop
# i = 1
# while i <= 10:
#     print('$' * i)
#     i += 1;

# # * list
# names = ["sid", "john", "chris", "groot", "bot"]
# print(names)
# print(names[0])
# print(names[-1]) # bot
# print(names[-2]) # groot
# print(names[0:3]) # range [0, 3) ['sid', 'john', 'chris']


# # * list methods
# numbers = [1, 2, 3, 4, 5]
# numbers.append(6)
# print(numbers)

# numbers.insert(0, -1)
# print(numbers)

# numbers.remove(3)
# print(numbers)

# # numbers.clear()
# # print(numbers)

# print(1 in numbers)
# print(len(numbers))

# for item in numbers:
#     print(item)


# * range function

# numbers = range(5)
# numbers = range(5, 10)
# numbers = range(5, 10, 2)
# print(numbers)
# for item in numbers:
#      print(item)

# # * also 
# for item in range(5):
#      print(item)
print(range(2, 2))
for n in range(2,3):
 print(n)


# * tuples (same as list but immutable (unchangeable))

# number = (1, 2, 3, 3)
# # number[0] = 10; # error 
# print(number)
# print(number.count(3) )
# print(number.index(3) )


# *The strftime() method is defined under classes date, datetime and time. 
# *The method creates a formatted string from a given date, datetime or time object.

from datetime import datetime

# current date and time
now = datetime.now()

t = now.strftime("%H:%M:%S")
print("time:", t)

s1 = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("s1:", s1)

s2 = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("s2:", s2)

# *The strptime() method creates a datetime object from a given string (representing date and time).



date_string = "20 June, 2018" 
print("date_string =", date_string) # date_string = 20 June, 2018

date_object = datetime.strptime(date_string, "%d %B, %Y") # date_object = 2018-06-21 00:00:00
print("date_object =", date_object)