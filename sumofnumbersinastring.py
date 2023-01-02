def sumofnumbers(sentence):
    sentence1=' '
    for i in range(len(sentence)):
        if sentence[i].isdigit():
            sentence1+=sentence[i]
    print(sentence1)
G=input("Enter string: ")
sumofnumbers(G)