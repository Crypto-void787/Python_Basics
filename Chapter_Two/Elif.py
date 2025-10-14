
# grading students according to their marks 

Marks = int(input("Enter your marks: "))

if Marks == 90 : 
    print("Grade: A+")

elif Marks >= 80 and Marks <= 90 :
    print("Grade: A")
        
elif Marks >= 70 and Marks <= 80 :
    print("Grade: B")

elif Marks >= 50 and Marks <=70 :
    print("Grade: C")

elif Marks >= 40 and Marks <=50 :
    print("Grade: D")

else:
    print("Grade: E")    

