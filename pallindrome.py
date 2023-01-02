def pallidrome(sentence):
    left=0 
    right=len(sentence)-1
    while(left<right):
        if sentence[right]==sentence[left]:
            left-=1
            right+=1
            return True
        elif sentence[right]!=sentence[left]:
            return False
            break
G=input("Enter string")
ans=pallidrome(G)
if ans==True:
    print("Pallindrome")
elif ans==False:
    print("Not Pallindrome")
