''' File containing number separated by comma, print the count of even numbers '''


def Even_numbers() : 
    with open("Chapter07/Files/Even.txt" , "r") as f :
        count = 0 
        data = f.read()
        numbers = data.split(',')
        print(numbers)
        for i in numbers :
            if int(i) % 2 == 0 :
                count += 1 

        print("Total even:" , count)        



def Odd_numbers() : 
    with open("Chapter07/Files/Even.txt" , "r") as w :
        count = 0
        data  = w.read() 
        numbers = data.split(',')
        for num in numbers :
            if int(num) % 2 != 0 :
                count += 1 

        print("Total odds:" , count)        



Even_numbers()
Odd_numbers()        