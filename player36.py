def player_36():
    n,k=input().split()
    c=0
    for i in range(len(n)):
        for k in n[i]:
            c+=1
    print(c)
player_36()
        
