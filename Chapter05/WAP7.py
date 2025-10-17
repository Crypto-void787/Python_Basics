''' searching any x number in given tuple via while loop '''

list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print(list)

x = int(input('Number you wanna search: '))

for val in list :
    if val == x :
        print( str(x) + ' Found')
        break

    print('Searching...')
        
else :
    print("Done")        