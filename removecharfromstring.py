str1=input("Enter ")
str2=input("Enter ")
str3=''
for i in str1:
    if i not in str2:
        str3+=i
print(str3)