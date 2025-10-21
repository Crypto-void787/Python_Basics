''' Printing the elements of a list in the single line '''


def printing_same_line(n):
    s = len(n)
    for i in range(s):  
        print(n[i], end=" ")


def Print_list(list):
    for item in list:
        print(item, end = " " )




countries = ['Japan', 'China', 'Germany', 'Turkey', 'America', 'Saudi Arabia']
printing_same_line(countries)

print()

Print_list(countries)