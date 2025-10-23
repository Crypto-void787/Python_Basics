''' Swapping Values
        Given:

            python
            x = 8
            y = 3 '''


def swap_val(x, y):
    print("Original values: \n","x =", x, "y =", y)
    temp = x
    x = y
    y = temp
    print("values swapped!\n", "x =", x, "y =", y)



swap_val(3 ,5)

