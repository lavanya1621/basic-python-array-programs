a=[1,0,2,1,0,2,2,0,1]
c0=0
c1=0
c2=0
for i in range(0,len(a)):
    if a[i]==0:
        c0=c1+1
    elif a[i]==1:
        c1=c1+1
    elif a[i]==2:
        c2=c2+1
  
j=0
print(c1,c2,c0)
while(c0>0):
        a[j]=0
        j+=1
        c0-=1
print(a)
while(c1>0):
        a[j]=1
        j+=1
        c1-=1
print(a)    
while(c2>0):
        a[j]=2
        j+=1
        c2-=1
print(a)