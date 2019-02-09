num1,num2=input().split()
num1=int(num1)
num2=int(num2)
for i in range(num1,num2+1):
    if(i%2 != 0):
      print(i,end=" ")
