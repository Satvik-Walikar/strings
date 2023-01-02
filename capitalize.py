def capitalize(sentence):
    sentence1=" "
    left=0
    right=len(sentence)-1
    for i in range(len(sentence)):
        if i==left or i==right:
            sentence1+=sentence[i].upper()
        else:
            sentence1+=sentence[i]
    print(sentence1)
G=input("Enter string: ")
capitalize(G)