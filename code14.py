a=input(" Enter Subject Name : ")
b='Enter marks of ',a,' : '
c=int(input(b))
if(c>100):
    print("Please enter valid marks")
elif(c>80):
    print("Grade of ",a," A")
elif(c>60):
    print("Grade of ",a," B")
elif(c>40):
    print("Grade of ",a," C")
else:
    print("Grade of ",a," D")