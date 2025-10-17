''' finding sum of first n numbers using while loop '''

n = 5 
s = 0 

for i in range(n):
    print(i)
    s += i  
else:
    print("Sum: " + str(s))


print("\nBy while loop")
num = 7
sum = 0 
i = 1
while i <= 5 :

    sum += i 
    i += 1
    

print("Total sum:", sum)
# lists = []
# M = int(input('Enter number: '))
# lists.append(M)
# print(lists)
# x = int(input("How many elements you want in your list: "))

# for i in range(x):
#    M = int(input('Enter number at ' + str(i) + ' index: '))
#    lists.append(M)
# else:
#    print("Final list" , lists)   

