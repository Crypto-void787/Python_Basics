# This program find out the greatest number outta 3 given numbers 

num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
num3 = int(input('Enter the third number: '))

if num1 > num2 and num1 > num3 :
    print(str(num1) + " is greater than others!")

elif num2 > num1 and num2 > num3 :
    print(str(num2) + " is greater than others!" )

else:
    print(str(num3) + " is greater than others!")