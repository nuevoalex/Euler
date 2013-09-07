ways = [0]*201
ways[0] = 1
for x in [1,2,5,10,20,50,100,200]:
    for i in xrange(x, 201):
        ways[i] += ways[i-x]
print ways[200]
