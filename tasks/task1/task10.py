d=[0,1]
print(d[0],end=" ")
print(d[1],end=" ")
for i in range(2,10):
    x=d[i-2]
    t=d[i-1]
    d.append(x+t)
    print(d[i],end=" ")
