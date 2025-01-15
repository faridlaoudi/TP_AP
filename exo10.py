
word = input("enter a word : ")
pal = True 
d=0
f=len(word)-1

while d < f:  
    if word[d] != word[f]:  
        pal = False
        break  
    d += 1
    f -= 1

if pal : print("yes , it's palindrom")    
else : print("no , it's not palindrom")    