a,b=input().split()
count1=0
count2=0
for i in a:
  count1+=1
for j in b:
  count2+=1
if (count2>count1):
  print(b)
elif (count1>count2):
  print(a)
else:
  print(b)
