#34
# country = "  Who is jc HOw is doing. THere is a snake"
# str = country.strip()
# str = str.split(' ')
# print((str))
# print(len(str))



#33
country = "  Who is jc.HOw is doing.THere is a snake."
str = country.strip()
str = str.split('.')
# while("" in str):
#     str.remove("")
# print((str))
# print(len(str))
countw = 0
counth = 0
for sent in str:
    if sent == '':
        continue
    if sent[0] == 'W' or sent[0] =='w':
       countw += 1
    elif sent[0] == 'H' or sent[0] == 'h':
       counth += 1

print('W or w ', countw)
print('H or h ', counth)