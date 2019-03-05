x =[1,2,3,43,4,2,3,4,52,21,4,5,2]
print(sorted(x))
x = "goddsd"
print(''.join(sorted(x)))
x = "this is kenya"
print(x.replace(' ', '%20'))
x = {'this': 1, "is" : 2, "kenya" : 3}
print(len(x))
x,y = 'aabccccccaa',[]

for i in x:
    if len(y) == 0:
        y.append([i,1])
    else:
        if y[-1][0] == i:
            y[-1][1] += 1
        else:
            y.append([i,1])

res = []
for i in y:
    i[1] = str(i[1])
    res.append(''.join(i))

print(''.join(res))

