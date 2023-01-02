str1=input("Enter the frst string ")
str2=input("Enter the second string ")
if len(str1)!=len(str2):
    count=0
else:
    str1=sorted(str1)
    str2=sorted(str2)
    for i in range(len(str1)):
        if str1[i]!=str2[i]:
            count=0
            break
        else:
            count=1
if count==0:
    print("not anagrams")
else:
    print("anagrams")
        
            
