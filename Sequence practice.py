
#TUPLE TUPLE TUPLE TUPLE TUPLE
a=(1,2,3,4,5)
print(type(a))#it prints the type of 'a' to be a tuple.
print(len(a))
print(a + (6,7,8))
print(a[2:5])
b = (10,)
c = 365,
print(b,type(b))
print(c,type(c))
print()

#...................................................................................

x=(1,2,3,4,5,4,3,2,1)
print(x.count(1))
print()
print("sum=",sum(x))
print()

#....................................................................................

x1=int(input("Enter x1 coordinate:"))
y1=int(input("Enter y1 coordinate:"))
coordinates1=(x1,y1) #here, coordinates is a tupule that contains object,x and y.
print()

x2=int(input("Enter x2 coordinate:"))
y2=int(input("Enter y2 coordinate:"))
coordinates2=(x2,y2)
print()

x3=int(input("Enter x3 coordinate:"))
y3=int(input("Enter y3 coordinate:"))
coordinates3=(x3,y3)
print()

x4=int(input("Enter x4 coordinate:"))
y4=int(input("Enter y4 coordinate:"))
coordinates4=(x4,y4)
print()

x5=int(input("Enter x5 coordinate:"))
y5=int(input("Enter y5 coordinate:"))
coordinates5=(x5,y5)
print()

#Till here, we have created and assigned 5 tuples.
#Now, all 5 tuples are packed in one list named "coordinates"

coordinates =[coordinates1, coordinates2, coordinates3, coordinates4, coordinates5]
print(coordinates, type(coordinates))
print()



#.............................................................................................




