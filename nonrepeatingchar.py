String=input("Enter string: ")
for i in String:
    #initialize a count variable
    count = 0
    for j in String:
        #check for repeated characters
        if i == j:
            count+=1
        #if character is found more than 1 time
        #brerak the loop
        if count > 3: #change this to count>1 to find non repeating charecter
            break
    #print for nonr epeating characters
    if count == 3: #change this to count==1 to find non repeating charecters
        print(i,end = " ")