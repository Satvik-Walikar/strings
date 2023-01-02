def counting(sentence):
    vowel=0
    consonant=0
    space=0
    sentence=sentence.lower()
    for i in range(len(sentence)):
        
        if sentence[i]=='i' or sentence[i]=='a' or sentence[i]=='e' or sentence[i]=='o' or sentence[i]=='u':
            vowel+=1
        elif sentence[i]>'a' and sentence[i]<'z':
            consonant+=1
        elif sentence[i]==' ':
            space+=1
    print("NUmber of vowels",vowel)
    print("NUmber of Consonants",consonant)
    print("NUmber of space",space)
G=input("Enter string: ")
counting(G)
