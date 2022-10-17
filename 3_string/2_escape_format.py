#This example erases one character (backspace):
txt = "Hello\nWorld!"
print(txt) 

ph = "1234567890"
ph1 = "1234567890as"
ph2 = "1234567890$@#@"
ph3 = "1234567890[][]"

# # if ph.isnumeric():
# #     print("Its a valid no")
# # else: 
# #     print("Its not valid no")

# def isPhoneNoValid(ph):
#      if ph.isnumeric():
#          print("Its a valid no")
#      else: 
#          print("Its not valid no")

# isPhoneNoValid(ph);
# isPhoneNoValid(ph1);
# isPhoneNoValid(ph2);
# isPhoneNoValid(ph3);

# usage of Return Boolean value (TRUE FALSE)
def isPhoneNoValid(ph):
     if ph.isnumeric():
         return True;
     else: 
        return False;


if isPhoneNoValid(ph):
    print("THIS NO IS VALID IN INDIA")
else : 
    print("THIS NO IS VALID IN AUS")
isPhoneNoValid(ph1);
isPhoneNoValid(ph2);
isPhoneNoValid(ph3);