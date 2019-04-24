#lakshmi
s=int(input())
y=[]
for x in range(2,s+1):
  if(s%x==0):
    o=0
    for i in range(1,x+1):
      if(x%i==0):
        o=o+1
    if(o==2):
      y.append(x)
for i in range(0,len(y)):
  if(i==len(y)-1):
    print(y[i])
  else:
    print(y[i],end=(' '))
