import random as rn

num = rn.randint(0 , 100)
guess = int(input("guess a number: "))
compt=1

while guess != num :
    if guess>num :
        print ("less than " , guess)
    
    if guess<num :
        print ("greater than " , guess)

    guess = int(input("enter your guess : "))
    compt=compt+1

print("you won")
print("you needed " , compt , "try to find te number")