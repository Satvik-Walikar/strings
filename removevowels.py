def removevowels(sentence):
    sentence1=" "
    for i in range(len(sentence)):
       if sentence[i]=='i' or sentence[i]=='a' or sentence[i]=='e' or sentence[i]=='o' or sentence[i]=='u':
           continue
       else:
           sentence1+=sentence[i]
    print(sentence1)
G=input("Enter string: ")
removevowels(G)