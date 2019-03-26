#lakshmi
n1=int(input())
n2=list(map(int,input().split()))
li=[0]*10
for i in range(0,n1):
  li[n2[i]]+=1
for i in range(0,len(li)):
  if li[i]==1:
    print(i)
