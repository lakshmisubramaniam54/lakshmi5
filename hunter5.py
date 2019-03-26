#lakshmi
n1=int(input())
a=str(n1)
c=0
for i in range(0,len(a)):
  if int(a[i:i+2])<26 and len(str(int(a[i:i+2])))==2:
    c=c+1
if c==2:
  print(c+c//2)
else:
  print(c+c//2+1)
