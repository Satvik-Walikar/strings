def frequencyofchar(sentence):
    sentence=sorted(sentence)
    ch=sentence[0]
    count=1
    print(" Number Of Occurance of charecters")
    for i in range(1,len(sentence)):
        if sentence[i]==ch:
            count+=1
        else:
            print(ch,count,end=" ")
            count=1
            ch=sentence[i]
    print(ch,count,end=" ")
G=input("Enter string: ")
frequencyofchar(G)