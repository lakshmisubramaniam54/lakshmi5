#lakshmi
n1=int(input())
n2=list(map(int,input().split()))
n3=[]
flag=0
for i in range(0,n1):
  if i==n2[i]:
    n3.append(i)
    flag=1
if flag==1:
  print(*n3)
else:
  print('-1')
