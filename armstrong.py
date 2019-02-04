num=int(input())
sum = 0
temp = 0
while temp>0:
 digit = temp%10
 sum+=digit**3
 temp//=10
if num==sum:
 print("Yes")
else:
 print("No")
