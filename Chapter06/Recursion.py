'''Recursion: 
           function call itself repeatedly '''


def show(n) :
    if(n == 0):
        return
    print(n) 
    show(n-1)
    print("End")



show(4)  