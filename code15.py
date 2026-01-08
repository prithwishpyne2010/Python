sub1=int(input("Marks of Eng : "))
sub2=int(input("Marks of Bng : "))
sub3=int(input("Marks of Mat : "))
sub4=int(input("Marks of His : "))
sub5=int(input("Marks of Geo : "))
tMarks=sub1+sub2+sub3+sub4+sub5
print("Total Marks: ",tMarks)
pMarks=tMarks/5
if(pMarks>100):
    print("Please enter valid marks")
elif(pMarks>80):
    print("Grade A")
elif(pMarks>60):
    print("Grade B")
elif(pMarks>40):
    print("Grade C")
else:
    print("Grade D")