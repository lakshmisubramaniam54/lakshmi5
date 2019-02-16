n1=int(input())
n2,n3=input().split()
n2=int(n2)
n3=int(n3)
if n1 in range(n2,n3):
    print("yes")
else:
    print("no")
