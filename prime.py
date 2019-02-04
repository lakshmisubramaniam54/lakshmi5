num=int(raw_input())
if num>1 :
  for i in range (2,num//2):
    if (num%i) == 0:
      print("No")
      break
    else:
      print("Yes")
else:
  print("Yes")
