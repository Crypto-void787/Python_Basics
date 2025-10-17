#searching any x number in given tuple via while loop

tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

print("Tuple: " + str(tup))

u = int(input("Enter the you wanna find out from tuple: "))

i = 0 
while i <= len(tup) :
    if tup[i] == u :
        print("Number found! (" + str(tup[i]) + ")")
        break 

    else :
        print(tup[i])
        i += 1   