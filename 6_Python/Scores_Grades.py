import random
for count in range(0,10):
    x = random.randint(60,100)
    if x > 60 and x < 69:
        print 'score: ',x,'; your grade is D'
    elif x > 70 and x < 69:
        print 'score: ',x,'; your grade is C'
    elif x > 80 and  x < 89:
        print 'score: ',x,'; your grade is B'
    elif x > 90 and  x < 100:
        print 'score: ',x,'; your grade is A'
print 'end of program, BYE!'