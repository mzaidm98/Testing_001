
#a = float(1)
#b = float(7)
#c = float(6)

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if (a >= b) and (a >= c):
    print ('The largest number is', a)

elif (b >= a) and (b >= c):
    print ('The largest number is', b)

else:
    print ('The largest number is', c)


