a=int(input("Enter a number :"))
b=int(input("Enter a number :"))
c=int(input("Enter a number :"))
d=int(input("Enter a number :"))
e=int(input("Enter a number :"))
if (a>b & a>c & a>d & a>e):
    print("large number is ", a)
elif (b>a & b>c & b>d & b>e):
    print("large number is ", b)
elif (c>a & c>b & c>d & c>e):
    print("large number is ", c)
elif (d>a & d>b & d>c & d>e):
    print("large number is ", d)
else:
    print("large number is ", e)