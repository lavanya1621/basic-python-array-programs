s=int(input("Enter size of array"))
a=[]
for i in range(s):
    r=int(input("Write element number"))
    a.insert(i,r)

print(a)
    
def findsum(a,s):
    if s==1:
        return a[0]
    else:
        if a[0]>a[1]:
            max=a[0]
            min=a[1]
        elif a[0]<a[1]:
            min=a[0]
            max=a[1]
        
        for i in range(2,s):
            if a[i]>max:
                max=a[i]
            elif a[i]<min:
                min=a[i]
    print(min)
    print(max)
    print(max+min)

findsum(a,s)
        






