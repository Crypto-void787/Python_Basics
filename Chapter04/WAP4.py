# take the sub's name n marks as input n returning 'em as key:value pair 

Student_grade_book = { }

key = input("Enter the 1st subject name: ")
value = input("Enter it's marks: ")
Student_grade_book.update({key : value})

key = input("Enter the 2nd subject name: ")
value = input("Enter it's marks: ")
Student_grade_book.update({key : value})

key = input("Enter the 3rd subject name: ")
value = input("Enter it's marks: ")
Student_grade_book.update({key : value})

print("Here's ur record:\n" , Student_grade_book)
