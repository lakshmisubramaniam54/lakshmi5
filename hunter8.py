import sys, string, math
n=int(input())
n1=list(map(int,input().split()))
n2=[]
len1=len(n1)
for i in range(0,len1-2):
  for j in range(i+1,len1-1):
    for k in range(j+1,len1):
      if n1[i]+n1[j]==n1[k]:
        print(n1[i],n1[j],n1[k])
