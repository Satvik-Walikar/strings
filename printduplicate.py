str1=input("Enter ")
HM={}
str2=" "
for i in str1:
    if i not in HM:
        HM[i]=1
    else:
        HM[i]+=1
for i in HM:
    if HM[i]>1:
        print(i,HM[i])