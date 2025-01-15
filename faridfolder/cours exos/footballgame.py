city=int(input("goals of mancity"))
barca=int(input("goals of barca"))

if (city < 0 ) | (barca<0) : print ("impossible")
else :
    if city == barca : print("draw")
    elif city>barca : print(f"'EL ManCity wins'")
    else : print("Barca wins")