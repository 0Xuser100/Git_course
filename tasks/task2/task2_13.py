x=int(input("enter num you want"))

if x % 4 == 0 or x % 100 != 0 and x % 400 == 0:
    print("leap")
else:
    print("not leap")