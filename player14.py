n,b=list(input()),[]
for i in range(len(n)):
    if n[i] in 'aeiou':
    b.append(i)
f=n[::-1]
b.sort(reverse=True)
for i in range (len(b)):
f.pop(b[i])
print(''.join(f))



    
    
