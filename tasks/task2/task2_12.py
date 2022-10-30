#a

x =int(input("Enter the Value of the num "))

a =(2**x)%10
print("The Last digits of the num " , a)
#b
x =int(input("Enter the Value of the num "))

a =(2**x)%100
print("The Last 2digits of the num " , a)
#c
x =int(input("Enter the Value of the num "))
c =int(input("how many digit you want  "))


a =(2**x)%(10**c)
print("The Last digits of the num " , a)