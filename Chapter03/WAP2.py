# checking a palindrome list 

list1 = []

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

list1.append(num1)
list1.append(num2)
list1.append(num3)

print("List 1:" , list1)

list1_copy = list1.copy()
list1_copy.reverse() 

if list1_copy == list1 :
    print("List 1 is palindrom")

else :
     print("List1 isn't palindrom")    

list2 = []

no1 = int(input("Enter the first number: "))
no2 = int(input("Enter the second number: "))
no3 = int(input("Enter the third number: "))

list2.append(no1)
list2.append(no2)
list2.append(no3)

print("List 2:" , list2)


print("______________________________")

list2_copy = list2.copy()
list2_copy.reverse() 


if list2_copy == list2 :
    print("List 2 is palindrom")    

else : 
    print("List 2 isn't palindrom")
