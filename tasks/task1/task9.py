def isprim(n):
    if(n==2):
        return True
    if((n<2)|(n%2==0)):
        return False
    for i in range (3,n,2):
        if(n%i==0):
            return False
        if(i*i>n):
            break
    return True
s=int(input("enter start point "))
e=int(input("enter end point "))
for i in range(s,e+1):
    if(isprim(i)):
        print(i)
