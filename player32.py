#lakshmi
n,k=map(int,input().split())
li=list(map(int,input().split()))
for i in li:
  if i==k:
    print("Yes")
    break
else:
  print("No")
