''' print all element in list using recursive funtion

   hint : 
    1- use list n index as paramenter'''

def print_list(list, index = 0) : 
    if index == len(list):
       return 
    print(list[index])
    print_list(list , (index+1))



fruits = ["apple" , "Banana" , "Grape"]    


print_list(fruits)