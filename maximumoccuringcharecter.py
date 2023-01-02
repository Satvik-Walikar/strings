str1=input("Enter ")
str2=''
str3=''
for i in range(len(str1)-1):
    for j in str1:
        if j==str1[i+1]:
            str2+=j
    if len(str3)<len(str2):
        str3=''
        str3+=str2
        str2=''
    else:
        str2=""
print(str3,len(str3))
        