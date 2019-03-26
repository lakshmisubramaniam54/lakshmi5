#lakshmi
n1=int(input())
n2=list(map(int,input().split()))
c=[]
for i in range(0,n1):
  if i%2==0 and n2[i]%2!=0:
    c.append(n2[i])
  elif i%2!=0 and n2[i]%2==0:
    c.append(n2[i])
print(*c)
