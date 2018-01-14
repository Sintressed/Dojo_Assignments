print 'starting the program...'
import random
a = 0
b = 0
q = ''
for count in range(0,5001):
    x = random.randint(0,1)
    if x == 0:
        a = a + 1
        q = 'head'
    elif x == 1:
        b = b + 1
        q = 'tails'

    print 'Attempt #',count,': Throwing a coin...','It is a ',q,'! ... Got', a, 'head(s) so far and', b ,'tail(s) so far' 